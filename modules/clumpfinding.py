def word_frequencies(genome, k):
    patterns = {}
    iterLen = len(genome)-k+1
    for i in range(0, iterLen):
        pattern = genome[i:i+k]
        if pattern not in patterns:
            patterns[pattern] = 1
        else:
            patterns[pattern] += 1
    return patterns

def word_counts(patterns):
    counts = {}
    for ptr, count in patterns.items():
        if count not in counts:
            counts[count] = [ptr]
        else:
            counts[count].append(ptr)
    return counts

def ClumpFinding(genome, k, L, t):
    clumps = []
    clumpWin = genome[0:L]
    patterns = word_frequencies(clumpWin, k)
    counts = word_counts(patterns)
    maxCount = max(counts)
    if maxCount >= t:
        clumps = counts[maxCount]
    iterLen = len(genome)-L+1
    for i in range(1, iterLen):
        ptr = genome[i-1:i-1+k]
        if ptr in patterns:
            patterns[ptr] -= 1
        else:
            patterns[ptr] = -1
        ptr = genome[i+L-k:i+L]
        if ptr in patterns:
            patterns[ptr] += 1
        else:
            patterns[ptr] = 1
        if patterns[ptr] >= t:
            clumps.append(ptr)
    return set(clumps)

