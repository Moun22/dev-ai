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
        plt.figure(figsize=(10, 6))
        sns.barplot(data=self.df, x=x, y=y, color=color)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt

    def line_chart(self, x: str, y: str, title: str = "Line Chart", xlabel: str = "", ylabel: str = "",
                   color: str = "blue"):
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=self.df, x=x, y=y, color=color)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt

    def pie_chart(self, values: str, title: str = "Pie Chart", labels: list = None, colors: list = None):
        plt.figure(figsize=(8, 8))
        plt.pie(self.df[values].value_counts(), labels=labels, colors=colors, autopct='%1.1f%%')
        plt.title(title)
        plt.tight_layout()
        return plt

    def heatmap(self, title: str = "Heatmap", cmap: str = "coolwarm"):
        plt.figure(figsize=(10, 8))
        sns.heatmap(self.df.corr(), annot=True, cmap=cmap)
        plt.title(title)
        plt.tight_layout()
        return plt
