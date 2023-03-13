from itertools import accumulate, combinations

def positions(c):
    """Return positions of amino acids according to configuration c"""
    p = list(accumulate(c))
    p.insert(0,0)
    return p

def fold(c, f):
    """Return configuration c folded by folding vector f"""
    return [a*b for a, b in zip(c,f)]

def score(a, c):
    """Return a score for amino acids sequence s in configuration c"""
    p = positions(c)
    # Choose only coordinates of hydrophobic amino acids
    p = [pos for acid, pos in zip(a,p) if acid]
    # Compute the total distance among all pairs of positions
    total = 0
    for p1, p2 in combinations(p, 2):
        total += abs(p1-p2)
    return total

