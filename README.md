# Analytics Tool

A flexible Python-based analytics tool for performing statistical analysis and data visualisation using YAML configuration files.

## Features

- **Statistical Analysis**: Compute various statistics (mean, sum, median, standard deviation, etc.) across any variables
- **Data Visualization**: Generate multiple chart types including:
  - Bar charts
  - Line charts
  - Histograms
  - Box plots
  - Scatter plots (2-way charts)
  - Correlation heatmaps
- **YAML Configuration**: Define your analysis workflow in a simple, readable YAML file
- **Flexible**: Works with rectangular (tabular) data in CSV format

## Installation

### Prerequisites

- Python 3.7 or higher

### Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- pandas (data manipulation)
- matplotlib (plotting)
- seaborn (statistical visualisation)
- pyyaml (YAML parsing)
- numpy (numerical operations)

## Quick Start

### 1. Basic Usage

Run the analytics tool with a configuration file and data file:

```bash
python analytics.py config.yaml sample_data.csv
```

### 2. Configuration File

Create a YAML configuration file to specify what analysis to perform. Here's an example:

```yaml
# Output directory for charts
output_dir: output

# Statistical Analysis
statistics:
  variables: [a, b, c, d, e]
  operations:
    - mean
    - sum
    - median
    - std

# Charts to Generate
charts:
  - type: bar
    variables: [a, b, c]
    title: "Variable Comparison"

  - type: scatter
    variables: [a, b]
    title: "A vs B Scatter Plot"
```

### 3. Data Format

Your data should be in CSV format with column headers. Example:

```csv
a,b,c,d,e
49.67,74.84,15.79,29.76,28
48.62,61.31,41.73,34.00,22
...
```

## Configuration Options

### Statistics Section

```yaml
statistics:
  variables: [a, b, c]  # Variables to analyse (omit for all)
  operations:           # Statistical operations to perform
    - mean              # Average
    - sum               # Total sum
    - median            # Median value
    - std               # Standard deviation
    - var               # Variance
    - min               # Minimum value
    - max               # Maximum value
    - count             # Count of values
```

### Charts Section

#### Bar Chart
Compare values across variables:
```yaml
- type: bar
  variables: [a, b, c, d]
  title: "Comparison Chart"
```

#### Line Chart
Show trends over data points:
```yaml
- type: line
  variables: [a, b]
  title: "Trend Analysis"
```

#### Histogram
Display distribution of values:
```yaml
- type: histogram
  variables: [a]
  title: "Distribution of Variable A"
```

#### Box Plot
Show statistical distribution:
```yaml
- type: box
  variables: [a, b, c, d, e]
  title: "Box Plot Comparison"
```

#### Scatter Plot (2-way chart)
Visualise relationship between two variables:
```yaml
- type: scatter
  variables: [a, b]  # First variable is X-axis, second is Y-axis
  title: "A vs B Relationship"
```

#### Heatmap
Show correlation between variables:
```yaml
- type: heatmap
  variables: [a, b, c, d, e]
  title: "Correlation Matrix"
```

## Example Workflow

1. **Prepare your data**: Create a CSV file with your variables
2. **Create configuration**: Define what statistics and charts you want
3. **Run analysis**:
   ```bash
   python analytics.py config.yaml data.csv
   ```
4. **View results**:
   - Statistics are printed to the console
   - Charts are saved in the output directory (default: `output/`)

## Sample Data

The repository includes sample data with variables a, b, c, d, e:

```bash
# Generate new sample data (optional)
python generate_sample_data.py

# Run analytics on sample data
python analytics.py config.yaml sample_data.csv
```

## Output

### Console Output
Statistics are printed in a readable format:

```
==================================================
STATISTICAL ANALYSIS
==================================================

a:
------------------------------
  mean           : 50.1234
  sum            : 5012.3400
  median         : 49.5600
  ...
```

### Chart Files
Charts are saved as PNG files in the output directory:
- `chart_1_bar.png`
- `chart_2_scatter.png`
- etc.

## Advanced Usage

### Custom Output Directory

Specify a custom output directory in your config:

```yaml
output_dir: my_results
```

### Multiple Analyses

Create different configuration files for different analyses:

```bash
python analytics.py basic_stats.yaml data.csv
python analytics.py detailed_charts.yaml data.csv
python analytics.py correlation_analysis.yaml data.csv
```

### Working with Your Own Data

1. Export your data as CSV with headers
2. Note the variable names (column headers)
3. Create a config file specifying your variables
4. Run the analysis

## Troubleshooting

### Missing Dependencies
```bash
pip install -r requirements.txt
```

### File Not Found
Ensure config and data files exist:
```bash
ls config.yaml sample_data.csv
```

### Invalid Configuration
Check your YAML syntax:
- Use spaces (not tabs) for indentation
- Ensure proper list formatting with brackets or dashes
- Validate variable names match your CSV columns

## Project Structure

```
.
├── analytics.py              # Main analytics tool
├── config.yaml               # Sample configuration
├── sample_data.csv           # Sample dataset
├── generate_sample_data.py   # Data generator script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── output/                   # Generated charts (created automatically)
```

## License

This project is provided as-is for educational and analytical purposes.