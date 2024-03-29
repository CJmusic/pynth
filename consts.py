import numpy as np
import matplotlib.pyplot as plt

MIDI_NOTES = {
    'C1-2': [ 0,      8.1757989156],
    'Db-2': [ 1,      8.6619572180],
    'D-2': [  2,      9.1770239974],
    'Eb-2': [ 3,      9.7227182413],
    'E-2': [  4,      10.3008611535],
    'F-2': [  5,      10.9133822323],
    'Gb-2': [ 6,      11.5623257097],
    'G-2': [  7,      12.2498573744],
    'Ab-2': [ 8,      12.9782717994],
    'A-2': [  9,      13.7500000000],
    'Bb-2': [ 10,     14.5676175474],
    'B-2': [  11,     15.4338531643],

    'C-1': [  12,     16.3515978313],
    'Db-1': [ 13,     17.3239144361],
    'D-1': [  14,     18.3540479948],
    'Eb-1': [ 15,     19.4454364826],
    'E-1': [  16,     20.6017223071],
    'F-1': [  17,     21.8267644646],
    'Gb-1': [ 18,     23.1246514195],
    'G-1': [  19,     24.4997147489],
    'Ab-1': [ 20,     25.9565435987],
    'A-1': [  21,     27.5000000000],
    'Bb-1': [ 22,     29.1352350949],
    'B-1': [  23,     30.8677063285],

    'C0': [   24,     32.7031956626],
    'Db0': [  25,     34.6478288721],
    'D0': [   26,     36.7080959897],
    'Eb0': [  27,     38.8908729653],
    'E0': [   28,     41.2034446141],
    'F0': [   29,     43.6535289291],
    'Gb0': [  30,     46.2493028390],
    'G0': [   31,     48.9994294977],
    'Ab0': [  32,     51.9130871975],
    'A0': [   33,     55.0000000000],
    'Bb0': [  34,     58.2704701898],
    'B0': [   35,     61.7354126570],

    'C1': [   36,     65.4063913251],
    'Db1': [  37,     69.2956577442],
    'D1': [   38,     73.4161919794],
    'Eb1': [  39,     77.7817459305],
    'E1': [   40,     82.4068892282],
    'F1': [   41,     87.3070578583],
    'Gb1': [  42,     92.4986056779],
    'G1': [   43,     97.9988589954],
    'Ab1': [  44,     103.8261743950],
    'A1': [   45,     110.0000000000],
    'Bb1': [  46,     116.5409403795],
    'B1': [   47,     123.4708253140],

    'C2': [   48,     130.8127826503],
    'Db2': [  49,     138.5913154884],
    'D2': [   50,     146.8323839587],
    'Eb2': [  51,     155.5634918610],
    'E2': [   52,     164.8137784564],
    'F2': [   53,     174.6141157165],
    'Gb2': [  54,     184.9972113558],
    'G2': [   55,     195.9977179909],
    'Ab2': [  56,     207.6523487900],
    'A2': [   57,     220.0000000000],
    'Bb2': [  58,     233.0818807590],
    'B2': [   59,     246.9416506281],

    'C3': [   60,     261.6255653006],
    'Db3': [  61,     277.1826309769],
    'D3': [   62,     293.6647679174],
    'Eb3': [  63,     311.1269837221],
    'E3': [   64,     329.6275569129],
    'F3': [   65,     349.2282314330],
    'Gb3': [  66,     369.9944227116],
    'G3': [   67,     391.9954359817],
    'Ab3': [  68,     415.3046975799],
    'A3': [   69,     440.0000000000],
    'Bb3': [  70,     466.1637615181],
    'B3': [   71,     493.8833012561],

    'C4': [   72,     523.2511306012],
    'Db4': [  73,     554.3652619537],
    'D4': [   74,     587.3295358348],
    'Eb4': [  75,     622.2539674442],
    'E4': [   76,     659.2551138257],
    'F4': [   77,     698.4564628660],
    'Gb4': [  78,     739.9888454233],
    'G4': [   79,     783.9908719635],
    'Ab4': [  80,     830.6093951599],
    'A4': [   81,     880.0000000000],
    'Bb4': [  82,     932.3275230362],
    'B4': [   83,     987.7666025122],

    'C5': [   84,     1046.5022612024],
    'Db5': [  85,     1108.7305239075],
    'D5': [   86,     1174.6590716696],
    'Eb5': [  87,     1244.5079348883],
    'E5': [   88,     1318.5102276515],
    'F5': [   89,     1396.9129257320],
    'Gb5': [  90,     1479.9776908465],
    'G5': [   91,     1567.9817439270],
    'Ab5': [  92,     1661.2187903198],
    'A5': [   93,     1760.0000000000],
    'Bb5': [  94,     1864.6550460724],
    'B5': [   95,     1975.5332050245],

    'C6': [   96,     2093.0045224048],
    'Db6': [  97,     2217.4610478150],
    'D6': [   98,     2349.3181433393],
    'Eb6': [  99,     2489.0158697766],
    'E6': [   100,    2637.0204553030],
    'F6': [   101,    2793.8258514640],
    'Gb6': [  102,    2959.9553816931],
    'G6': [   103,    3135.9634878540],
    'Ab6': [  104,    3322.4375806396],
    'A6': [   105,    3520.0000000000],
    'Bb6': [  106,    3729.3100921447],
    'B6': [   107,    3951.0664100490],

    'C7': [   108,    4186.0090448096],
    'Db7': [  109,    4434.9220956300],
    'D7': [   110,    4698.6362866785],
    'Eb7': [  111,    4978.0317395533],
    'E7': [   112,    5274.0409106059],
    'F7': [   113,    5587.6517029281],
    'Gb7': [  114,    5919.9107633862],
    'G7': [   115,    6271.9269757080],
    'Ab7': [  116,    6644.8751612791],
    'A7': [   117,    7040.0000000000],
    'Bb7': [  118,    7458.6201842894],
    'B7': [   119,    7902.1328200980],
    
    'C8': [   120,    8372.0180896192],
    'Db8': [  121,    8869.8441912599],
    'D8': [   122,    9397.2725733570],
    'Eb8': [  123,    9956.0634791066],
    'E8': [   124,    10548.0818212118],
    'F8': [   125,    11175.3034058561],
    'Gb8': [  126,    11839.8215267723],
    'G8': [  127,     12543.8539514160]
}  

