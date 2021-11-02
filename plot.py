import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from oblig3 import read_data

def plot_col(ax: matplotlib.axes, filename: str, col_suffix: str):
    """

    Args:
        ax: Axis object to plot on.
        filename: Name of file to plot results from. Name of file to read from 
                  is then outputs/<filename>_results.csv.
        col_suffix: Suffix of column to plot. Can be `time`, `swaps`, `cmp`.

    Will save plot as `plots/<filename>_<col_suffix>.pdf`.
    """

    df = pd.read_csv(f"outputs/{filename}_results.csv", dtype=int)
    for column in df.columns:
        if col_suffix in column:
            ax.plot(df["n"], df[column], label=column.split("_")[0])

def main():
    for filename in ["random_100", "random_1000"]:
        fig, axs = plt.subplots(1, 3, figsize=(12, 5))
        for col_suffix, title, ax in zip(["swaps", "cmp", "time"],
                                         ["Swaps", "Compares", "Time"], axs):
            plot_col(ax, filename, col_suffix)
            ax.set_xlabel("n (log)")
            ax.set_ylabel(f"{title} (log)")
            ax.set_xscale("log")
            ax.set_yscale("log")

        plt.legend()
        plt.tight_layout()
        plt.savefig(f"plots/{filename}.pdf")

if __name__ == "__main__":
    main()
