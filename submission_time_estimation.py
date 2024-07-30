import requests
import json
from collections import defaultdict

# Define the API endpoint
url = 'https://codeforces.com/api/contest.status'
params = {
    'contestId': 1983,
    'asManager': 'False',
    'from': 1,
    'count': 200000,
}
response = requests.get(url, params=params)
data = response.json()

# Check if the request was successful
if data['status'] != 'OK':
    raise Exception('API request failed')


# Initialize dictionaries to count submissions
task_submissions = defaultdict(list)

# Process the submissions
for submission in data['result']:
    user = submission['author']['members'][0]['handle']
    task = submission['problem']['index']
    task_submissions[task].append(user)

# Calculate the mean number of submissions per task
task_mean_submissions = {}

for task, users in task_submissions.items():
    user_submission_counts = defaultdict(int)
    for user in users:
        user_submission_counts[user] += 1
    mean_submissions = sum(user_submission_counts.values()) / len(user_submission_counts)
    task_mean_submissions[task] = mean_submissions

# Print the mean number of submissions for each task
for task, mean in task_mean_submissions.items():
    print(f'Task {task}: Mean number of submissions per user: {mean}')