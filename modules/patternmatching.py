def PatternMatching(genome, pattern):
    iterLen = len(genome)-len(pattern)+1
    idxs = []
    for i in range(0, iterLen):
        if genome[i:i+len(pattern)] == pattern:
            idxs.append(str(i))
    return ' '.join(idxs)
