import pytest
import pandas as pd
from src.analyzer import DataAnalyzer

# Sample data for testing
TEST_DATA = {
    "date": [
        "2023-01-05", "2023-01-08", "2023-01-10", "2023-01-15", "2023-01-20",
        "2023-01-22", "2023-01-25", "2023-01-28", "2023-02-01", "2023-02-05"
    ],
    "category": [
        "groceries", "electronics", "groceries", "clothing", "electronics",
        "groceries", "clothing", "groceries", "electronics", "groceries"
    ],
    "amount": [
        124.56, 899.99, 75.25, 149.99, 450.00, 65.75, 89.99, 112.34, 1299.99, 94.55
    ],
    "customer_id": ["C001", "C002", "C003", "C001", "C004", "C002", "C003", "C001", "C004", "C002"]
}

@pytest.fixture
def sample_dataframe():
    return pd.DataFrame(TEST_DATA)

def test_summary_statistics(sample_dataframe):
    analyzer = DataAnalyzer(sample_dataframe)
    stats = analyzer.summary_statistics(category_col="category", value_col="amount")
    assert stats.loc[stats["category"] == "groceries", "mean"].iloc[0] == pytest.approx(94.89, 0.01)
    assert stats.loc[stats["category"] == "electronics", "median"].iloc[0] == pytest.approx(899.99, 0.01)

def test_time_series_analysis(sample_dataframe):
    analyzer = DataAnalyzer(sample_dataframe)
    time_series = analyzer.time_series_analysis(date_col="date", value_col="amount")
    assert time_series.loc[time_series["date"] == "2023-01-08", "amount"].iloc[0] == 899.99
    assert time_series["amount"].sum() == pytest.approx(3362.41, 0.01)

def test_top_spending_categories(sample_dataframe):
    analyzer = DataAnalyzer(sample_dataframe)
    top_categories = analyzer.top_spending_categories(category_col="category", value_col="amount", top_n=2)
    assert top_categories.iloc[0]["category"] == "electronics"
    assert top_categories.iloc[1]["category"] == "groceries"

def test_customer_segmentation(sample_dataframe):
    analyzer = DataAnalyzer(sample_dataframe)
    segmentation = analyzer.customer_segmentation(customer_id_col="customer_id", value_col="amount")
    assert segmentation.loc[segmentation["customer_id"] == "C001", "sum"].iloc[0] == pytest.approx(386.89, 0.01)
    assert segmentation.loc[segmentation["customer_id"] == "C002", "mean"].iloc[0] == pytest.approx(353.43, 0.01)