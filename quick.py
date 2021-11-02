import numpy as np
from typing import List, Optional
import statistics
from countcompares import CountCompares
from countswaps import CountSwaps

def choosepivot(A: CountSwaps, low: int, high: int) -> int:
    n = len(A)
    return statistics.median([(A[low], low), (A[n//2],n//2), (A[high],high)])[1]

def partition(A: CountSwaps, low: int, high: int) -> int:
    n = len(A)
    p = choosepivot(A, low, high)
    A.swap(p, high)
    pivot = A[high]
    left = low
    right = high - 1
    while left <= right:
        while left <= right and A[left] <= pivot:
            left += 1
        while right >= left and A[right] >= pivot:
            right -= 1
        if left < right:
            A.swap(left, right)
    A.swap(left, high)
    return left

def _sort(A: CountSwaps, low: int = 0, high: Optional[int] = None) -> CountSwaps:
    if high is None:
        high = len(A) - 1

    if low >= high:
        return A
    p = partition(A, low, high)
    _sort(A, low, p-1)
    _sort(A, p+1, high)
    return A
