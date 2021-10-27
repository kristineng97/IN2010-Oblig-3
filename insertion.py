import numpy as np
from typing import List
from countcompares import CountCompares
from countswaps import CountSwaps

def _sort(A: List[int]) -> List[int]:
    n = len(A)
    for i in range(1, n):
        j = i
        while j>0 and A[j-1]>A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            j -= 1
    return A
