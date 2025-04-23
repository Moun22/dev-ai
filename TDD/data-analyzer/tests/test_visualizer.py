import pytest
import pandas as pd
from src.visualizer import DataVisualizer
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Sample data for testing
TEST_DATA = {
    "date": ["2023-01-05", "2023-01-08", "2023-01-10"],
    "category": ["groceries", "electronics", "groceries"],
    "amount": [124.56, 899.99, 75.25],
}


@pytest.fixture
def sample_dataframe():
    return pd.DataFrame(TEST_DATA)


@pytest.fixture
def empty_dataframe():
    return pd.DataFrame()


def test_bar_chart_returns_figure(sample_dataframe):
    visualizer = DataVisualizer(sample_dataframe)
    fig = visualizer.bar_chart(x="category", y="amount", title="Test Bar Chart")
    assert isinstance(fig, Figure)


def test_line_chart_returns_figure(sample_dataframe):
    visualizer = DataVisualizer(sample_dataframe)
    fig = visualizer.line_chart(x="date", y="amount", title="Test Line Chart")
    assert isinstance(fig, Figure)


def test_pie_chart_returns_figure(sample_dataframe):
    visualizer = DataVisualizer(sample_dataframe)
    fig = visualizer.pie_chart(values="category", title="Test Pie Chart", labels=sample_dataframe["category"].unique())
    assert isinstance(fig, Figure)


def test_heatmap_returns_figure(sample_dataframe):
    visualizer = DataVisualizer(sample_dataframe)
    fig = visualizer.heatmap(title="Test Heatmap")
    assert isinstance(fig, Figure)


def test_methods_handle_empty_data(empty_dataframe):
    visualizer = DataVisualizer(empty_dataframe)
    with pytest.raises(ValueError, match="No data available"):
        visualizer.bar_chart(x="category", y="amount")
    with pytest.raises(ValueError, match="No data available"):
        visualizer.line_chart(x="date", y="amount")
    with pytest.raises(ValueError, match="No data available"):
        visualizer.pie_chart(values="category")
    with pytest.raises(ValueError, match="No data available"):
        visualizer.heatmap()


def test_saving_to_file(sample_dataframe, tmp_path):
    visualizer = DataVisualizer(sample_dataframe)
    file_path = tmp_path / "test_chart.png"
    fig = visualizer.bar_chart(x="category", y="amount", title="Test Bar Chart")
    fig.savefig(file_path)
    assert file_path.exists()