global odd  

odd = np.empty((15,))
odd[::2] = 1
odd[1::2] = 0

def osc_sine(s, fs, pitch):  
    wave = np.sin(s/fs*2*np.pi*pitch)
    return wave

def osc_saw(s, fs, pitch):
    if type(s) == np.array:
        wave = np.zeros(len(s))
    else:
        wave = 0.0
    for n in range(0,len(odd),1):
	    wave += (-1)**(n-1)*1.0/(n+1)*np.sin(2*np.pi*pitch*(n+1)*s/fs)
    return wave
  

def osc_square(s, fs, pitch):
    if type(s) == np.array:
        wave = np.zeros(len(s))
    else:
        wave = 0.0
    for n in range(0,len(odd),1):
	    wave += odd[n]*1.0/(n+1)*np.sin(2*np.pi*pitch*(n+1)*s/fs)
    return wave

def osc_triangle(s, fs, pitch):
    if type(s) == np.array:
        wave = np.zeros(len(s))
    else:
        wave = 0.0
    for n in range(0,len(odd),1):
	    wave += odd[n]*0.8/((n+1)**2)*np.cos(2*np.pi*pitch*(n+1)*s/fs)
    return wave

if __name__ == "__main__":
    s = np.linspace(0,10000.0,10000.0)
    fig = plt.figure()

    ax1 = fig.add_subplot(411)
    WAVE = osc_sine(s, 44100.0, 10.0)#[]
    ax1.plot(WAVE)
    ax1.set_yticks([])
    ax1.set_xticks([])
    plt.title('Synthesizer Waveforms')
    plt.ylabel('Sine')
    

    ax2 = fig.add_subplot(412)
    WAVE = osc_triangle(s, 44100.0, 10.0)
    plt.plot(WAVE)
    ax2.set_yticks([])
    ax2.set_xticks([])

    plt.ylabel('Triangle')
    

    ax3 = fig.add_subplot(413)
    WAVE = osc_saw(s, 44100.0, 10.0)#[]
    plt.plot(WAVE)
    plt.ylabel('Saw')
    ax3.set_yticks([]) # labels along the bottom edge are off
    ax3.set_xticks([])

    ax4 = fig.add_subplot(414)
    WAVE = osc_square(s, 44100.0, 10.0)#[]
    plt.plot(WAVE)
    plt.ylabel('Square')
    ax4.set_yticks([])
    ax4.set_xticks([])
    # plt.show()    
    plt.savefig('waveforms.png')