import pandas as pd 

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.
    """
    # 
    data = data[((data['passenger_count'] > 0) & (data['trip_distance'] > 0))]
    print(data.shape)

    # 
    # data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'])
    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime']).dt.date

    # 
    distinct_values = data['VendorID'].unique()
    print("Distinct VendorID: ", distinct_values)

    #
    data.rename(columns={
        'VendorID': 'vendor_id',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id'
        }, inplace=True)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

@test
def test_for_zero_passenger_count(output, *args) -> None:
    assert (output['passenger_count'] > 0).all(), 'You still have some trips with zero passengers'

@test
def test_for_zero_trip_distance(output, *args) -> None:
    assert (output['trip_distance'] > 0).all(), 'You still have some trips with zero distance'

@test
def test_for_vendor_id_column(output, *args) -> None:
    assert ('vendor_id' in output.columns), 'Cannot find column "vendor_id" in dataframe'