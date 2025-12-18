import numpy as np

def is_silent(audio, threshold=0.01):
    return np.max(np.abs(audio)) < threshold
