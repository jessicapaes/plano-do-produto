#!/usr/bin/env python3
"""
Multiple commits per day script.
This creates several commits throughout the day to show more activity.
"""

import subprocess
import datetime
import random
import os
from pathlib import Path

COMMIT_MESSAGES = [
    "docs: update activity log",
    "chore: maintain repository activity",
    "docs: update documentation",
    "chore: repository maintenance",
    "docs: update project status",
    "chore: daily update",
    "docs: update activity tracker",
    "chore: keep repository active",
]

def make_commit(message=None):
    """Create a single commit."""
    
    repo_root = Path(__file__).parent.parent
    os.chdir(repo_root)
    
    # Update activity log
    activity_file = repo_root / "activity.md"
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(activity_file, "a", encoding="utf-8") as f:
        f.write(f"- Update at {timestamp}\n")
    
    # Git operations
    try:
        subprocess.run(["git", "add", "activity.md"], check=True, capture_output=True)
        
        if not message:
            message = random.choice(COMMIT_MESSAGES)
        
        commit_message = f"{message} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True, capture_output=True)
        
        subprocess.run(["git", "push", "origin", "main"], check=True, capture_output=True)
        
        print(f"✅ Committed: {commit_message}")
        return True
        
    except subprocess.CalledProcessError as e:
        # No changes to commit is fine
        if "nothing to commit" in str(e).lower():
            print("ℹ️  No changes to commit")
            return True
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    import sys
    message = sys.argv[1] if len(sys.argv) > 1 else None
    make_commit(message)

