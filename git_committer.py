import os
import subprocess
import datetime
import time

# HARDCODED values
GIT_EMAIL = "workspacereddy@gmail.com"
GIT_NAME = "workspacereddy"
REPO_URL = "github.com/workspacereddy/auto-com.git"

def setup_and_run_committer():
    TOKEN = os.environ['GITHUB_TOKEN']

    def setup_git():
        os.system(f"git config --global user.email \"{GIT_EMAIL}\"")
        os.system(f"git config --global user.name \"{GIT_NAME}\"")

    def clone_repo():
        if not os.path.exists("repo"):
            clone_url = f"https://{TOKEN}@{REPO_URL}"
            os.system(f"git clone {clone_url} repo")
        # Update remote URL to ensure token is used for pushing
        os.chdir("repo")
        os.system(f"git remote set-url origin https://{TOKEN}@{REPO_URL}")
        os.chdir("..")

    def commit_changes():
        os.chdir("repo")
        with open("log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - Automated log entry\n")

        subprocess.run(["git", "add", "log.txt"])
        subprocess.run(["git", "commit", "-m", "Automated commit"])
        subprocess.run(["git", "push"])
        os.chdir("..")

    setup_git()
    clone_repo()
    while True:
        commit_changes()
        print("✅ Committed successfully. Sleeping for 1 minute...")
        time.sleep(60)  # Use 86400 for 24-hour interval
