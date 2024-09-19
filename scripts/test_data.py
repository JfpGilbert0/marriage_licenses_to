import pandas as pd
import pytest

# Sample test dataset creation
@pytest.fixture
def sample_data():
    # Simulated data to match the expected structure
    data = "data\analysis_data\cleaned_marriage_data.csv"
    df = pd.DataFrame(data)
    df['TIME_PERIOD'] = pd.to_datetime(df['TIME_PERIOD'], format='%Y-%m')
    return df

# Test for correct data types
def test_data_types(sample_data):
    assert sample_data['_id'].dtype == 'int64', "Incorrect data type for _id"
    assert sample_data['CIVIC_CENTRE'].dtype == 'object', "Incorrect data type for CIVIC_CENTRE"
    assert sample_data['MARRIAGE_LICENSES'].dtype == 'int64', "Incorrect data type for MARRIAGE_LICENSES"
    assert sample_data['TIME_PERIOD'].dtype == 'datetime64[ns]', "Incorrect data type for TIME_PERIOD"

# Test that marriage licenses are non-negative
def test_marriage_licenses_non_negative(sample_data):
    assert (sample_data['MARRIAGE_LICENSES'] >= 0).all(), "MARRIAGE_LICENSES should be non-negative."

# Test for valid time periods format (should be datetime)
def test_time_period_format(sample_data):
    assert pd.api.types.is_datetime64_any_dtype(sample_data['TIME_PERIOD']), "TIME_PERIOD should be datetime format."

# Test for non-null fields
def test_non_null_values(sample_data):
    assert sample_data['_id'].notna().all(), "_id should not contain null values."
    assert sample_data['CIVIC_CENTRE'].notna().all(), "CIVIC_CENTRE should not contain null values."
    assert sample_data['MARRIAGE_LICENSES'].notna().all(), "MARRIAGE_LICENSES should not contain null values."
    assert sample_data['TIME_PERIOD'].notna().all(), "TIME_PERIOD should not contain null values."

# Test for duplicates
def test_no_duplicates(sample_data):
    assert not sample_data.duplicated().any(), "Dataset should not contain duplicate rows."

# Test for valid CIVIC_CENTRE values
def test_valid_civic_centre(sample_data):
    valid_civic_centres = ['ET', 'NY', 'SC', 'TO', 'YK']
    assert sample_data['CIVIC_CENTRE'].isin(valid_civic_centres).all(), "Invalid CIVIC_CENTRE value found."

# Test for reasonable date range (example: dates should be from 2010 onwards)
def test_reasonable_date_range(sample_data):
    start_date = pd.Timestamp('2010-01-01')
    assert (sample_data['TIME_PERIOD'] >= start_date).all(), "TIME_PERIOD should be from 2010 onwards."

