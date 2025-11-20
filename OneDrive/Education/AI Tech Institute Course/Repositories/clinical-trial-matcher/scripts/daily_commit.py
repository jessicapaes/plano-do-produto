#!/usr/bin/env python3
"""
Daily commit script to maintain GitHub activity.
Run this script manually or schedule it with a task scheduler.
"""

import subprocess
import datetime
import os
from pathlib import Path

def make_daily_commit():
    """Create a daily commit to maintain repository activity."""
    
    repo_root = Path(__file__).parent.parent
    
    # Update activity log
    activity_file = repo_root / "activity.md"
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(activity_file, "a", encoding="utf-8") as f:
        f.write(f"\n## {datetime.datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"Activity update at {timestamp}\n\n")
    
    # Git operations
    os.chdir(repo_root)
    
    try:
        # Add the file
        subprocess.run(["git", "add", "activity.md"], check=True)
        
        # Commit
        commit_message = f"chore: daily activity update - {datetime.datetime.now().strftime('%Y-%m-%d')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Push
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print(f"✅ Successfully committed and pushed activity update at {timestamp}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    make_daily_commit()

