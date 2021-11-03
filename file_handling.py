from typing import List

from countcompares import CountCompares

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
    alg_headers = [f"{alg}_cmp,{alg}_swaps,{alg}_time" for alg in algorithms]
    
    with open(f"outputs/{filename}_results.csv", "w") as outfile:
        outfile.write(f"n,{','.join(alg_headers)} \n")

def append_to_results_file(n: int, results: List[int],
                           filename: str):
    """Appends a line to an already existing results file"""
    with open(f"outputs/{filename}_results.csv", "a") as outfile:
        outfile.write(f"{n}, {', '.join([str(res) for res in results])}\n")