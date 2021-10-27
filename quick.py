import numpy as np
from typing import List
import statistics
from countcompares import CountCompares
from countswaps import CountSwaps



def choosepivot(A: List[int],low: int, high: int) -> int:
    n = len(A)
    return statistics.median([(A[low], low), (A[n//2],n//2), (A[high],high)])[1]

def partition(A: List[int],low: int, high: int) -> int:
    n = len(A)
    p = choosepivot(A, low, high)
    A[p], A[high] = A[high], A[p]
    pivot = A[high]
    left = low
    right = high - 1
    while left <= right:
        while left <= right and A[left] <= pivot:
            left += 1
        while right >= left and A[right] >= pivot:
            right -= 1
        if left < right:
            A[left], A[right] = A[right], A[left]
    A[left], A[high] = A[high], A[left]
    return left


def _sort(A: List[int],low: int, high: int) -> List[int]:
    if low >= high:
        return A
    p = partition(A, low, high)
    _sort(A, low, p-1)
    _sort(A, p+1, high)
    return A
