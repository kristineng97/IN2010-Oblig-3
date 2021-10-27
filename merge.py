import numpy as np
from typing import List
from countcompares import CountCompares
from countswaps import CountSwaps

def merge_(A1: List[int], A2: List[int], A: List[int]) -> List[int]:
    i = 0
    j = 0

    while i < len(A1) and j < len(A2):
        if A1[i] < A2[j]:
            A[i+j] = A1[i]
            i += 1
        else:
            A[i+j] = A2[j]
            j += 1

    while i < len(A1):
        A[i+j] = A1[i]
        i += 1

    while j < len(A2):
        A[i+j] = A2[j]
        j += 1
    return A

def _sort(A: List[int]) -> List[int]:
    if len(A) <= 1:
        return A

    i = len(A)//2
    A1 = _sort(A[:i-1])
    A2 = _sort(A[i:len(A)-1])
    return merge_(A1,A2,A)
