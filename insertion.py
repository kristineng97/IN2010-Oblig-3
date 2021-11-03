import numpy as np
from typing import List

from countswaps import CountSwaps

def _sort(A: CountSwaps) -> CountSwaps:
    n = len(A)
    for i in range(1, n):
        j = i
        while j>0 and A[j-1]>A[j]:
            A.swap(j-1, j)
            j -= 1
    return A
