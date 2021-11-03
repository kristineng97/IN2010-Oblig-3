import numpy as np
from typing import List

from countswaps import CountSwaps

def _sort(A: CountSwaps) -> CountSwaps:
    n = len(A)
    for i in range(n):
        k = i
        for j in range(i+1, n):
            if A[j] < A[k]:
                k = j
        if i != k:
            A.swap(i, k) 
    return A
