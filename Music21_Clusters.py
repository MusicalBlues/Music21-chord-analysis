#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:47:10 2018

@author: Dimihollo
"""

import PDF_to_music
import sys
from music21 import *


score = converter.parse('/Users/Dimihollo/Desktop/47655144-Bill-Evans-The-two-Lonely-People.xml')
#n1 = score.flat.getElementsByClass('Chord')[6]
#n2 = score.pitches
#print(n2[3])
#print(n1)
#print(voiceLeading.getVerticalityFromObject(n1, score))

scoreTree = tree.fromStream.asTimespans(score, flatten=True,
                                        classList=(note.Note, chord.Chord))

verticality = scoreTree.getVerticalityAt(0)                              
i=0          
while i <= 5 :
#    verticality = scoreTree.getVerticalityAt()
    new_v = verticality.nextVerticality
    print(verticality)
#    print(verticality.bassTimespan)
#    print(new_v)
    verticality=new_v
    pitch_class = verticality.pitchClassSet
#    print(pitch_class)
    i += 1
    
