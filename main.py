import os
import subprocess

from rich import box
from rich import print
from rich.panel import Panel
from rich.traceback import install
install(show_locals=True)

def get_commits():
    # Ask for the repository path from the user
    repo = input("Enter the repository path: ")

    # Change the current working directory to the specified repository
    try:
        os.chdir(repo)
    except FileNotFoundError:
        print(f"Repository path '{repo}' not found. Please enter a valid path.")
        return

    # Git pull all the remote origin updates from all branches
    pull_command = ["git", "pull", "--all"]
    subprocess.run(pull_command, check=True)

    # Git log command to get commit details
    log_command = ["git", "log", "--all", "--after=2021-06-10", "--pretty=format:%h, %an, %ad, %s"]

    try:
        # Capture the output of the git log command
        result = subprocess.run(log_command, capture_output=True, text=True, check=True)
        # Print the commit logs
        print("Commit logs:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error fetching commit logs: {e}")

def commit_panel():
          ...

def get_docs():
          ...


get_commits()