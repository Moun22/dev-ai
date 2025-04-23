import pandas as pd
from typing import Optional


# Create a DataAnalyzer class that takes a DataFrame and provides:
# - Summary statistics (mean, median, std dev by category)
# - Time series analysis (spending trends over time)
# - Spending distribution analysis
# - Top spending categories
# - Customer segmentation by spending patterns
class DataAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def summary_statistics(self, category_col: str, value_col: str) -> pd.DataFrame:
        """
        Calculate summary statistics (mean, median, std dev) by category.
        """
        return self.df.groupby(category_col)[value_col].agg(['mean', 'median', 'std']).reset_index()

    def time_series_analysis(self, date_col: str, value_col: str) -> pd.DataFrame:
        """
        Analyze spending trends over time.
        """
        self.df[date_col] = pd.to_datetime(self.df[date_col])
        return self.df.groupby(date_col)[value_col].sum().reset_index()

    def spending_distribution(self, value_col: str) -> pd.Series:
        """
        Analyze spending distribution.
        """
        return self.df[value_col].describe()

    def top_spending_categories(self, category_col: str, value_col: str, top_n: int = 5) -> pd.DataFrame:
        """
        Get the top N spending categories.
        """
        return self.df.groupby(category_col)[value_col].sum().nlargest(top_n).reset_index()

    def customer_segmentation(self, customer_id_col: str, value_col: str) -> pd.DataFrame:
        """
        Segment customers by spending patterns.
        """
        return self.df.groupby(customer_id_col)[value_col].agg(['mean', 'sum']).reset_index()
