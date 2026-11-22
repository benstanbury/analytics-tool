#!/usr/bin/env python3
"""
Structure Test for Analytics Tool
----------------------------------
Tests the project structure without requiring external dependencies.
"""

import os
import sys
import ast

# A standalone script (run: python test_structure.py), not a pytest module; its helpers
# take arguments, so stop pytest collecting them as tests.
__test__ = False

def test_file_exists(filename, description):
    """Test if a file exists."""
    exists = os.path.exists(filename)
    status = "✓" if exists else "✗"
    print(f"{status} {description}: {filename}")
    return exists

def test_python_syntax(filename):
    """Test if Python file has valid syntax."""
    try:
        with open(filename, 'r') as f:
            ast.parse(f.read())
        print(f"  ✓ Valid Python syntax")
        return True
    except SyntaxError as e:
        print(f"  ✗ Syntax error: {e}")
        return False

def test_has_main_function(filename):
    """Test if Python file has a main function."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            if 'def main():' in content or 'def main(' in content:
                print(f"  ✓ Has main() function")
                return True
            else:
                print(f"  ⚠ No main() function found")
                return False
    except Exception as e:
        print(f"  ✗ Error reading file: {e}")
        return False

def test_has_class(filename, classname):
    """Test if Python file has a specific class."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            if f'class {classname}' in content:
                print(f"  ✓ Has class '{classname}'")
                return True
            else:
                print(f"  ⚠ No class '{classname}' found")
                return False
    except Exception as e:
        print(f"  ✗ Error reading file: {e}")
        return False

def main():
    """Run structure tests."""
    print("="*60)
    print("ANALYTICS TOOL - STRUCTURE TEST")
    print("="*60)
    print()

    all_tests_passed = True

    # Test core files
    print("Core Files:")
    print("-" * 60)
    all_tests_passed &= test_file_exists('analytics.py', 'Main analytics script')
    if os.path.exists('analytics.py'):
        all_tests_passed &= test_python_syntax('analytics.py')
        all_tests_passed &= test_has_class('analytics.py', 'AnalyticsTool')
        all_tests_passed &= test_has_main_function('analytics.py')

    print()
    all_tests_passed &= test_file_exists('config.yaml', 'Configuration file')
    print()
    all_tests_passed &= test_file_exists('sample_data.csv', 'Sample data file')
    print()
    all_tests_passed &= test_file_exists('requirements.txt', 'Requirements file')
    print()
    all_tests_passed &= test_file_exists('generate_sample_data.py', 'Data generator')
    if os.path.exists('generate_sample_data.py'):
        all_tests_passed &= test_python_syntax('generate_sample_data.py')

    print()
    all_tests_passed &= test_file_exists('README.md', 'Documentation')
    print()
    all_tests_passed &= test_file_exists('.gitignore', 'Git ignore file')

    # Test configuration
    print()
    print("Configuration Validation:")
    print("-" * 60)
    if os.path.exists('config.yaml'):
        with open('config.yaml', 'r') as f:
            config_content = f.read()

        if 'statistics:' in config_content:
            print("✓ Statistics section configured")
        else:
            print("✗ No statistics section")
            all_tests_passed = False

        if 'charts:' in config_content:
            print("✓ Charts section configured")
        else:
            print("✗ No charts section")
            all_tests_passed = False

        chart_types = ['bar', 'line', 'histogram', 'box', 'scatter', 'heatmap']
        found_types = [ct for ct in chart_types if f'type: {ct}' in config_content]
        print(f"✓ Chart types configured: {', '.join(found_types)}")

    # Test data file
    print()
    print("Data File Validation:")
    print("-" * 60)
    if os.path.exists('sample_data.csv'):
        with open('sample_data.csv', 'r') as f:
            lines = f.readlines()

        if len(lines) > 0:
            header = lines[0].strip()
            if 'a' in header and 'b' in header:
                print(f"✓ Header row: {header}")
            else:
                print(f"✗ Missing expected variables in header")
                all_tests_passed = False

            print(f"✓ Data rows: {len(lines) - 1}")
        else:
            print("✗ Empty data file")
            all_tests_passed = False

    # Test documentation
    print()
    print("Documentation Validation:")
    print("-" * 60)
    if os.path.exists('README.md'):
        with open('README.md', 'r') as f:
            readme = f.read()

        required_sections = ['Installation', 'Quick Start', 'Configuration', 'Usage']
        for section in required_sections:
            if section in readme:
                print(f"✓ Has '{section}' section")
            else:
                print(f"⚠ Missing '{section}' section")

    # Summary
    print()
    print("="*60)
    if all_tests_passed:
        print("✓ ALL STRUCTURE TESTS PASSED")
        print()
        print("Note: To run the analytics tool, you need to install dependencies:")
        print("  pip install -r requirements.txt")
        print()
        print("Then run:")
        print("  python analytics.py config.yaml sample_data.csv")
    else:
        print("✗ SOME TESTS FAILED")
    print("="*60)

if __name__ == '__main__':
    main()
