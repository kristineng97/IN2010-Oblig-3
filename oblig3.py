import sys
from typing import List
import insertion

def read_data(filename: str) -> List[int]:
    """Reads a file with one integer on each line"""
    with open(filename, "r") as infile:
        elements = []
        for line in infile:
            elements.append(int(line))
    return elements

def main():
    A = read_array()
    print("hade")
    print(insertion.sort(A))




if __name__ == '__main__':
    main()
