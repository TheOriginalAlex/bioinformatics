def HammingDistance(p, q):
    result = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            result += 1
    return result
