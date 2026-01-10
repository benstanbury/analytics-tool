#!/usr/bin/env python3
"""
Generate Sample Data
--------------------
Creates a sample CSV file with variables a, b, c, d, e for testing the analytics tool.
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of data points
n = 100

# Generate sample data
data = {
    'a': np.random.normal(50, 10, n),      # Normal distribution, mean=50, std=10
    'b': np.random.uniform(0, 100, n),      # Uniform distribution, 0-100
    'c': np.random.exponential(20, n),      # Exponential distribution, scale=20
    'd': np.random.normal(30, 5, n),        # Normal distribution, mean=30, std=5
    'e': np.random.poisson(25, n),          # Poisson distribution, lambda=25
}

# Create DataFrame
df = pd.DataFrame(data)

# Add some correlation between a and b for interesting scatter plots
df['b'] = df['a'] * 0.5 + df['b'] * 0.5 + np.random.normal(0, 5, n)

# Save to CSV
output_file = 'sample_data.csv'
df.to_csv(output_file, index=False)

print(f"Sample data generated successfully!")
print(f"File: {output_file}")
print(f"Shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())
print(f"\nBasic statistics:")
print(df.describe())
