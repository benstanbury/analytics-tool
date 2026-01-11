# Learning Platform Analytics

This directory contains analytics configurations specifically designed for learning platform data analysis.

## Dataset Overview

**File**: `learning_platform_data.csv`
**Records**: 1,000 course enrollments
**Unique Learners**: ~183

### Columns

| Column | Type | Description |
|--------|------|-------------|
| `learner_name` | String | Full name of the learner |
| `email` | String | Email address |
| `last_login` | DateTime | Most recent login timestamp |
| `is_active` | Boolean | Whether learner currently has an active licence |
| `path` | String | Learning path name (e.g., "Data Analyst in Python") |
| `step` | Integer | Current step/course number in the path (1-8) |
| `language` | String | Programming language (Python, R, or SQL) |
| `dtm_course_started` | DateTime | When the course was started |
| `progress` | Integer | Course completion percentage (0-100%) |
| `dtm_completed` | DateTime | Completion timestamp (empty if not completed) |

### Learning Paths Available

**Python Paths:**
- Data Analyst in Python
- Python Developer
- Data Scientist in Python
- Machine Learning Specialist in Python

**R Paths:**
- Data Analyst in R
- Statistician in R
- Data Scientist in R

**SQL Paths:**
- SQL Fundamentals
- Database Administrator

## Analytics Configuration

**Config File**: `learning_platform_config.yaml`

### Analysis 1: Course Progress Statistics

**Objective**: Understand overall learner progress across all courses

**Metrics Computed**:
- **Mean progress**: Average completion percentage (useful for overall engagement)
- **Median progress**: Middle value (less affected by outliers)
- **Standard deviation**: How varied progress levels are
- **Min/Max**: Range of progress values
- **Count**: Total number of course enrollments

**Business Value**:
- Identifies if most learners are engaged (high average)
- High std deviation indicates mixed engagement levels
- Low median with higher mean suggests some highly engaged learners but many struggling

### Analysis 2: Progress Distribution Histogram

**Objective**: Visualise how learners are distributed across completion levels

**Chart Type**: Histogram of `progress` variable

**What It Shows**:
- Peak at 0-20%: Many learners drop early (potential onboarding issue)
- Peak at 80-100%: Strong completion rate (engaged learners)
- Uniform distribution: Learners at all stages
- Bimodal distribution: Two distinct groups (e.g., completers vs early droppers)

**Business Value**:
- Identifies drop-off patterns
- Helps target interventions (e.g., support for 30-40% progress range)
- Measures effectiveness of course design

### Analysis 3: Learning Path Step Distribution

**Objective**: Understand where learners are in their learning journeys

**Chart Type**: Histogram of `step` variable

**What It Shows**:
- High concentration at Step 1: Many beginners, possible retention issue
- Decreasing trend: Normal funnel, some drop-off between steps
- Uniform distribution: Good retention across the path
- Peak at later steps: Experienced learners returning

**Business Value**:
- Identifies which steps lose learners
- Helps allocate resources to difficult steps
- Validates path difficulty progression

### Analysis 4: Progress and Step Box Plots

**Objective**: Compare distributions of progress and step side-by-side

**Chart Type**: Box plot showing both variables

**What It Shows**:
- **Median line**: Central tendency for each metric
- **Box**: Middle 50% of data (interquartile range)
- **Whiskers**: Typical range of values
- **Outliers**: Unusual cases (e.g., step 8 with 5% progress)

**Business Value**:
- Quick visual comparison of spread
- Identifies outliers needing attention
- Shows if progress is more varied than step position

### Analysis 5: Step vs Progress Relationship

**Objective**: Determine if course position correlates with completion

**Chart Type**: Scatter plot (step on X-axis, progress on Y-axis)

**Possible Patterns**:

1. **Positive correlation**: Learners at higher steps have higher progress
   - *Interpretation*: Engaged learners progress through paths
   - *Action*: Focus on keeping learners motivated

2. **No correlation**: Progress varies regardless of step
   - *Interpretation*: Each course is independent
   - *Action*: Improve individual course quality

3. **Negative correlation**: Higher steps have lower progress
   - *Interpretation*: Later courses may be too difficult
   - *Action*: Review difficulty curve, add support

4. **Clusters**: Distinct groups (e.g., completers at all steps, droppers at step 1)
   - *Interpretation*: Different learner segments
   - *Action*: Personalise learning paths

**Business Value**:
- Validates learning path design
- Identifies difficulty spikes
- Informs curriculum improvements

## Usage Instructions

### 1. Generate Sample Data

```bash
python generate_learning_data.py
```

This creates `learning_platform_data.csv` with 1,000 realistic course enrollments.

### 2. Run Analytics

```bash
python analytics.py learning_platform_config.yaml learning_platform_data.csv
```

### 3. View Results

**Statistics**: Check `output_learning/statistics.txt` or `statistics.json`

**Charts**: Open PNG files in `output_learning/`:
- `chart_1_histogram.png` - Progress distribution
- `chart_2_histogram.png` - Step distribution
- `chart_3_box.png` - Progress and step box plots
- `chart_4_scatter.png` - Step vs progress relationship
- `chart_5_histogram.png` - Detailed progress distribution

## Extending the Analysis

### Ideas for Additional Analyses

While the current YAML-based tool works well for numeric data, here are ideas for more advanced analyses:

1. **Language Comparison**: Create separate CSV files filtered by language, then compare:
   - Python vs R vs SQL completion rates
   - Which language has highest engagement

2. **Active vs Inactive Analysis**: Filter data by `is_active` status:
   - Compare progress distributions
   - Identify patterns in inactive learners

3. **Path-Specific Analysis**: Filter by learning path:
   - Which paths have best completion rates
   - Compare difficulty across paths

4. **Time-Based Analysis**: Convert datetime columns to numeric:
   - Days since course start vs progress
   - Time to completion distribution
   - Login recency vs engagement

5. **Cohort Analysis**: Group by start date periods:
   - Monthly cohort retention
   - Seasonal patterns in engagement

### Future Dashboard Ideas

For a Streamlit dashboard, consider:

- **Interactive filters**: Select language, path, active status
- **Real-time metrics**: Total learners, avg progress, completion rate
- **Trend charts**: Progress over time, new enrollments
- **Learner segments**: Identify at-risk learners, champions, beginners
- **Predictive analytics**: Likelihood to complete based on early progress

## Key Insights from Sample Data

Based on the generated 1,000 record sample:

- **69.7% active learners**: Good retention of licensed users
- **29.6% completion rate**: Room for improvement in course completion
- **183 unique learners**: Average of ~5.5 course enrollments per learner
- **9 learning paths**: Diverse curriculum across 3 languages

## Notes on Simplicity

This analytics setup follows a "keep it simple" philosophy:

✅ **Simple YAML configs**: Easy to read and modify
✅ **Standard CSV format**: Works with any data export
✅ **Self-documenting**: Comments explain each analysis
✅ **No complex code**: Uses existing analytics tool
✅ **Clear visualisations**: Standard chart types everyone understands

This makes the analysis accessible to non-technical stakeholders whilst providing actionable insights.
