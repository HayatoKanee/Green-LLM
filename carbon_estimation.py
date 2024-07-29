from codecarbon import OfflineEmissionsTracker, EmissionsTracker, track_emissions
from unittest.mock import patch
import io
import sys


# Original code to be tested (example function that uses input and print)
def original_code():
    from itertools import permutations

    def solve() -> None:
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(3)]
        w = (sum(arr[0]) + 2) // 3
        for p in permutations(range(3)):
            start = [0] * 3
            end = [0] * 3
            i = s = 0
            for x in p:
                start[x] = i + 1
                s = 0
                while i < n and s < w:
                    s += arr[x][i]
                    i += 1
                end[x] = i
            if s >= w:
                for i in range(3):
                    print(start[i], end[i], end=" ")
                print()
                return
        print(-1)

    for _ in range(int(input())):
        solve()


def load_test_cases(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()


# Path to the text file containing test cases
test_cases_file = 'test.txt'

# Load the test cases from the file
test_cases = load_test_cases(test_cases_file)


# Function to run the original code with predefined inputs
def run_with_predefined_inputs(inputs):
    input_iter = iter(inputs)
    with patch('builtins.input', lambda: next(input_iter)):
        original_code()


# Start the tracker
tracker = OfflineEmissionsTracker(country_iso_code="GBR")
tracker.start()

# Capture the outputs
old_stdout = sys.stdout
sys.stdout = output_capture = io.StringIO()

# Run the original code with predefined inputs
run_with_predefined_inputs(test_cases)

# Stop the tracker
tracker.stop()

# Restore the original stdout
sys.stdout = old_stdout

# Print captured outputs
captured_output = output_capture.getvalue()
print("Captured Output:\n", captured_output)
