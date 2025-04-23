# 🧠 GitHub Copilot for Python Development

## Project: Data Analysis Tool with Pandas and Visualization

### 🧪 Project Setup

#### Project Structure
```bash
data-analyzer/
├── data/
│   └── sample_data.csv
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── analyzer.py
│   └── visualizer.py
├── tests/
│   ├── __init__.py
│   ├── test_data_loader.py
│   ├── test_analyzer.py
│   └── test_visualizer.py
└── main.py
```

### ✅ Step 1: DataLoader Class (with Copilot)

Used Copilot to implement:

- load_data(): loads CSV, validates required columns, cleans types
- filter_by_date(): returns data within a date range
- filter_by_category(): filters by category values

Prompts used:
```python
# Create a DataLoader class that:
# - Loads a CSV file into a pandas DataFrame
# - Validates that required columns are present
# - Parses date columns and converts data types
# - Removes rows with missing or invalid data
# - Provides methods to filter data by date range and category
```
### ✅ Step 2: DataAnalyzer Class (with Copilot)

Methods implemented:
- summary_statistics(): returns mean, median, std per category
- time_series_analysis(): total spending grouped by date
- spending_distribution(): amount distribution stats
- top_spending_categories(n): top N categories by total amount
- customer_segmentation(): customer spend segmentation using quantiles

Prompts used:
```python
# Return mean, median, and std deviation of amount grouped by category
# Return total spending by date as a time series
# Segment customers based on total spending

