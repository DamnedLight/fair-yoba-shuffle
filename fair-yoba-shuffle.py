#!/usr/bin/env python3

import random
import itertools

sequence = []
for player in ['Seröga', 'Oleg', 'Kolän', 'Dimon', 'Yura']:
    sequence += [player] * 6

random.shuffle(sequence)
for seqnum, player in itertools.zip_longest(range(1,31), sequence):
    print("%2s: %s" % (seqnum, player))
