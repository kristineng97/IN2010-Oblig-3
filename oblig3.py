import sys
import numpy as np
from typing import List, Any

import time
import insertion
import selection
import quick
import merge
from countcompares import CountCompares
from countswaps import CountSwaps
import plot
from file_handling import read_data, write_data, make_results_file, \
                          append_to_results_file

def pseudo_logspace(n_max: int, max_num_points: int = 100) -> np.ndarray:
    """Make something like a logspace, just without duplicate values.

    A logspace has the nice property that it looks good when plotted in log, and
    in our case, where the high values for n are the most expensive to compute,
    it also saves us some computation time.

    It works by finding how high the first number that isn't repeated with a 
    logspace is (this is the number `l`), and then making a linspace up to that 
    point, a logspace from that point, and concatenating them.

    Args:
        n_max: The highest n-value in the data.
        max_num_points: How many points to make. Won't make higher than n_max, 
                        and default is 100.
    """
    num_points = min(max_num_points, n_max)

    l = 1
    ratio = (n_max/l)**(1/(l-num_points))
    while np.abs(l*(ratio - 1)) < 1 and l < num_points - 1:
        l += 1
        ratio = (n_max/l)**(1/(l-num_points))
    l += 1
    
    linspace = np.linspace(1, l, l, dtype=int)
    logspace = np.logspace(np.log10(l+2), np.log10(n_max), num_points - l,
               dtype=int)

    return np.append(linspace, logspace)

def compute_results(algorithms: List, filenames: List[str]):
    """Write results to file, after sorting the files with different algorithms.

    Goes through every file, and then for every k from 1 to the length of the 
    list, sort the first k elements with every algorithm. After each of these
    iterations, store the results in a file. Also, store the final resulting 
    file with the sorted list to another file.

    Args:
        algorithms: List of modules, each with a _sort function.
        filenames: List of filenames.
    """
    for filename in filenames:
        make_results_file([alg.__name__ for alg in algorithms], filename)

        n_max = int(filename.split("_")[-1])

        for n in pseudo_logspace(n_max):
            results = []
            for algorithm in algorithms:
                A = read_data(filename)
                start_time = time.time_ns()
                sorted_A = algorithm._sort(CountSwaps(A[:n]))
                end_time = int((time.time_ns() - start_time) / 1000)

                compares = 0
                for elem in sorted_A:
                    compares += elem.compares
                
                results.extend([compares, sorted_A.swaps, end_time])
                
                # Write final sorted list to file
                if n == n_max:
                    write_data(sorted_A, f"{filename}_{algorithm.__name__}.out")
                
                print(f"{filename}: {n}/{n_max}", end="\r")
            append_to_results_file(n, results, filename)
        print()

def main():
    small_files = ["random_10", "random_100", "random_1000"]
    nearly_sorted_files = ["nearly_sorted_10", "nearly_sorted_100",
                           "nearly_sorted_1000"]
    big_files = ["random_10000", "random_100000"]
    slow_algs = [insertion, selection]
    fast_algs = [merge, quick]

    if "-c" in sys.argv or "--compute" in sys.argv:
        compute_results(slow_algs + fast_algs, small_files)
        compute_results(fast_algs, big_files)
        compute_results(slow_algs + fast_algs, nearly_sorted_files)

    if "-p" in sys.argv or "--plot" in sys.argv:
        plot.all_cols(small_files + nearly_sorted_files + big_files)
        plot.fit_to_time("random_1000", "selection", "merge")

if __name__ == '__main__':
    main()
