from pynth import *


# amp = {'att': 10,'dec': 30,'sus': 0.5,'rel': 30}#[att, dec, sus, rel]
# osc = 'square'#[sine, saw, square, triangle]
# seq = {'bpm': 100,'div': 1.0,'gate': 0.75, 'SEQ': ['C3', 'C3', 'B3', 'B2', 'C3', 'C3','B3','C3']}#[bpm, div, gate, SEQ]
# filt = {'on': True, 'cutoff': 1000}


# pynth('files/pynth',osc,amp,filt,seq)



# ###Pad Chords###
amp = {'att': 2000,'dec': 3000,'sus': 0.2,'rel': 300}#[att, dec, sus, rel]
osc = 'saw'#[sine, saw, square, triangle]
filt = {'on': True, 'cutoff': 800}

seq1 = {'bpm': 50,'div': 4.0,'gate': 0.8, 'SEQ': ['D2']}#[bpm, div, gate, SEQ]
seq2 = {'bpm': 50,'div': 4.0,'gate': 0.8, 'SEQ': ['F2']}#[bpm, div, gate, SEQ]
seq3 = {'bpm': 50,'div': 4.0,'gate': 0.8, 'SEQ': ['A2']}#[bpm, div, gate, SEQ]

pynth('files/A-pad1-D2',osc,amp,filt,seq1)
pynth('files/A-pad1-F2',osc,amp,filt,seq2)
pynth('files/A-pad1-A2',osc,amp,filt,seq3)


seq1 = {'bpm': 50,'div': 4.0,'gate': 0.8, 'SEQ': ['C2']}#[bpm, div, gate, SEQ]
seq2 = {'bpm': 50,'div': 4.0,'gate': 0.8, 'SEQ': ['F2']}#[bpm, div, gate, SEQ]
seq3 = {'bpm': 50,'div': 4.0,'gate': 0.8, 'SEQ': ['A2']}#[bpm, div, gate, SEQ]

pynth('files/A-pad2-C2',osc,amp,filt,seq1)
pynth('files/A-pad2-F2',osc,amp,filt,seq2)
pynth('files/A-pad2-A2',osc,amp,filt,seq3)


seq1 = {'bpm': 50,'div': 4.0,'gate': 0.8, 'SEQ': ['C2']}#[bpm, div, gate, SEQ]
seq2 = {'bpm': 50,'div': 4.0,'gate': 0.8, 'SEQ': ['E2']}#[bpm, div, gate, SEQ]
seq3 = {'bpm': 50,'div': 4.0,'gate': 0.8, 'SEQ': ['A2']}#[bpm, div, gate, SEQ]
seq4 = {'bpm': 50,'div': 4.0,'gate': 0.8, 'SEQ': ['E3']}#[bpm, div, gate, SEQ]
seq5 = {'bpm': 50,'div': 4.0,'gate': 0.8, 'SEQ': ['A1']}#[bpm, div, gate, SEQ]

pynth('files/A-pad2-C2',osc,amp,filt,seq1)
pynth('files/A-pad2-E2',osc,amp,filt,seq2)
pynth('files/A-pad2-A2',osc,amp,filt,seq3)
pynth('files/A-pad2-E3',osc,amp,filt,seq4)
pynth('files/A-pad2-A1',osc,amp,filt,seq5)


seq1 = {'bpm': 100,'div': 4.0,'gate': 0.8, 'SEQ': ['D2']}#[bpm, div, gate, SEQ]
seq2 = {'bpm': 100,'div': 4.0,'gate': 0.8, 'SEQ': ['G2']}#[bpm, div, gate, SEQ]
seq3 = {'bpm': 100,'div': 4.0,'gate': 0.8, 'SEQ': ['Bb2']}#[bpm, div, gate, SEQ]

pynth('files/A-pad3-D2',osc,amp,filt,seq1)
pynth('files/A-pad3-G2',osc,amp,filt,seq2)
pynth('files/A-pad3-BB2',osc,amp,filt,seq3)

seq1 = {'bpm': 100,'div': 4.0,'gate': 0.8, 'SEQ': ['D2']}#[bpm, div, gate, SEQ]
seq2 = {'bpm': 100,'div': 4.0,'gate': 0.8, 'SEQ': ['F2']}#[bpm, div, gate, SEQ]
seq3 = {'bpm': 100,'div': 4.0,'gate': 0.8, 'SEQ': ['A2']}#[bpm, div, gate, SEQ]
seq4 = {'bpm': 100,'div': 4.0,'gate': 0.8, 'SEQ': ['C2']}#[bpm, div, gate, SEQ]

pynth('files/A-pad4-D2',osc,amp,filt,seq1)
pynth('files/A-pad4-F2',osc,amp,filt,seq2)
pynth('files/A-pad4-A2',osc,amp,filt,seq3)
pynth('files/A-pad4-C2',osc,amp,filt,seq4)



#####


