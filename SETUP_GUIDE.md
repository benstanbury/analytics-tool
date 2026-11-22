# Learning Platform Analytics - Setup Guide

This guide helps you get started with the learning platform analytics scenario.

## What's Been Created

### 1. Sample Data Generator
**File**: `generate_learning_data.py`

Generates realistic learning platform data with 1,000 course enrollments including:
- 183 unique learners
- 9 learning paths across Python, R, and SQL
- Realistic progress percentages and completion dates
- Active/inactive status
- Step progression through learning paths

**Run it**:
```bash
python generate_learning_data.py
```

**Output**: `learning_platform_data.csv`

### 2. Analytics Configurations

#### Basic Configuration
**File**: `learning_platform_config.yaml`

**Analyses (5 charts)**:
1. Progress distribution histogram
2. Learning path step distribution
3. Progress and step box plots (side-by-side comparison)
4. Step vs progress scatter plot (relationship analysis)
5. Detailed progress distribution

**Focus**: Core engagement metrics and progress patterns

**Run it**:
```bash
python analytics.py learning_platform_config.yaml learning_platform_data.csv
```

**Output**: Statistics and charts in `output_learning/` directory

#### Detailed Configuration
**File**: `learning_platform_detailed_config.yaml`

**Analyses (7 charts)**:
1. Progress completion levels histogram
2. Learning path step distribution
3. Progress and step trends (line chart)
4. Correlation heatmap
5. Statistical distribution box plots
6. Step vs progress scatter plot
7. Average comparison bar chart

**Focus**: Statistical depth and correlation analysis

**Run it**:
```bash
python analytics.py learning_platform_detailed_config.yaml learning_platform_data.csv
```

**Output**: Statistics and charts in `output_learning_detailed/` directory

### 3. Documentation
**File**: `LEARNING_PLATFORM_ANALYTICS.md`

Comprehensive guide covering:
- Dataset structure and columns
- Each analysis explained in detail
- Business value and interpretation
- Ideas for extending the analysis
- Future dashboard suggestions

## Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Generate Sample Data
```bash
python generate_learning_data.py
```

You should see output like:
```
Generated 1000 course enrollment records
Unique learners: 183
Learning paths: 9
Languages: ['Python', 'R', 'SQL']
Active learners: 697 (69.7%)
Completed courses: 296 (29.6%)
```

### Step 3: Run Basic Analytics
```bash
python analytics.py learning_platform_config.yaml learning_platform_data.csv
```

This will:
- Print statistics to console
- Create `output_learning/statistics.json` and `statistics.txt`
- Generate 5 PNG chart files

### Step 4: Run Detailed Analytics
```bash
python analytics.py learning_platform_detailed_config.yaml learning_platform_data.csv
```

This will:
- Create more comprehensive statistics
- Generate 7 PNG chart files in `output_learning_detailed/`

### Step 5: Review Results

**Statistics**:
- Open `output_learning/statistics.txt` for human-readable stats
- Open `output_learning/statistics.json` for machine-readable data

**Charts**:
- Browse PNG files in output directories
- Each chart is named descriptively (e.g., `chart_1_histogram.png`)

## Understanding the Analyses

### Key Metrics

**Progress** (0-100%):
- Average around 50-60%: Moderate engagement
- High std deviation: Mixed learner engagement
- Peak at 100%: Strong completion culture
- Peak at 0-20%: Retention challenge

**Step** (1-8):
- Average around 3-4: Learners progressing through paths
- High concentration at Step 1: Many beginners
- Declining pattern: Natural funnel
- Even distribution: Good retention

### Interpreting Scatter Plots

The step vs progress scatter plot can reveal:

- **Vertical clusters**: Learners at same step with varied progress
  - Normal: Each course is independent

- **Diagonal pattern**: Higher steps correlate with higher progress
  - Good sign: Engaged learners advance through paths

- **Horizontal clusters**: Same progress across different steps
  - Concerning: May indicate disengagement

- **Outliers**: Unusual combinations (e.g., step 7 with 5% progress)
  - Action needed: Investigate why advanced learners aren't progressing

## Customising the Analysis

### Modify Statistics

Edit the YAML config to change which statistics are computed:

```yaml
statistics:
  variables:
    - progress
    - step
  operations:
    - mean      # Average
    - median    # Middle value
    - std       # Standard deviation
    - min       # Minimum
    - max       # Maximum
    - count     # Number of records
    - sum       # Total (useful for some metrics)
    - var       # Variance
```

### Add Charts

Add new chart definitions to the `charts` section:

```yaml
charts:
  # Your new chart
  - type: histogram
    variables: [progress]
    title: "My Custom Chart Title"
```

**Available chart types**:
- `histogram`: Distribution of values
- `box`: Statistical distribution with quartiles
- `scatter`: Relationship between two variables (requires exactly 2 variables)
- `bar`: Compare average values
- `line`: Trends over data points
- `heatmap`: Correlation matrix

## Next Steps

### Potential Extensions

1. **Filter by language**: Create separate CSV files for Python, R, and SQL learners
2. **Active vs inactive**: Split data by `is_active` status
3. **Time analysis**: Add columns for days since start, days to completion
4. **Completion prediction**: Identify patterns in learners who complete vs drop off
5. **Streamlit dashboard**: Interactive visualisations with filters and drill-downs

### Using Your Own Data

Replace `learning_platform_data.csv` with your actual learning platform export:

1. Ensure CSV has the required columns (or update YAML to match your columns)
2. Numeric columns work best for statistics (progress, step, scores, etc.)
3. Update `variables` in YAML config to match your column names
4. Run analytics with your data file

## Simplicity by Design

This setup is intentionally simple:

✅ **No custom code**: Uses existing analytics tool
✅ **YAML configuration**: Easy to read and modify
✅ **Standard formats**: CSV input, PNG/JSON output
✅ **Minimal dependencies**: Just pandas, matplotlib, seaborn
✅ **Self-documenting**: Comments explain each analysis

This makes it easy to maintain, extend, and share with non-technical stakeholders.

## Troubleshooting

**Issue**: `ModuleNotFoundError`
**Solution**: Run `pip install -r requirements.txt`

**Issue**: No charts generated
**Solution**: Check `output_dir` exists and you have write permissions

**Issue**: "Variable not found in data"
**Solution**: Verify column names in CSV match YAML config (case-sensitive)

**Issue**: Empty statistics
**Solution**: Ensure data file has numeric columns for statistical operations

## Questions?

Refer to:
- `LEARNING_PLATFORM_ANALYTICS.md` - Detailed analysis explanations
- `README.md` - Main analytics tool documentation
- YAML config files - Inline comments explain each setting
