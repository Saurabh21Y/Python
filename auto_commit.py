import os
import sys
import time
from datetime import datetime

# Default interval in seconds (12 hours = 43200 seconds, resulting in 2 commits per day)
DEFAULT_INTERVAL = 43200

def run_commit():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"Auto commit at {timestamp}\n"
    
    # Write to commits.txt
    with open("commits.txt", "a") as file:
        file.write(log_entry)
    
    # Stage changes, commit, and push
    os.system("git add .")
    os.system(f'git commit -m "Auto commit at {timestamp}"')
    print(f"[{timestamp}] Changes committed successfully.")
    
    print(f"[{timestamp}] Pushing changes to remote...")
    os.system("git push")

def main():
    # Get interval from command-line argument (in hours)
    # e.g., "python auto_commit.py 12" will commit every 12 hours
    interval = DEFAULT_INTERVAL
    if len(sys.argv) > 1:
        try:
            interval_hours = float(sys.argv[1])
            interval = int(interval_hours * 3600)
            if interval <= 0:
                raise ValueError
        except ValueError:
            print("Invalid interval. Using default of 12 hours (2 commits per day).")
            interval = DEFAULT_INTERVAL

    print(f"Auto-commit daemon started.")
    print(f"Interval: {interval / 3600:.1f} hour(s) (~{24 * 3600 / interval:.1f} commits per day)")
    print("Press Ctrl+C to stop the script.")
    
    try:
        while True:
            run_commit()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nAuto-commit process stopped.")

if __name__ == "__main__":
    main()