def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    dct = {}
    for i in samples:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] += 1
    n = len(samples)
    ans = []
    samples = list(set(samples))
    samples = sorted(samples)
    for i in samples:
        ans.append((i, dct[i] / n))
    return ans