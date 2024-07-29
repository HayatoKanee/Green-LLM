import numpy as np
import requests

# Define the API endpoint
url = 'https://codeforces.com/api/contest.status'
params = {
    'contestId': 1983,
    'asManager': 'False',
    'from': 1,
    'count': 200000,
}


# Function to filter outliers
def filter_outliers(times):
    mean = np.mean(times)
    std_dev = np.std(times)
    return [t for t in times if mean - 2 * std_dev <= t <= mean + 2 * std_dev]


# Function to calculate the average runtime for Python submissions
def calculate_average_runtime(data):
    index_times = {}
    index_memory = {}

    for result in data['result']:
        problem_index = result['problem']['index']
        programming_language = result['programmingLanguage']
        time_consumed = result['timeConsumedMillis']
        verdict = result['verdict']
        memory_consumed = result['memoryConsumedBytes']

        if programming_language.startswith('C++') and verdict == 'OK':
            if problem_index not in index_times:
                index_times[problem_index] = []
                index_memory[problem_index] = []
            index_times[problem_index].append(time_consumed)
            index_memory[problem_index].append(memory_consumed)

    average_times = {}
    average_memory = {}
    for index, memory in index_memory.items():
        memory_filtered = filter_outliers(memory)
        if memory_filtered:  # Avoid division by zero
            average_memory[index] = np.mean(memory_filtered)
    for index, times in index_times.items():
        times_filtered = filter_outliers(times)
        if times_filtered:  # Avoid division by zero
            average_times[index] = np.mean(times_filtered)

    return average_times, average_memory


# Make the GET request
response = requests.get(url, params=params)

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    if data['status'] == 'OK':
        average_runtimes, average_memory = calculate_average_runtime(data)
        print("Average runtimes (in milliseconds) for Python submissions by problem index:")
        for index, avg_time in average_runtimes.items():
            print(f"Index {index}: {avg_time:.2f} ms")
        for index, avg_memory in average_memory.items():
            print(f"Index {index}: {avg_memory:.2f} Bytes")
    else:
        print("Error in API response:", data['comment'])
else:
    print("Failed to fetch data from API. Status code:", response.status_code)
