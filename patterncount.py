#!/usr/bin/env python

import sys

def PatternCount(txt, pattern):
    count = 0
    iterLen = len(txt)-len(pattern)
    for i in range(0, iterLen):
        if txt[i:i+len(pattern)] == pattern:
            count += 1
    return count

with open(sys.argv[1]) as f:
    parts = f.read().split('\n')
    print(PatternCount(parts[0], parts[1]))
