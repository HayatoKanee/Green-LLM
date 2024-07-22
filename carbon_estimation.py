from codecarbon import OfflineEmissionsTracker, EmissionsTracker, track_emissions
from unittest.mock import patch
import io
import sys


# Original code to be tested (example function that uses input and print)
def original_code():
    for _ in range(int(input())):
        n = int(input())
        s = [i for i in range(1, n + 1)]
        print(*s)


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
