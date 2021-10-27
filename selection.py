import numpy as np
from typing import List
from countcompares import CountCompares
from countswaps import CountSwaps

def _sort(A: List[int]) -> List[int]:
    n = len(A)
    for i in range(n-1):
        k = i
        for j in range(i+1, n-1):
            if A[j] < A[k]:
                k = j
        if i != k:
            A[i], A[k] = A[k], A[i]
    return A
