import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    df = None
    months = [10, 11, 12]

    for mnth in months:
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{mnth}.csv.gz'
        partial_df = pd.read_csv(url, sep=',', compression='gzip')

        if df is None:
            df = partial_df
        else:
            df = df.append(partial_df, ignore_index=True)
        
    print(df.shape)
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
