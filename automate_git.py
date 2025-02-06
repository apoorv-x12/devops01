import sys
from git import Repo

def automate_git(commit_message):
    """
    Automates the following Git commands:
    1. git add .
    2. git commit -m <commit_message>
    3. git push
    """
    try:
        # Initialize the repository in the current directory.
        repo = Repo(".")
        
        # Check if the repository is in a valid state.
        if repo.bare:
            print("The repository is bare. Exiting.")
            return
        
        # Stage all changes.
        print("Adding all changes...")
        repo.git.add('--all')
        
        # Commit changes with the provided commit message.
        print(f"Committing changes with message: {commit_message}")
        repo.index.commit(commit_message)
        
        # Push to the remote repository (default is 'origin').
        print("Pushing changes to remote repository...")
        origin = repo.remote(name='origin')
        push_info = origin.push()
        
        # Print push results.
        for info in push_info:
            print(info.summary)
        
        print("Automation complete.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if a commit message was provided via command line arguments.
    if len(sys.argv) != 2:
        print("Usage: python automate_git.py 'your commit message'")
        sys.exit(1)
    
    commit_msg = sys.argv[1]
    automate_git(commit_msg)
