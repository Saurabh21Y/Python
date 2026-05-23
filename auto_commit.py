import os
from datetime import datetime

num_commits = int(input("Enter number of commits: "))

for i in range(num_commits):
    with open("commits.txt", "a") as file:
        file.write(f"Commit {i+1} at {datetime.now()}\n")

    os.system("git add .")
    os.system(f'git commit -m "Auto commit {i+1}"')

print(f"{num_commits} commits completed!")