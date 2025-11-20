# GitHub Activity Automation Guide

This guide explains different methods to maintain consistent GitHub activity.

## Method 1: GitHub Actions (Recommended - Automatic)

The `.github/workflows/daily-activity.yml` workflow automatically commits daily at 9 AM UTC.

**Setup:**
- Already configured! Just push this repository and the workflow will run automatically.
- The workflow runs on a schedule and commits to `activity.md`
- No local setup required

**Customize the schedule:**
Edit `.github/workflows/daily-activity.yml` and change the cron expression:
- `'0 9 * * *'` = 9 AM UTC daily
- `'0 */6 * * *'` = Every 6 hours
- `'0 9,15,21 * * *'` = 9 AM, 3 PM, 9 PM daily

## Method 2: Local Python Script

Run the script manually or schedule it with Windows Task Scheduler.

**Manual run:**
```bash
python scripts/daily_commit.py
```

**Windows Task Scheduler setup:**
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (e.g., daily at specific times)
4. Action: Start a program
5. Program: `python` (or full path to python.exe)
6. Arguments: `C:\path\to\clinical-trial-matcher\scripts\daily_commit.py`
7. Start in: `C:\path\to\clinical-trial-matcher`

## Method 3: Multiple Commits Per Day

To have several commits per day, you can:

1. **Modify the GitHub Actions workflow** to run multiple times:
```yaml
schedule:
  - cron: '0 9 * * *'   # 9 AM
  - cron: '0 14 * * *'  # 2 PM
  - cron: '0 19 * * *'  # 7 PM
```

2. **Use the Python script** multiple times per day via Task Scheduler

3. **Create different activity types:**
   - Update documentation
   - Add code comments
   - Update dependencies
   - Refactor small sections
   - Add tests

## Method 4: Legitimate Development Practices

The best way to show activity is through real work:

- **Small, frequent commits** (best practice anyway!)
- **Documentation updates** as you learn
- **Code improvements** and refactoring
- **Adding comments** and docstrings
- **Updating dependencies**
- **Writing tests**

## Tips

1. **Commit messages matter**: Use meaningful messages like "docs: update README" or "refactor: improve code structure"
2. **Spread commits**: Don't commit everything at once - make multiple small commits
3. **Weekend activity**: GitHub Actions runs on weekends too, keeping your graph green
4. **Multiple repositories**: Activity across multiple repos shows more engagement

## Best Practices

✅ **Do:**
- Use automation for maintenance tasks
- Make real improvements when possible
- Write meaningful commit messages
- Follow conventional commit format (feat:, fix:, docs:, etc.)

❌ **Don't:**
- Make empty commits with no purpose
- Commit random characters or gibberish
- Violate repository guidelines
- Spam commits excessively

## Current Setup

- ✅ GitHub Actions workflow configured
- ✅ Python script available for local use
- ✅ Activity log file created

Just push this repository and the automation will start working!

