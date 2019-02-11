from . import patterncount

def FrequentWords(txt, k):
    counts = {}
    iterLen = len(txt)-k+1
    for i in range(0, iterLen):
        pattern = txt[i:i+k]
        count = patterncount.PatternCount(txt, pattern)
        if count in counts:
            counts[count].append(pattern)
        else:
            counts[count] = [pattern]
    patterns = sorted(set(counts[max(counts)]))
    return patterns
