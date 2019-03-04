def MinimumSkew(Genome):
    prevSkew = 0
    skews = []
    i = 1
    skewToIdx = {}
    for n in Genome:
        if n == 'G':
            prevSkew += 1
        elif n == 'C':
            prevSkew -= 1
        skews.append(prevSkew)
        if prevSkew not in skewToIdx:
            skewToIdx[prevSkew] = [i]
        else:
            skewToIdx[prevSkew].append(i)
        i += 1
    return skewToIdx[min(skews)]
