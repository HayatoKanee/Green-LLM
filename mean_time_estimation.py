import requests
import numpy as np

# Define the API endpoint
url = 'https://codeforces.com/api/contest.standings'
params = {
    'contestId': 1983,
    'asManager': 'False',
    'from': 1,
    'count': 10000,
    'showUnofficial': 'true'
}

# Make the GET request
response = requests.get(url, params=params)


def filter_outliers(times):
    mean = np.mean(times)
    std_dev = np.std(times)
    return [t for t in times if mean - 2 * std_dev <= t <= mean + 2 * std_dev]


# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the problem results
    rows = data['result']['rows']

    problem_times = {}

    for row in rows:
        problem_results = row['problemResults']
        previous_time = 0
        for i, result in enumerate(problem_results):
            problem_index = chr(65 + i)  # Convert 0, 1, 2, ... to A, B, C, ...
            if problem_index not in problem_times:
                problem_times[problem_index] = []

            time = result.get('bestSubmissionTimeSeconds', -1) - previous_time
            if time > 0:
                problem_times[problem_index].append(time)
            previous_time = result.get('bestSubmissionTimeSeconds', previous_time)

    filtered_times = {k: filter_outliers(v) for k, v in problem_times.items()}
    mean_times = {k: sum(v) / len(v) for k, v in filtered_times.items() if len(v) > 0}
    # mean_times = {k: sum(v) / len(v) for k, v in problem_times.items()}
    # Print mean submission times
    for problem, mean_time in mean_times.items():
        print(f"Mean submission time for problem {problem}: {mean_time:.2f} seconds")
else:
    print(f"Failed to retrieve data: {response.status_code}")
