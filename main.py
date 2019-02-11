#!/usr/bin/env python

import sys
from modules import *

with open(sys.argv[2]) as f:
    parts = f.read().strip().split('\n')
    print({
        "patterncount": lambda: patterncount.PatternCount(parts[0], parts[1]),
        "frequentwords": lambda: frequentwords.FrequentWords(parts[0], int(parts[1])),
	"reversecomplement": lambda: reversecomplement.ReverseComplement(parts[0]),
	"patternmatching": lambda: patternmatching.PatternMatching(parts[1], parts[0])
    }[sys.argv[1]]())

