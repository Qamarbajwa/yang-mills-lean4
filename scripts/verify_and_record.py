from pathlib import Path
from datetime import datetime, timezone
import subprocess, sys, json, platform, hashlib

ROOT = Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "evidence" / "test_runs"
OUTDIR.mkdir(parents=True, exist_ok=True)

def git_value(*args):
    try:
        p = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
        if p.returncode == 0:
            return p.stdout.strip()
        return None
    except FileNotFoundError:
        return None

def run(command):
    p = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr

def main():
    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    log_path = OUTDIR / f"verify_{stamp}.log"
    json_path = OUTDIR / f"verify_{stamp}.json"

    basetemp = OUTDIR / f".pytest_temp_{stamp}"
    commands = [
        [sys.executable, "-m", "pytest", "-q", "--basetemp", str(basetemp)],
        [sys.executable, "scripts/check_repo.py"],
    ]


    records = []
    all_ok = True
    full_log = []

    for cmd in commands:
        code, out, err = run(cmd)
        all_ok = all_ok and code == 0
        records.append({
            "command": cmd,
            "exit_code": code,
            "stdout": out,
            "stderr": err,
        })
        full_log.extend([
            "$ " + " ".join(cmd),
            out,
            err,
            f"[exit_code={code}]",
            "",
        ])

    log_text = "\n".join(full_log)
    log_path.write_text(log_text, encoding="utf-8")

    sha = hashlib.sha256(log_text.encode("utf-8")).hexdigest()
    payload = {
        "task_id": "YM-000",
        "timestamp_utc": now.isoformat(),
        "status": "PASS" if all_ok else "FAIL",
        "evidence_level": "E3_REPRODUCIBLE_MACHINE_EVIDENCE",
        "python": sys.version,
        "platform": platform.platform(),
        "git_sha": git_value("rev-parse", "HEAD"),
        "git_branch": git_value("branch", "--show-current"),
        "git_status": git_value("status", "--short"),
        "commands": records,
        "log_file": str(log_path.relative_to(ROOT)),
        "log_sha256": sha,
    }
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(f"Verification status: {payload['status']}")
    print(f"Evidence JSON: {json_path.relative_to(ROOT)}")
    print(f"Evidence log:  {log_path.relative_to(ROOT)}")
    print(f"Log SHA-256:   {sha}")
    return 0 if all_ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
