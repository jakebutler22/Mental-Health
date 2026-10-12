"""Local verification runner; optional explicit prior key access, no secret persistence."""
import argparse
import os
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--mode", choices=["mock", "live"], default="mock")
parser.add_argument("--port", type=int, default=8001)
parser.add_argument("--database", default="backend/data/campus-pause.sqlite3")
parser.add_argument("--prior-key-file", type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
environment = os.environ.copy()
environment["MODEL_MODE"] = args.mode
environment["DATABASE_PATH"] = str((root / args.database).resolve())
if args.prior_key_file and not environment.get("OPENROUTER_API_KEY"):
    # Read exactly one authorized key. Never copy the file or persist its contents.
    from dotenv import dotenv_values
    value = dotenv_values(args.prior_key_file).get("OPENROUTER_API_KEY")
    if value:
        environment["OPENROUTER_API_KEY"] = value
subprocess.run([str(root / "backend/.venv/bin/python"), "-m", "uvicorn", "app.main:app", "--app-dir", str(root / "backend"), "--host", "127.0.0.1", "--port", str(args.port)], env=environment, check=True)
