import argparse
import pandas as pd
from src.data_loader import DataLoader
from src.analyzer import DataAnalyzer
from src.visualizer import DataVisualizer

# Create a command-line interface that:
# - Takes a CSV file path as input
# - Allows selecting analysis type (summary, time-series, category, etc.)
# - Allows selecting visualization type
# - Supports saving results to files
# - Has a help menu explaining functionality

def main():
    # Set up CLI argument parsing
    parser = argparse.ArgumentParser(description="📊 Data Analysis and Visualization Tool")
    parser.add_argument("csv", help="Path to the CSV file")
    parser.add_argument(
        "--analysis",
        choices=["summary", "time-series", "top-categories", "segment"],
        required=True,
        help="Type of analysis to perform"
    )
    parser.add_argument(
        "--plot",
        choices=["bar", "line", "pie", "heatmap"],
        help="Optional visualization to generate"
    )
    parser.add_argument(
        "--output",
        help="Path to save output visualization (e.g., results/chart.png)"
    )

    args = parser.parse_args()

    # Load and clean the data
    loader = DataLoader(
        file_path=args.csv,
        date_columns=["date"],
        required_columns=["date", "category", "amount", "customer_id"]
    )
    loader.load_data()
    df = loader.data

    # Run selected analysis
    analyzer = DataAnalyzer(df)

    if args.analysis == "summary":
        result = analyzer.summary_statistics("category", "amount")
    elif args.analysis == "time-series":
        result = analyzer.time_series_analysis("date", "amount")
    elif args.analysis == "top-categories":
        result = analyzer.top_spending_categories("category", "amount", top_n=5)
    elif args.analysis == "segment":
        result = analyzer.customer_segmentation("customer_id", "amount")
    else:
        print("⚠️ Unsupported analysis type.")
        return

    # Display analysis result
    print("\n=== Analysis Result ===")
    print(result)

    # Generate visualization if requested
    if args.plot:
        visualizer = DataVisualizer(df)

        if args.plot == "bar":
            fig = visualizer.bar_chart(x="category", y="amount", title="Bar Chart")
        elif args.plot == "line":
            fig = visualizer.line_chart(x="date", y="amount", title="Line Chart")
        elif args.plot == "pie":
            fig = visualizer.pie_chart(values="category", title="Spending by Category", labels=df["category"].unique())
        elif args.plot == "heatmap":
            fig = visualizer.heatmap(title="Correlation Heatmap")
        else:
            print("⚠️ Unsupported plot type.")
            return

        if args.output:
            import os
            os.makedirs(os.path.dirname(args.output), exist_ok=True)
            fig.savefig(args.output)
            print(f"\n✅ Chart saved to: {args.output}")
        else:
            fig.show()


if __name__ == "__main__":
    main()