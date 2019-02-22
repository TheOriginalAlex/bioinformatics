def word_frequencies(genome, k):
    patterns = {}
    iterLen = len(genome)-k+1
    for i in range(0, iterLen):
        pattern = genome[i:i+k]
        if pattern not in patterns:
            patterns[pattern] = 1
        else:
            patterns[pattern] += 1
    counts = {}
    for ptr, count in patterns.items():
        if count not in counts:
            counts[count] = [ptr]
        else:
            counts[count].append(ptr)
    return counts

def ClumpFinding(genome, k, L, t):
    patterns = {}
    iterLen = len(genome)-L+1
    clumps = []
    for i in range(0, iterLen):
        clumpWin = genome[i:i+L]
        counts = word_frequencies(clumpWin, k)
        maxCount = max(counts)
        if maxCount >= t:
            clumps = clumps + counts[maxCount]
            clumps = list(set(clumps))
    return clumps

