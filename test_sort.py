import pytest
from typing import List

import insertion
import selection
import quick
import merge
import oblig3

def test_sort():
    for filename in ["random_100", "random_1000"]:
        for algorithm in [insertion, selection, quick, merge]:
            A = oblig3.read_data(filename)
            expected = A.copy()
            expected.sort()
            computed = algorithm._sort(A)
            assert computed == expected, "The list was not sorted correctly" + \
                                        f" with {algorithm.__name__}._sort"
