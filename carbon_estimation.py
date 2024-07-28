from codecarbon import OfflineEmissionsTracker, EmissionsTracker, track_emissions
from unittest.mock import patch
import io
import sys


# Original code to be tested (example function that uses input and print)
def original_code():
    from collections import defaultdict
    def cf1983F():
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
    
        ans = 0
        f = [n] * n
        for d in range(29,-1,-1):
            p = defaultdict()
            nf = f.copy()
            for i in range(n):
                cur  = (a[i] ^ ans) >> d
                if cur in p.keys():
                    j = p[cur]
                    if nf[j] > i:
                        nf[j] = i
                p[a[i] >> d] = i
    
            for i in range(n-2,-1,-1):
                if nf[i] > nf[i+1]:
                    nf[i] = nf[i+1]
    
            sm = 0
            for i in range(n):
                sm += n - nf[i]
    
            if sm < k:
                ans |= (1 << d)
                for i, x in enumerate(nf):
                    f[i] = x
    
        print(ans)
        return
    
 
 
 
    t = int(input())
    for i in range(t):
        cf1983F()


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
