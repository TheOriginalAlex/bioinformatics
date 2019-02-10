#!/usr/bin/env python

import sys
from modules import *

with open(sys.argv[2]) as f:
    parts = f.read().strip().split('\n')
    print({
        "patterncount": lambda: patterncount.PatternCount(parts[0], parts[1]),
        "frequentwords": lambda: frequentwords.FrequentWords(parts[0], int(parts[1]))
    }[sys.argv[1]]())
