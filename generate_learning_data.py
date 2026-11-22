"""
Generate sample learning platform data for analytics testing
"""
import csv
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
random.seed(42)

# Fixed "now" for last-login dates, so every run writes the same data
REFERENCE_DATE = datetime(2026, 1, 11, 21, 39, 50)

# Define learning paths
learning_paths = {
    'Python': [
        'Data Analyst in Python',
        'Python Developer',
        'Data Scientist in Python',
        'Machine Learning Specialist in Python'
    ],
    'R': [
        'Data Analyst in R',
        'Statistician in R',
        'Data Scientist in R'
    ],
    'SQL': [
        'SQL Fundamentals',
        'Database Administrator'
    ]
}

# Flatten paths with their languages
path_language_pairs = []
for lang, paths in learning_paths.items():
    for path in paths:
        path_language_pairs.append((path, lang))

# Generate learner names
first_names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Ethan', 'Sophia', 'Mason', 'Isabella', 'William',
               'Mia', 'James', 'Charlotte', 'Benjamin', 'Amelia', 'Lucas', 'Harper', 'Henry', 'Evelyn', 'Alexander',
               'Abigail', 'Michael', 'Emily', 'Daniel', 'Elizabeth', 'Matthew', 'Sofia', 'Jackson', 'Avery', 'Sebastian',
               'Ella', 'David', 'Scarlett', 'Joseph', 'Grace', 'Carter', 'Chloe', 'Owen', 'Victoria', 'Wyatt',
               'Riley', 'John', 'Aria', 'Jack', 'Lily', 'Luke', 'Aubrey', 'Dylan', 'Zoey', 'Grayson']

last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
              'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin',
              'Lee', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker']

# Generate 200 unique learners
num_learners = 200
learners = []
for i in range(num_learners):
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"
    email = f"{first.lower()}.{last.lower()}{i}@learningplatform.com"
    learners.append({'name': name, 'email': email})

# Generate 1000 course enrollments
data = []
base_date = datetime(2024, 1, 1)

for i in range(1000):
    # Select a learner
    learner = random.choice(learners)

    # Select a learning path and language
    path, language = random.choice(path_language_pairs)

    # Determine number of steps in path (courses range from 3-8 steps)
    max_steps = random.randint(3, 8)
    step = random.randint(1, max_steps)

    # Is the learner currently active? (70% active)
    is_active = random.random() < 0.7

    # Course start date (within last year)
    days_ago = random.randint(0, 365)
    dtm_course_started = base_date + timedelta(days=days_ago)

    # Last login (for active users, recent; for inactive, older)
    if is_active:
        last_login_days = random.randint(0, 30)
    else:
        last_login_days = random.randint(31, 180)
    last_login = REFERENCE_DATE - timedelta(days=last_login_days)

    # Progress percentage
    # Active users tend to have higher or varied progress
    # Some courses are completed (100%), some in progress
    if random.random() < 0.3:  # 30% completion rate
        progress = 100
        # Completed date is after start date
        days_to_complete = random.randint(7, 90)
        dtm_completed = dtm_course_started + timedelta(days=days_to_complete)
    else:
        # In progress - varied completion levels
        if is_active:
            progress = random.randint(5, 95)
        else:
            # Inactive users tend to have lower progress
            progress = random.randint(0, 50)
        dtm_completed = ''

    # Create record
    record = {
        'learner_name': learner['name'],
        'email': learner['email'],
        'last_login': last_login.strftime('%Y-%m-%d %H:%M:%S'),
        'is_active': is_active,
        'path': path,
        'step': step,
        'language': language,
        'dtm_course_started': dtm_course_started.strftime('%Y-%m-%d %H:%M:%S'),
        'progress': progress,
        'dtm_completed': dtm_completed if dtm_completed == '' else dtm_completed.strftime('%Y-%m-%d %H:%M:%S')
    }

    data.append(record)

# Save to CSV
with open('learning_platform_data.csv', 'w', newline='') as f:
    fieldnames = ['learner_name', 'email', 'last_login', 'is_active', 'path', 'step', 'language',
                  'dtm_course_started', 'progress', 'dtm_completed']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Calculate summary statistics
unique_learners = len(set(record['learner_name'] for record in data))
unique_paths = len(set(record['path'] for record in data))
unique_languages = set(record['language'] for record in data)
active_count = sum(1 for record in data if record['is_active'])
completed_count = sum(1 for record in data if record['progress'] == 100)

print(f"Generated {len(data)} course enrollment records")
print(f"Unique learners: {unique_learners}")
print(f"Learning paths: {unique_paths}")
print(f"Languages: {sorted(unique_languages)}")
print(f"Active learners: {active_count} ({active_count/len(data)*100:.1f}%)")
print(f"Completed courses: {completed_count} ({completed_count/len(data)*100:.1f}%)")
print(f"\nFirst 5 records:")
for i, record in enumerate(data[:5]):
    print(f"{i+1}. {record['learner_name']} - {record['path']} (Step {record['step']}) - Progress: {record['progress']}%")
print(f"\nData saved to: learning_platform_data.csv")
