import pandas as pd

def datas_load_csv(path: str):
    """Load a CSV file using pandas and return a DataFrame.

    Parameters
    ----------
    path: str
        Path to the CSV file.
    """
    return pd.read_csv(path)

if __name__ == "__main__":
    # Example usage (replace with your own file)
    df = datas_load_csv("data/example.csv")
    print(df.head())
