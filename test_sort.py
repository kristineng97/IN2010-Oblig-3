import insertion
from typing import List
import pytest
import oblig3



def test_sort():
    filenames = ["random_100", "random_1000"]
    algorithms = ["insertion"]
    for filename in filenames:
        for algorithm in algorithms:
            A = oblig3.read_data(f"output/{filename}_{algorithm}.out")
