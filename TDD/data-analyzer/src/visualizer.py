import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Create a DataVisualizer class that takes analysis results and generates:
# - Bar charts for spending by category
# - Line charts for spending over time
# - Pie charts for spending distribution
# - Heatmaps for correlation between variables
# - Each method should support customization options (colors, titles, etc.)
# - Methods should return the figure and also have an option to save to file
class DataVisualizer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def bar_chart(self, x: str, y: str, title: str = "Bar Chart", xlabel: str = "", ylabel: str = "",
                  color: str = "blue"):
        if self.df.empty:
            raise ValueError("No data available")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=self.df, x=x, y=y, color=color, ax=ax)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig

    def line_chart(self, x: str, y: str, title: str = "Line Chart", xlabel: str = "", ylabel: str = "",
                   color: str = "blue"):
        if self.df.empty:
            raise ValueError("No data available")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=self.df, x=x, y=y, color=color, ax=ax)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig

    def pie_chart(self, values: str, title: str = "Pie Chart", labels: list = None, colors: list = None):
        if self.df.empty:
            raise ValueError("No data available")
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(self.df[values].value_counts(), labels=labels, colors=colors, autopct='%1.1f%%')
        ax.set_title(title)
        plt.tight_layout()
        return fig

    def heatmap(self, title: str = "Heatmap", cmap: str = "coolwarm"):
        if self.df.empty:
            raise ValueError("No data available")
        fig, ax = plt.subplots(figsize=(10, 8))
        corr = self.df.select_dtypes(include="number").corr()
        sns.heatmap(corr, annot=True, cmap=cmap, ax=ax)
        ax.set_title(title)
        plt.tight_layout()
        return fig