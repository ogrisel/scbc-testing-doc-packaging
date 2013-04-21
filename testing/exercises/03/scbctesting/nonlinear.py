import numpy as np

def interaction(a, b):
    diff = np.abs(b - a)
    return np.where(diff < 1, diff, diff ** 2)


def positive_interaction(a, b):
    if a < 0 or b < 0:
        raise ValueError(
            "Both a and b must be positive: got %r and %r"% (a, b))
    return interaction(a, b)