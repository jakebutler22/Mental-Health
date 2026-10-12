"""Audit the Git publication set without printing credential values (stdlib only).

Run from any directory: python3 scripts/audit_publication.py
Includes tracked/index files, not unrelated ignored runtime data.
"""
import argparse
from pathlib import Path
import json
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def git(*args):
    return subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, check=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-pending-reports", action="store_true", help="Source checkpoint only; final submission audit must omit this option")
    options = parser.parse_args()
    problems = []
    tracked = git('ls-files', '-z')
    if tracked.returncode:
        print(json.dumps({'status': 'failed', 'reason': 'git ls-files failed'}))
        return 1
    paths = [Path(p.decode()) for p in tracked.stdout.split(b'\0') if p]
    secret_patterns = [
        re.compile(r'sk-or-v1-[A-Za-z0-9_-]{16,}'),
        re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}'),
        re.compile(r'github_pat_[A-Za-z0-9_]{20,}'),
        re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
        re.compile(r'(?i)(?:OPENROUTER_API_KEY|api_key|access_token)\s*[=:]\s*[\"\']?(?![\"\']?(?:$|\s|None\b|null\b|process\b|os\b|settings\b|config\b|key\b|<|YOUR|REPLACE|example))[A-Za-z0-9_-]{24,}'),
    ]
    markdown_count = 0
    reports = []
    for relative in paths:
        parts = relative.parts
        name = relative.name
        forbidden = any(p in {'.venv', 'venv', 'node_modules', '__pycache__', '.pytest_cache', '.clean-checkout', '.verification', '.runtime'} for p in parts)
        forbidden |= (name == '.env' or name.startswith('.env.')) and name != '.env.example'
        forbidden |= bool(re.search(r'\.(?:db|sqlite|sqlite3)(?:-|$)', name))
        if forbidden:
            problems.append({'file': str(relative), 'rule': 'forbidden-publication-path'})
            continue
        # Index contents are what an impending commit publishes, including staged changes.
        blob = git('show', ':' + relative.as_posix())
        if blob.returncode:
            problems.append({'file': str(relative), 'rule': 'unreadable-index-entry'})
            continue
        try:
            content = blob.stdout.decode('utf-8')
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(content.splitlines(), 1):
            if any(pattern.search(line) for pattern in secret_patterns):
                problems.append({'file': str(relative), 'line': number, 'rule': 'possible-credential-review-required'})
        if relative.suffix == '.md':
            markdown_count += 1
            for match in re.finditer(r'!?\[[^\]]*\]\(([^\n)]+)\)', content):
                target = match.group(1).strip().strip('<>')
                if target.startswith(('#', '/')) or urlsplit(target).scheme:
                    continue
                target = unquote(urlsplit(target).path)
                if target and not (ROOT / relative.parent / target).exists():
                    problems.append({'file': str(relative), 'line': content[:match.start()].count('\n') + 1, 'rule': 'missing-relative-link'})
            if relative.name == 'report.md' and parts[0] == 'submissions':
                commits = re.findall(r'(?i)(?:submitted source commit|source commit)\s*:\s*[*` ]*([0-9a-f]{40})', content)
                entry = {'file': str(relative), 'source_commits': commits}
                reports.append(entry)
                if not commits and not options.allow_pending_reports:
                    problems.append({'file': str(relative), 'rule': 'missing-exact-source-commit'})
                for commit in commits:
                    if git('cat-file', '-e', commit + '^{commit}').returncode:
                        problems.append({'file': str(relative), 'rule': 'source-commit-not-in-local-git'})
                if not re.search(r'https://github\.com/[^\s/]+/[^\s.)]+', content):
                    problems.append({'file': str(relative), 'rule': 'missing-repository-url'})
    print(json.dumps({'status': 'passed' if not problems else 'failed', 'scope': 'Git index publication set', 'pending_reports_allowed': options.allow_pending_reports, 'tracked_files': len(paths), 'markdown_files': markdown_count, 'reports': reports, 'findings': problems}, indent=2))
    return bool(problems)

if __name__ == '__main__':
    raise SystemExit(main())
