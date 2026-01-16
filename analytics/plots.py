import matplotlib.pyplot as plt
import pandas as pd


def plot_average_age(avg_age: pd.Series) -> None:
    avg_age.plot(kind="bar")
    plt.title("Average Age by Country")
    plt.ylabel("Age")
    plt.tight_layout()

    plt.savefig("average_age_by_country.png")
    plt.close()
