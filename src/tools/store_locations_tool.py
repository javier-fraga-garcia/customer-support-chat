import os
import pandas as pd


def get_store_locations(postal_codes: list[int]) -> list:
    """
    Retrieves the locations of stores near the specified postal codes.

    Args:
        postal_codes (list): A list of postal codes to search for nearby stores.

    Returns:
        list: A list of store locations found near the provided postal codes.
    """
    print(f"Function called for postal codes: {postal_codes}")
    df = pd.read_csv(f"{os.getcwd()}/src/data/stores.csv")
    filtered_df = df[df["postal_code"].isin(postal_codes)]
    return list(filtered_df["store_name"].values)
