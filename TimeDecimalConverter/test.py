#Tests conversion methods two-ways

import subprocess

def run_script(script_path, num_runs):
    success_count = 0

    for _ in range(num_runs):
        # Run the script and capture the output
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        output = result.stdout.splitlines()

        # Check if the script produced at least three lines of output
        if len(output) >= 3:
            # Compare the first and third line
            if output[0] == output[2]:
                success_count += 1

    # Calculate success rate
    success_rate = (success_count / num_runs) * 100
    return success_rate

# Example usage
script_path = 'C:/Users/l/Desktop/Personal Python Projects/proj1/main.py'
num_runs = 150  # Number of times you want to run the script
success_rate = run_script(script_path, num_runs)
print(f"Success Rate: {success_rate}%")
