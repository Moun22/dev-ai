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
# Create a DataAnalyzer class that takes a DataFrame and provides:
# - Summary statistics (mean, median, std dev by category)
# - Time series analysis (spending trends over time)
# - Spending distribution analysis
# - Top spending categories
# - Customer segmentation by spending patterns
```
### ✅ Step 3: DataVisualizer Class (with Copilot)

Methods implemented:
- bar_chart(): bar chart of total spending per category
- line_chart(): spending trend by date
- pie_chart(): percentage of total by category
- heatmap(): correlations between numeric fields

Prompts used:
```python
# Create a DataVisualizer class that takes analysis results and generates:
# - Bar charts for spending by category
# - Line charts for spending over time
# - Pie charts for spending distribution
# - Heatmaps for correlation between variables
# - Each method should support customization options (colors, titles, etc.)
# - Methods should return the figure and also have an option to save to file
```
### ✅ Step 4: Testing (with Copilot)

Tests written for:
- ✅ DataLoader:
    - load_data() returns correct structure
    - raises error if columns are missing
    - date/category filters return expected rows
- ✅ DataAnalyzer:
    - summary stats and top categories are correct
- ✅ DataVisualizer:
    - plotting methods return matplotlib figures

Prompts used:
```python
# Test that data is loaded correctly
# Test filtering by date range returns correct subset
# Test that saving to file works without error
```
### ✅ Step 5: CLI App in main.py (with Copilot)

Features:
- Uses argparse to parse CLI input
- Loads and validates data
- Performs selectable analysis:
  - summary, time-series, top-categories, segmentation
- Supports visualization (bar, line, pie, heatmap)
- Optionally saves chart to file

Prompts used:
```python
# Create a command-line interface that:
# - Takes a CSV file path as input
# - Allows selecting analysis type (summary, time-series, category, etc.)
# - Allows selecting visualization type
# - Supports saving results to files
# - Has a help menu explaining functionality
```

## 🧪 Example CLI Commands

```bash
# Run summary statistics
python main.py data/sample_data.csv --analysis summary

# Run time series analysis
python main.py data/sample_data.csv --analysis time-series

# Get top spending categories with a bar chart
python main.py data/sample_data.csv --analysis top-categories --plot bar

# Generate and save a pie chart to a file
python main.py data/sample_data.csv --analysis top-categories --plot pie --output results/pie.png

# Run customer segmentation analysis
python main.py data/sample_data.csv --analysis segment

# Generate and save a heatmap of correlations
python main.py data/sample_data.csv --analysis summary --plot heatmap --output results/heatmap.png



