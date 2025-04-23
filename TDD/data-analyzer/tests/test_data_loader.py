import pytest
import pandas as pd
from src.data_loader import DataLoader

# Sample data for testing
TEST_CSV = "test_data.csv"
TEST_DATA = """date,category,amount,customer_id
2023-01-05,groceries,124.56,C001
2023-01-08,electronics,899.99,C002
2023-01-10,groceries,75.25,C003
"""


@pytest.fixture
def create_test_csv(tmp_path):
    # Create a temporary CSV file for testing
    test_file = tmp_path / TEST_CSV
    test_file.write_text(TEST_DATA)
    return str(test_file)


def test_load_data_success(create_test_csv):
    loader = DataLoader(file_path=create_test_csv, date_columns=["date"],
                        required_columns=["date", "category", "amount", "customer_id"])
    loader.load_data()
    assert not loader.data.empty
    assert list(loader.data.columns) == ["date", "category", "amount", "customer_id"]


def test_missing_required_columns(create_test_csv):
    loader = DataLoader(file_path=create_test_csv, date_columns=["date"],
                        required_columns=["date", "category", "missing_column"])
    with pytest.raises(ValueError, match="Missing required column: missing_column"):
        loader.load_data()


def test_filter_by_date_range(create_test_csv):
    loader = DataLoader(file_path=create_test_csv, date_columns=["date"],
                        required_columns=["date", "category", "amount", "customer_id"])
    loader.load_data()
    filtered_data = loader.filter_by_date_range("2023-01-06", "2023-01-09")
    assert len(filtered_data) == 1
    assert filtered_data.iloc[0]["category"] == "electronics"


def test_filter_by_category(create_test_csv):
    loader = DataLoader(file_path=create_test_csv, date_columns=["date"],
                        required_columns=["date", "category", "amount", "customer_id"])
    loader.load_data()
    filtered_data = loader.filter_by_category("category", "groceries")
    assert len(filtered_data) == 2
    assert all(filtered_data["category"] == "groceries")
