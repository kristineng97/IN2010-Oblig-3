import sys
from typing import List, Union
import time
import insertion
import selection
import quick
import merge
from countcompares import CountCompares
from countswaps import CountSwaps

def read_data(filename: str, folder: str = "inputs") -> List[CountCompares]:
    """Reads a file with one integer on each line.
    """
    with open(f"{folder}/{filename}", "r") as infile:
        elements = CountSwaps()
        for line in infile:
            elements.append(CountCompares(int(line.strip())))
    return elements

def write_data(A: List[CountCompares], filename: str):
    """Takes a list A and writes its elements to a file with filename given as input.

    Filename is relative to outputs folder.
    """
    with open(f"outputs/{filename}", "w") as outfile:
        for element in A:
            outfile.write(str(element) + "\n")

def make_results_file(algorithms: List[str], filename: str):
    """Make a new file with headers for results on swaps, compares and time.

    Each algorithm gets four columns, first one for how many compares there are,
    then one for swaps, and lastly one for time usage.

    Filename is relative to outputs folder.
    """
    alg_headers = [f"{alg}_cmp, {alg}_swaps, {alg}_time" for alg in algorithms]
    
    with open(f"outputs/{filename}_results.csv", "w") as outfile:
        outfile.write(f"n, {', '.join(alg_headers)} \n")

def append_to_results_file(n: int, results: List[Union[float, int]],
                           filename: str):
    """Appends a line to an already existing results file"""
    with open(f"outputs/{filename}_results.csv", "a") as outfile:
        outfile.write(f"{n}, {', '.join([str(res) for res in results])}\n")

def main():
    algorithms = [insertion, selection, merge, quick]
    for filename in ["random_10", "random_100", "random_1000"]:
        make_results_file([alg.__name__ for alg in algorithms], filename)

        n = int(filename.split("_")[-1])

        for k in range(1, n + 1):
            results = []
            for algorithm in algorithms:
                A = read_data(filename)
                start_time = time.time_ns()
                sorted_A = algorithm._sort(CountSwaps(A[:k]))
                swaps, compares = 0, 0 # Dummy variables to be found later

                end_time = (time.time_ns() - start_time) / 1000

                # Find swaps and compares
                for elem in sorted_A:
                    compares += elem.compares
                print(algorithm.__name__)
                swaps = sorted_A.swaps

                
                # print(sorted_A)
                results.extend([compares, swaps, end_time])
                
                if k == n:
                    write_data(sorted_A, f"{filename}_{algorithm.__name__}.out")
                print(f"{filename}: {k}/{n}", end="\r")
            append_to_results_file(k, results, filename)
        print()


if __name__ == '__main__':
    main()
