from matplotlib import axes, pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from typing import List, Optional

from oblig3 import pseudo_logspace

def col(ax: axes, filename: str, col_suffix: str,
        algorithms: Optional[List[str]] = None):
    """Plot the data from column in a file to ax.

    Args:
        ax: Axis object to plot on.
        filename: Name of file to plot results from. Name of file to read from 
                  is then outputs/<filename>_results.csv.
        col_suffix: Suffix of column to plot. Can be `time`, `swaps`, `cmp`.
        algorithms: Algorithms to include. Default is None, which plots all
                    algorithms.

    Will save plot as `plots/<filename>_<col_suffix>.pdf`.
    """
    df = pd.read_csv(f"outputs/{filename}_results.csv", dtype=int)
    for column in df.columns:
        if col_suffix in column:
            algorithm_name = column.split("_")[0]
            if algorithms is None or algorithm_name in algorithms:
                ax.plot(df["n"], df[column], label=algorithm_name.capitalize())

def all_cols(filenames: List[str]):
    """Plots all data from the results in filenames.

    Makes a plot with three subplots for each filename, with one subplot for
    swaps, one for compares and one for time.

    Args:
        filenames: List of filenames.
    """
    for filename in filenames:
        fig, axs = plt.subplots(1, 3, figsize=(12, 5))
        for col_suffix, title, ax in zip(["swaps", "cmp", "time"],
                                         ["Swaps", "Compares", "Time, ms"], axs):
            col(ax, filename, col_suffix)
            ax.set_xlabel("n (log)")
            ax.set_ylabel(f"{title} (log)")
            ax.set_xscale("log")
            ax.set_yscale("log")

        plt.legend()
        plt.tight_layout()
        plt.savefig(f"plots/{filename}.pdf")
        plt.close()

def fit_to_time(filename: str, sqr_alg_name: str, log_alg_name: str):
    """Make a plot with actual runtime and a function fit to it.

    Args:
        filename: File to take actual runtime data from.
        sqr_alg_name: Name of algorithm that runs in O(n^2).
        log_alg_name: Name of algorithm that runs in O(n log(n)).
    """
    df = pd.read_csv(f"outputs/{filename}_results.csv", dtype=int)
    
    #fig, axs = plt.subplots(111, figsize=(8, 5))
    #ax = axs[0]

    # poly = Polynomial.fit(df["n"], df[f"{sqr_alg_name.lower()}_time"], 2)
    # plt.plot(df["n"], *poly.linspace(df["n"].iloc[-1]), label=f"Fit with {poly_expression}")

    n_log = lambda n, a, b, c: a + b*np.log(n) + c*n
    n_sqr = lambda n, a, b, c: a + b*n + c*n**2
    sqr_params, _ = curve_fit(n_sqr, df["n"], df[f"{sqr_alg_name}_time"])
    log_params, _ = curve_fit(n_log, df["n"], df[f"{log_alg_name}_time"])
    n_linspace = pseudo_logspace(df["n"].iloc[-1])
    
    sqr_expression = "$\\mathcal{O}(n^2)$"
    log_expression = "$\\mathcal{O}(n \\log(n))$"
    plt.plot(n_linspace, n_log(n_linspace, *log_params), linestyle="--",
             label=f"Fit with {log_expression}")
    plt.plot(n_linspace, n_sqr(n_linspace, *sqr_params), linestyle="--",
             label=f"Fit with {sqr_expression}")

    col(plt.gca(), filename, "time", [sqr_alg_name, log_alg_name])
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("n (log)")
    plt.ylabel("time, ms (log)")
    plt.legend()
    plt.savefig(f"plots/{filename}_fit.pdf")
    plt.close()







