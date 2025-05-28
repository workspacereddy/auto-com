import os
import subprocess
import datetime
import time

def setup_and_run_committer():
    GIT_EMAIL = os.environ['GIT_EMAIL']
    GIT_NAME = os.environ['GIT_NAME']
    REPO_URL = os.environ['REPO_URL']
    TOKEN = os.environ['GITHUB_TOKEN']

    def setup_git():
        with open(os.path.expanduser("~/.git-credentials"), "w") as cred:
            cred.write(f"https://{TOKEN}:x-oauth-basic@github.com\n")

        os.system("git config --global credential.helper store")
        os.system(f"git config --global user.email \"{GIT_EMAIL}\"")
        os.system(f"git config --global user.name \"{GIT_NAME}\"")

    def clone_repo():
        if not os.path.exists("repo"):
            clone_url = f"https://{TOKEN}@{REPO_URL}"
            os.system(f"git clone {clone_url} repo")

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
        print("Committed successfully. Sleeping for 24 hours...")
        time.sleep(24 * 60 * 60)
