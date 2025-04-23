# Create a DataLoader class that:
# - Loads a CSV file into a pandas DataFrame
# - Validates that required columns are present
# - Parses date columns and converts data types
# - Removes rows with missing or invalid data
# - Provides methods to filter data by date range and category
class DataLoader:
    def __init__(self, file_path: str, date_columns: list, required_columns: list):
        self.file_path = file_path
        self.date_columns = date_columns
        self.required_columns = required_columns
        self.data = None

    def load_data(self):
        import pandas as pd

        # Load the CSV file into a DataFrame
        self.data = pd.read_csv(self.file_path)

        # Validate that required columns are present
        for column in self.required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

        # Parse date columns and convert data types
        for column in self.date_columns:
            self.data[column] = pd.to_datetime(self.data[column], errors='coerce')

        # Remove rows with missing or invalid data
        self.data.dropna(inplace=True)

    def filter_by_date_range(self, start_date: str, end_date: str):
        mask = (self.data[self.date_columns[0]] >= start_date) & (self.data[self.date_columns[0]] <= end_date)
        return self.data.loc[mask]

    def filter_by_category(self, category_column: str, category_value: str):
        return self.data[self.data[category_column] == category_value]