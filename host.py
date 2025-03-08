import os
import subprocess
import time
from datetime import datetime

# Repository details
repo_url = "https://github.com/mautpy/ccc.git"
repo_dir = "ccc"
script_name = "cc.py"

def run_command(command):
    """Runs a shell command and prints output in real-time."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in process.stdout:
        print(line, end="")  # Print output line-by-line

    for line in process.stderr:
        print(line, end="")  # Print errors line-by-line

    process.wait()  # Wait for process to finish

while True:
    # Get current time
    now = datetime.now()
    current_hour = now.hour

    # If it's 3 AM, rest for 1 hour
    if current_hour == 3:
        print("\nResting for 1 hour (3 AM - 4 AM)...\n")
        time.sleep(3600)  # Sleep for 1 hour
        continue  # Skip to the next loop iteration

    # Check if repo exists
    if os.path.exists(repo_dir):
        print(f"[{now}] Updating repository...\n")
        run_command(["git", "-C", repo_dir, "pull"])
    else:
        print(f"[{now}] Cloning repository...\n")
        run_command(["git", "clone", repo_url])

    # Change directory to the repo
    os.chdir(repo_dir)

    # Run the Python script
    print(f"\n[{now}] Running {script_name}...\n")
    run_command(["python3", script_name])

    # Go back to the original directory
    os.chdir("..")

    # Wait 1 hour before the next execution
    print(f"\n[{now}] Waiting for 1 hour before next update...\n")
    time.sleep(3600)  # Sleep for 1 hour