###Bass Sound
amp = {'att': 5,'dec': 30,'sus': 0.5,'rel': 5}#[att, dec, sus, rel]
osc = 'triangle'#[sine, saw, square, triangle]
seq = {'bpm': 100,'div': 2.0,'gate': 1.0, 'SEQ': ['D1', 'F1', 'D1', 'E1']}#[bpm, div, gate, SEQ]
filt = {'on': True, 'cutoff': 500}
# pynth('files/A-bass1-D',osc,amp,filt,seq)

# seq = {'bpm': 100,'div': 2.0,'gate': 1.0, 'SEQ': ['F1', 'C1', 'A1', 'E1']}
# pynth('files/A-bass2-F',osc,amp,filt,seq)


# seq = {'bpm': 100,'div': 4.0,'gate': 1.0, 'SEQ': ['C1']}
# pynth('files/A-bass3-A',osc,amp,filt,seq)


seq = {'bpm': 100,'div': 1.0,'gate': 1.0, 'SEQ': ['F1']}
pynth('files/A-bass4-F',osc,amp,filt,seq)

seq = {'bpm': 100,'div': 4.0,'gate': 1.0, 'SEQ': ['G1', 'A1']}
pynth('files/A-bass4-G-A',osc,amp,filt,seq)
#####


###Melody Lead


####




###Arp 1 
pynth('files/A-arp1-D',osc,amp,filt,seq)

seq = {'bpm': 200,'div': 0.5,'gate': 1.0, 'SEQ': ['F4', 'A4', 'C4', 'A5', 'F5', 'C4']}#[bpm, div, gate, SEQ]
pynth('files/A-arp1-F',osc,amp,filt,seq)


seq = {'bpm': 200,'div': 0.5,'gate': 1.0, 'SEQ': ['A4', 'C4', 'E4', 'A5', 'G5', 'C4']}#[bpm, div, gate, SEQ]
pynth('files/A-arp1-Am7',osc,amp,filt,seq)

seq = {'bpm': 200,'div': 0.5,'gate': 1.0, 'SEQ': ['G4', 'Bb4', 'D4', 'Bb5', 'G5', 'F4']}#[bpm, div, gate, SEQ]
pynth('files/A-arp1-Gm',osc,amp,filt,seq)


seq = {'bpm': 200,'div': 0.5,'gate': 1.0, 'SEQ': ['F4', 'A4', 'C4', 'F5', 'A5', 'E4']}#[bpm, div, gate, SEQ]
pynth('files/A-arp1-F2',osc,amp,filt,seq)

###



###Arp 2
amp = {'att': 50,'dec': 100,'sus': 0.5,'rel': 500}#[att, dec, sus, rel]
osc = 'square'#[sine, saw, square, triangle]
seq = {'bpm': 200,'div': 0.5,'gate': 1.0, 'SEQ': ['D4', 'F4', 'A4', 'D5', 'A5', 'F4']}#[bpm, div, gate, SEQ]
filt = {'on': False, 'cutoff': 20000}
pynth('files/A-arp2-D',osc,amp,filt,seq)

seq = {'bpm': 200,'div': 0.5,'gate': 1.0, 'SEQ': ['F4', 'A4', 'C4', 'A5', 'F5', 'C4']}#[bpm, div, gate, SEQ]
pynth('files/A-arp2-F',osc,amp,filt,seq)


seq = {'bpm': 200,'div': 0.5,'gate': 1.0, 'SEQ': ['A4', 'C4', 'E4', 'A5', 'G5', 'C4']}#[bpm, div, gate, SEQ]
pynth('files/A-arp2-Am7',osc,amp,filt,seq)

seq = {'bpm': 200,'div': 0.5,'gate': 1.0, 'SEQ': ['G4', 'Bb4', 'D4', 'Bb5', 'G5', 'F4']}#[bpm, div, gate, SEQ]
pynth('files/A-arp2-Gm',osc,amp,filt,seq)


seq = {'bpm': 200,'div': 0.5,'gate': 1.0, 'SEQ': ['F4', 'A4', 'C4', 'F5', 'A5', 'E4']}#[bpm, div, gate, SEQ]
pynth('files/A-arp2-F2',osc,amp,filt,seq)


seq = {'bpm': 200,'div': 0.5,'gate': 1.0, 'SEQ': ['F4', 'A4', 'C4', 'F5', 'A5', 'E4']}#[bpm, div, gate, SEQ]
pynth('files/A-arp2-F2',osc,amp,filt,seq)

###




# ##Sparkle 
amp = {'att': 2000,'dec': 900,'sus': 0.2,'rel': 3000}#[att, dec, sus, rel]
osc = 'saw'#[sine, saw, square, triangle]
filt = {'on': True, 'cutoff': 15000}

seq1 = {'bpm': 50,'div': 8.0,'gate': 0.2, 'SEQ': ['D5']}#[bpm, div, gate, SEQ]
pynth('files/A-sparkleD',osc,amp,filt,seq1)
