import os
import subprocess
import argparse
import sys
from datetime import datetime
 
def run_command(command, cwd=None):
    """Run a shell command and handle errors."""
    try:
        print(f"Running command: {' '.join(command)}")
        result = subprocess.run(command, cwd=cwd, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {e.stderr}")
        sys.exit(1)
 from git import Repo, GitCommandError

class GitOperations:
    def commit_and_push(self, files, branch, repo_path='.', remote='origin', commit_message='Auto-commit'):
        try:
            print(f"DEBUG: repo_path = {repo_path}")
            print(f"DEBUG: files = {files}")
            print(f"DEBUG: branch = {branch}")

            repo = Repo(repo_path)
            assert not repo.bare

            repo.index.add([files] if isinstance(files, str) else files)
            repo.index.commit(commit_message)
            repo.remote(name=remote).push(refspec=f"{branch}:{branch}")

            print("Successfully committed and pushed.")
        except GitCommandError as e:
            raise Exception(f"GIT ERROR: {e}")
        except Exception as e:
            raise Exception(f"UNEXPECTED ERROR: {e}")

    # Git config (optional for automation)
    run_command(['git', 'config', 'user.email', 'copado-bot@example.com'])
    run_command(['git', 'config', 'user.name', 'Copado Robot Bot'])
 
    # Git add files
    for file in files:
        if os.path.exists(file):
            run_command(['git', 'add', file])
        else:
            print(f"⚠️ Warning: File does not exist and won't be committed: {file}")
 
    # Commit
    full_message = f"{commit_message} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    run_command(['git', 'commit', '-m', full_message])
 
    # Pull (handle conflicts in automation)
    run_command(['git', 'pull', '--rebase', remote, branch])
 
    # Push
    run_command(['git', 'push', remote, branch])
 
    print("✅ Changes committed and pushed successfully.")
 
def parse_args():
    parser = argparse.ArgumentParser(description="Commit and push changes to GitHub (Copado style).")
    parser.add_argument("--repo_path", required=True, help="Path to the local Git repository")
    parser.add_argument("--files", nargs='+', required=True, help="List of files to commit and push")
    parser.add_argument("--message", required=True, help="Commit message")
    parser.add_argument("--branch", default="main", help="Git branch to push to")
    parser.add_argument("--remote", default="origin", help="Git remote name")
    return parser.parse_args()
 
def main():
    args = parse_args()
    commit_and_push(args.repo_path, args.files, args.message, args.branch, args.remote)
 
if __name__ == "__main__":
    main()