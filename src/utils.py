import numpy as np

from src.constants import TOLERANCE


def unit(a: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(a)
    if norm < TOLERANCE:
        raise ValueError("Trying to get a unit vector of a null vector")
    return a / norm
