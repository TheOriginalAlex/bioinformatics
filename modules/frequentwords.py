def FrequentWords(txt, k):
    patterns = {}
    iterLen = len(txt)-k+1
    for i in range(0, iterLen):
        pattern = txt[i:i+k]
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
    return counts[max(counts)]
