from . import patterncount

def FrequentWords(txt, k):
    patterns = []
    counts = []
    iterLen = len(txt)-k
    for i in range(0, iterLen):
        pattern = txt[i:i+k]
        counts.append(patterncount.PatternCount(txt, pattern))
    maxCount = max(counts)
    for i in range(0, iterLen):
        if counts[i] == maxCount:
            patterns.append(txt[i:i+k])
    patterns = sorted(set(patterns))
    return ' '.join(patterns)
