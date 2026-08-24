from pathlib import Path
from datetime import datetime, timezone
import subprocess, json, hashlib

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "checkpoints"
OUT.mkdir(parents=True, exist_ok=True)

def git(*args):
    p = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()

def main():
    code, sha, err = git("rev-parse", "HEAD")
    if code != 0:
        raise SystemExit("Cannot seal checkpoint: Git repository/commit not available.")

    _, status, _ = git("status", "--short")
    _, branch, _ = git("branch", "--show-current")

    test_dir = ROOT / "evidence" / "test_runs"
    evidence = sorted(test_dir.glob("verify_*.json")) if test_dir.exists() else []
    latest = evidence[-1] if evidence else None
    latest_payload = json.loads(latest.read_text(encoding="utf-8")) if latest else None

    if not latest_payload or latest_payload.get("status") != "PASS":
        raise SystemExit("Cannot seal checkpoint: no latest PASS verification evidence.")

    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    payload = {
        "timestamp_utc": now.isoformat(),
        "git_sha": sha,
        "git_branch": branch,
        "working_tree_status": status,
        "verification_evidence": str(latest.relative_to(ROOT)),
        "verification_log_sha256": latest_payload.get("log_sha256"),
        "checkpoint_state": "BASELINE_SMOKE_TESTED" if status else "KNOWN_GOOD_CHECKPOINT_CANDIDATE",
    }
    raw = json.dumps(payload, indent=2)
    payload["checkpoint_record_sha256"] = hashlib.sha256(raw.encode("utf-8")).hexdigest()

    out = OUT / f"checkpoint_{stamp}.json"
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    md = ROOT / "KNOWN_GOOD_CHECKPOINT.md"
    md.write_text(
        "# KNOWN GOOD CHECKPOINT\n\n"
        f"- Timestamp UTC: `{payload['timestamp_utc']}`\n"
        f"- Git SHA: `{sha}`\n"
        f"- Branch: `{branch}`\n"
        f"- Working tree: `{'CLEAN' if not status else 'DIRTY'}`\n"
        f"- Verification: `{payload['verification_evidence']}`\n"
        f"- Verification log SHA-256: `{payload['verification_log_sha256']}`\n"
        f"- State: `{payload['checkpoint_state']}`\n",
        encoding="utf-8",
    )
    print(out.relative_to(ROOT))
    print(md.relative_to(ROOT))

if __name__ == "__main__":
    main()
