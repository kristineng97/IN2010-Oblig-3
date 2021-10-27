import sys
from typing import List
import time
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

def write_elements_to_file(A: List[int], filename: str):
    """Takes a list A and writes its elements to a file with filename given as input"""
    outfile = open(filename, "w")
    for element in A:
        outfile.write(f"{element}\n")
    outfile.close()

def make_results_file(algorithms: List[str], inputfile: str):
    outfile = open(f"{inputfile}_results.csv", "w")
    for a in algorithms:
        outfile.write(f"n, {a}_cmp, {a}_swaps, {a}_time,
        {a+1}_cmp, {a+1}_swaps, {a+1}_time,
        {a+2}_cmp, {a+2}_swaps, {a+2}_time,
        {a+3}_cmp, {a+3}_swaps, {a+3}_time")

        outfile.write()



def main():
    A = read_array()
    n = len(A)
    write_to_file(insertion._sort(A), "random_10_insertion.out")

    print("Selection")
    t = time.time_ns()
    print(selection._sort(A))
    timeus = (time.time_ns() - t) / 1000
    print("Selection time:", timeus)
    
    print("Quick")
    print(quick._sort(A, 0, n-1))
    print("Merge")
    print(merge._sort(A))





if __name__ == '__main__':
    main()
