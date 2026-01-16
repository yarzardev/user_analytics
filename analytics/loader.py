import pandas as pd
import logging


def load_users(csv_path: str) -> pd.DataFrame:
    """
    Load users from a CSV file.
    """
    try:
        df = pd.read_csv(csv_path)
        return df
    except FileNotFoundError as e:
        logging.error(f"CSV file not found: {csv_path}")
        raise e
