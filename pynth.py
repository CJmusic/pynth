import matplotlib.pyplot as plt
import scipy
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import scipy.signal as sig
from scipy.signal import butter, lfilter, freqz
import numpy as np
# import wavio

from consts import *

class pynth: 
    def __init__(self, name, osc, amp, filt, seq):
        ##First step is to read in the synth parameters from the input
        osc = osc
        amp = amp
        seq = seq
        filt = filt

        fs = 44100

        bpm = seq['bpm']
        div = seq['div']
        gate = seq['gate'] #in percentage
        SEQ = seq['SEQ']


        att = amp['att']
        dec = amp['dec']
        sus = amp['sus']
        rel = amp['rel']

        filt_on = filt['on']
        cutoff = filt['cutoff']
        
        ##now calculate the length of each note in the sequence in both time(seconds) and samples
        note_length = 1.0/(bpm/60.0)*float(div)
        note_length_s = 1.0/(bpm/60.0)*float(div)*fs

        seq_length = note_length*len(SEQ)
        seq_length_s = note_length_s*len(SEQ)       


        ##Calculate the envelope
        rel_on = False 
        att_on = True
        env = 0.0
        ENV = [] #the envelope array

        for i in range(int(note_length_s)):
            if att_on == True:
                env += 1.0/((att/1000.0)*fs)
            if env >= 0.9: 
                att_on = False
            if att_on == False:
                if i > gate*note_length_s: 
                    rel_on = True
                if rel_on == False:
                    env -= 1.0/((dec/1000.0)*fs)
                    if env < sus:
                        env = sus 
                if rel_on == True:
                    env -= sus/((rel/1000.0)*fs)
            if env < 0.0:
                env = 0.0
            ENV.append(env)

        plt.plot(ENV)
        plt.xlabel('Sample')
        plt.ylabel('Amplitude')
        plt.title('Envelope')
        plt.savefig('envelope.png')
        
        s = np.linspace(0,note_length_s,note_length_s)
        # s = range(0,note_length_s,note_length_s)

        WAVE = []
        for i in range(len(SEQ)):
            pitch = MIDI_NOTES[SEQ[i]][1]
            for j in range(int(note_length_s)): 
                wave = ENV[j]*self.osc_selector(osc,s[j],fs,pitch)
                WAVE.append(wave)

        if filt_on == True:
            WAVE = self.butter_lowpass_filter(WAVE, cutoff, fs, 5)

        plt.plot(WAVE)
        plt.savefig('wave.png')
        # plt.show()

        # wavio.write('%s.wav' % name, np.array(WAVE), 44100, sampwidth=3)
        scipy.io.wavfile.write('%s.wav' % name, 44100, np.array(WAVE))

    def osc_selector(self,osc,s,fs,pitch):
        if osc == 'sine':
            return osc_sine(s,fs,pitch)
        if osc == 'square':
            return osc_square(s,fs,pitch)
        if osc == 'saw':
            return osc_saw(s,fs,pitch)
        if osc == 'triangle':
            return osc_triangle(s,fs,pitch)

    #thanks Stack Overflow!        
    def butter_lowpass(self, cutoff, fs=44100, order=5):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = sig.butter(order, normal_cutoff, btype='low', analog=False)
        return b, a

    def butter_lowpass_filter(self, data, cutoff, fs, order=5):
        b, a = self.butter_lowpass(cutoff, fs, order=order)
        y = sig.lfilter(b, a, data)
        return y

            


amp = {'att': 10,'dec': 30,'sus': 0.5,'rel': 30}#[att, dec, sus, rel]
osc = 'square'#[sine, saw, square, triangle]
seq = {'bpm': 85,'div': 0.25,'gate': 0.75, 'SEQ': ['C3']}#, 'C3', 'B3', 'B2', 'C3', 'C3','B3','C3']}#[bpm, div, gate, SEQ]
filt = {'on': True, 'cutoff': 1000}


pynth('pynth',osc,amp,filt,seq)

