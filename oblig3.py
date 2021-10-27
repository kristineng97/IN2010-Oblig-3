import sys
from typing import List
import insertion
import selection
import quick
import merge

def read_data(filename: str) -> List[int]:
    """Reads a file with one integer on each line"""
    with open(filename, "r") as infile:
        elements = []
        for line in infile:
            elements.append(int(line.strip()))
    return elements

def read_array() -> List[int]:
    """Reads an array where each int element is on its own line."""
    return [int(element) for element in sys.stdin.readlines()]

def main():
    A = read_array()
    n = len(A)
    print("Insertion")
    print(insertion.sort(A))
    print("Selection")
    print(selection.sort(A))
    print("Quick")
    print(quick._sort(A, 0, n-1))
    print("Merge")
    print(merge._sort(A))





if __name__ == '__main__':
    main()
