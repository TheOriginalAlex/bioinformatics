complement_map = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

def ReverseComplement(pattern):
    complement = []
    for char in pattern:
        complement.append(complement_map[char])
    return ''.join(complement[::-1])
