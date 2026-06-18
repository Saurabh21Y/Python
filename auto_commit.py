import os
import sys
import time
from datetime import datetime

# Default interval in seconds (60 minutes = 3600 seconds)
DEFAULT_INTERVAL = 3600

def run_commit():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"Auto commit at {timestamp}\n"
    
    # Write to commits.txt
    with open("commits.txt", "a") as file:
        file.write(log_entry)
    
    # Stage changes and commit
    os.system("git add .")
    os.system(f'git commit -m "Auto commit at {timestamp}"')
    print(f"[{timestamp}] Changes committed successfully.")

def main():
    # Get interval from command-line argument (in minutes)
    # e.g., "python auto_commit.py 15" will commit every 15 minutes
    interval = DEFAULT_INTERVAL
    if len(sys.argv) > 1:
        try:
            interval_mins = float(sys.argv[1])
            interval = int(interval_mins * 60)
            if interval <= 0:
                raise ValueError
        except ValueError:
            print("Invalid interval. Using default of 60 minutes.")
            interval = DEFAULT_INTERVAL

    print(f"Auto-commit daemon started.")
    print(f"Interval: {interval / 60:.1f} minute(s)")
    print("Press Ctrl+C to stop the script.")
    
    try:
        while True:
            run_commit()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nAuto-commit process stopped.")

if __name__ == "__main__":
    main()