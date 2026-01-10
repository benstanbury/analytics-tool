#!/usr/bin/env python3
"""
Unit Tests for Analytics Tool
------------------------------
Tests the analytics tool functionality including statistics saving.
"""

import pytest
import json
import tempfile
import shutil
from pathlib import Path
import pandas as pd
import yaml
from analytics import AnalyticsTool


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test outputs."""
    temp_path = tempfile.mkdtemp()
    yield temp_path
    shutil.rmtree(temp_path)


@pytest.fixture
def sample_data(temp_dir):
    """Create sample CSV data for testing."""
    data_path = Path(temp_dir) / 'test_data.csv'
    df = pd.DataFrame({
        'a': [1.0, 2.0, 3.0, 4.0, 5.0],
        'b': [10.0, 20.0, 30.0, 40.0, 50.0],
        'c': [5.0, 15.0, 25.0, 35.0, 45.0]
    })
    df.to_csv(data_path, index=False)
    return data_path


@pytest.fixture
def sample_config(temp_dir):
    """Create sample YAML config for testing."""
    config_path = Path(temp_dir) / 'test_config.yaml'
    config = {
        'output_dir': str(Path(temp_dir) / 'output'),
        'statistics': {
            'variables': ['a', 'b', 'c'],
            'operations': ['mean', 'median', 'std', 'min', 'max']
        }
    }
    with open(config_path, 'w') as f:
        yaml.dump(config, f)
    return config_path


def test_statistics_files_created(sample_config, sample_data, temp_dir):
    """Test that statistics.txt and statistics.json are created."""
    tool = AnalyticsTool(str(sample_config), str(sample_data))
    tool.run_statistics()

    output_dir = Path(temp_dir) / 'output'
    txt_file = output_dir / 'statistics.txt'
    json_file = output_dir / 'statistics.json'

    assert txt_file.exists(), "statistics.txt should be created"
    assert json_file.exists(), "statistics.json should be created"


def test_statistics_json_content(sample_config, sample_data, temp_dir):
    """Test that JSON file contains correct statistics structure."""
    tool = AnalyticsTool(str(sample_config), str(sample_data))
    tool.run_statistics()

    json_file = Path(temp_dir) / 'output' / 'statistics.json'

    with open(json_file, 'r') as f:
        stats_data = json.load(f)

    # Check structure
    assert 'a' in stats_data, "Variable 'a' should be in stats"
    assert 'b' in stats_data, "Variable 'b' should be in stats"
    assert 'c' in stats_data, "Variable 'c' should be in stats"

    # Check operations for variable 'a'
    assert 'mean' in stats_data['a'], "Mean should be calculated"
    assert 'median' in stats_data['a'], "Median should be calculated"
    assert 'std' in stats_data['a'], "Std should be calculated"
    assert 'min' in stats_data['a'], "Min should be calculated"
    assert 'max' in stats_data['a'], "Max should be calculated"


def test_statistics_json_values(sample_config, sample_data, temp_dir):
    """Test that JSON file contains correct calculated values."""
    tool = AnalyticsTool(str(sample_config), str(sample_data))
    tool.run_statistics()

    json_file = Path(temp_dir) / 'output' / 'statistics.json'

    with open(json_file, 'r') as f:
        stats_data = json.load(f)

    # Check specific values for variable 'a' (1.0, 2.0, 3.0, 4.0, 5.0)
    assert stats_data['a']['mean'] == 3.0, "Mean of a should be 3.0"
    assert stats_data['a']['median'] == 3.0, "Median of a should be 3.0"
    assert stats_data['a']['min'] == 1.0, "Min of a should be 1.0"
    assert stats_data['a']['max'] == 5.0, "Max of a should be 5.0"

    # Check specific values for variable 'b' (10.0, 20.0, 30.0, 40.0, 50.0)
    assert stats_data['b']['mean'] == 30.0, "Mean of b should be 30.0"
    assert stats_data['b']['min'] == 10.0, "Min of b should be 10.0"
    assert stats_data['b']['max'] == 50.0, "Max of b should be 50.0"


def test_statistics_txt_content(sample_config, sample_data, temp_dir):
    """Test that text file contains readable statistics."""
    tool = AnalyticsTool(str(sample_config), str(sample_data))
    tool.run_statistics()

    txt_file = Path(temp_dir) / 'output' / 'statistics.txt'

    with open(txt_file, 'r') as f:
        content = f.read()

    # Check for expected content
    assert 'STATISTICAL ANALYSIS' in content, "Should have header"
    assert 'a:' in content, "Should contain variable 'a'"
    assert 'b:' in content, "Should contain variable 'b'"
    assert 'c:' in content, "Should contain variable 'c'"
    assert 'mean' in content, "Should contain 'mean' operation"
    assert 'median' in content, "Should contain 'median' operation"


def test_output_directory_creation(sample_config, sample_data, temp_dir):
    """Test that output directory is created if it doesn't exist."""
    output_dir = Path(temp_dir) / 'output'
    assert not output_dir.exists(), "Output directory should not exist initially"

    tool = AnalyticsTool(str(sample_config), str(sample_data))
    tool.run_statistics()

    assert output_dir.exists(), "Output directory should be created"
    assert output_dir.is_dir(), "Output path should be a directory"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
