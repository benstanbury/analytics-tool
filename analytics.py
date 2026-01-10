#!/usr/bin/env python3
"""
Analytics Tool
--------------
A flexible analytics tool that performs statistical analysis and visualization
based on YAML configuration files.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml
import sys
import json
from pathlib import Path


class AnalyticsTool:
    """Main analytics tool class for processing data and generating outputs."""

    def __init__(self, config_path, data_path):
        """
        Initialize the analytics tool.

        Args:
            config_path: Path to YAML configuration file
            data_path: Path to CSV data file
        """
        self.config = self._load_config(config_path)
        self.data = self._load_data(data_path)
        self.results = {}

    def _load_config(self, config_path):
        """Load YAML configuration file."""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def _load_data(self, data_path):
        """Load CSV data file."""
        return pd.read_csv(data_path)

    def run_statistics(self):
        """Execute statistical analyses specified in config."""
        if 'statistics' not in self.config:
            return

        stats_config = self.config['statistics']
        variables = stats_config.get('variables', list(self.data.columns))
        operations = stats_config.get('operations', ['mean'])

        print("\n" + "="*50)
        print("STATISTICAL ANALYSIS")
        print("="*50)

        for var in variables:
            if var not in self.data.columns:
                print(f"Warning: Variable '{var}' not found in data")
                continue

            print(f"\n{var}:")
            print("-" * 30)

            for op in operations:
                result = self._compute_statistic(var, op)
                if result is not None:
                    self.results[f"{var}_{op}"] = result
                    print(f"  {op:15s}: {result:.4f}")

        # Save statistics to files
        self._save_statistics()

    def _compute_statistic(self, variable, operation):
        """Compute a single statistic for a variable."""
        data_series = self.data[variable]

        operations_map = {
            'mean': data_series.mean,
            'sum': data_series.sum,
            'median': data_series.median,
            'std': data_series.std,
            'var': data_series.var,
            'min': data_series.min,
            'max': data_series.max,
            'count': data_series.count,
        }

        if operation in operations_map:
            return operations_map[operation]()
        else:
            print(f"  Warning: Unknown operation '{operation}'")
            return None

    def _save_statistics(self):
        """Save statistics to text and JSON files in output directory."""
        output_dir = Path(self.config.get('output_dir', 'output'))
        output_dir.mkdir(exist_ok=True)

        stats_config = self.config.get('statistics', {})
        variables = stats_config.get('variables', list(self.data.columns))
        operations = stats_config.get('operations', ['mean'])

        # Prepare structured data for JSON
        stats_data = {}
        for var in variables:
            if var in self.data.columns:
                stats_data[var] = {}
                for op in operations:
                    key = f"{var}_{op}"
                    if key in self.results:
                        stats_data[var][op] = float(self.results[key])

        # Save to JSON file
        json_path = output_dir / 'statistics.json'
        with open(json_path, 'w') as f:
            json.dump(stats_data, f, indent=2)

        # Save to text file
        txt_path = output_dir / 'statistics.txt'
        with open(txt_path, 'w') as f:
            f.write("="*50 + "\n")
            f.write("STATISTICAL ANALYSIS\n")
            f.write("="*50 + "\n\n")

            for var in variables:
                if var in stats_data:
                    f.write(f"{var}:\n")
                    f.write("-" * 30 + "\n")
                    for op in operations:
                        if op in stats_data[var]:
                            value = stats_data[var][op]
                            f.write(f"  {op:15s}: {value:.4f}\n")
                    f.write("\n")

    def generate_charts(self):
        """Generate charts specified in config."""
        if 'charts' not in self.config:
            return

        print("\n" + "="*50)
        print("GENERATING CHARTS")
        print("="*50)

        output_dir = Path(self.config.get('output_dir', 'output'))
        output_dir.mkdir(exist_ok=True)

        for i, chart_config in enumerate(self.config['charts']):
            self._generate_chart(chart_config, output_dir, i)

    def _generate_chart(self, chart_config, output_dir, index):
        """Generate a single chart."""
        chart_type = chart_config.get('type')
        variables = chart_config.get('variables', [])
        title = chart_config.get('title', f'Chart {index+1}')

        if not variables:
            print(f"Warning: No variables specified for chart '{title}'")
            return

        print(f"\nGenerating: {title} ({chart_type})")

        plt.figure(figsize=(10, 6))

        if chart_type == 'bar':
            self._create_bar_chart(variables, title)
        elif chart_type == 'line':
            self._create_line_chart(variables, title)
        elif chart_type == 'histogram':
            self._create_histogram(variables, title)
        elif chart_type == 'box':
            self._create_box_plot(variables, title)
        elif chart_type == 'scatter':
            self._create_scatter_plot(variables, title)
        elif chart_type == 'heatmap':
            self._create_heatmap(variables, title)
        else:
            print(f"  Warning: Unknown chart type '{chart_type}'")
            plt.close()
            return

        # Save the chart
        filename = f"chart_{index+1}_{chart_type}.png"
        filepath = output_dir / filename
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"  Saved: {filepath}")

    def _create_bar_chart(self, variables, title):
        """Create a bar chart."""
        if len(variables) == 1:
            # Single variable: show value counts
            self.data[variables[0]].value_counts().plot(kind='bar')
            plt.xlabel(variables[0])
        else:
            # Multiple variables: show means
            means = self.data[variables].mean()
            means.plot(kind='bar')
            plt.xlabel('Variables')
        plt.ylabel('Value')
        plt.title(title)
        plt.xticks(rotation=45)

    def _create_line_chart(self, variables, title):
        """Create a line chart."""
        for var in variables:
            if var in self.data.columns:
                plt.plot(self.data.index, self.data[var], label=var, marker='o')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)

    def _create_histogram(self, variables, title):
        """Create a histogram."""
        for var in variables:
            if var in self.data.columns:
                plt.hist(self.data[var], alpha=0.6, label=var, bins=20)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title(title)
        if len(variables) > 1:
            plt.legend()

    def _create_box_plot(self, variables, title):
        """Create a box plot."""
        data_to_plot = [self.data[var].dropna() for var in variables if var in self.data.columns]
        plt.boxplot(data_to_plot, labels=variables)
        plt.ylabel('Value')
        plt.title(title)
        plt.xticks(rotation=45)

    def _create_scatter_plot(self, variables, title):
        """Create a scatter plot (2-way chart)."""
        if len(variables) < 2:
            print(f"  Warning: Scatter plot requires at least 2 variables")
            return

        x_var = variables[0]
        y_var = variables[1]

        plt.scatter(self.data[x_var], self.data[y_var], alpha=0.6)
        plt.xlabel(x_var)
        plt.ylabel(y_var)
        plt.title(title)
        plt.grid(True, alpha=0.3)

    def _create_heatmap(self, variables, title):
        """Create a correlation heatmap."""
        if not variables:
            variables = list(self.data.select_dtypes(include=['number']).columns)

        corr_matrix = self.data[variables].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                    square=True, linewidths=1)
        plt.title(title)

    def run(self):
        """Execute the full analytics pipeline."""
        print("\n" + "="*50)
        print("ANALYTICS TOOL")
        print("="*50)
        print(f"Data shape: {self.data.shape[0]} rows, {self.data.shape[1]} columns")
        print(f"Variables: {', '.join(self.data.columns)}")

        # Run statistics
        self.run_statistics()

        # Generate charts
        self.generate_charts()

        print("\n" + "="*50)
        print("ANALYSIS COMPLETE")
        print("="*50 + "\n")


def main():
    """Main entry point."""
    if len(sys.argv) < 3:
        print("Usage: python analytics.py <config.yaml> <data.csv>")
        print("\nExample: python analytics.py config.yaml sample_data.csv")
        sys.exit(1)

    config_path = sys.argv[1]
    data_path = sys.argv[2]

    # Check if files exist
    if not Path(config_path).exists():
        print(f"Error: Config file '{config_path}' not found")
        sys.exit(1)

    if not Path(data_path).exists():
        print(f"Error: Data file '{data_path}' not found")
        sys.exit(1)

    # Run analytics
    tool = AnalyticsTool(config_path, data_path)
    tool.run()


if __name__ == "__main__":
    main()
