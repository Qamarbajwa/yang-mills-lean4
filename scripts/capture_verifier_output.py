import json
import hashlib
import sys
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def capture_verifier_output(conversation_id: str, candidate_sha: str, task_id: str = "YM-002AR1"):
    log_path = Path(f"C:/Users/arqam/.gemini/antigravity/brain/{conversation_id}/.system_generated/logs/transcript.jsonl")
    full_log_path = Path(f"C:/Users/arqam/.gemini/antigravity/brain/{conversation_id}/.system_generated/logs/transcript_full.jsonl")
    if not log_path.exists() and not full_log_path.exists():
        raise FileNotFoundError(f"Transcript not found at {log_path} or {full_log_path}")
    
    target_log = full_log_path if full_log_path.exists() else log_path
    lines = [l for l in target_log.read_text(encoding="utf-8").split("\n") if l.strip()]
    
    last_response = None
    # Check send_message tool calls first for full transmitted audit reports
    for line in reversed(lines):
        try:
            step = json.loads(line)
        except Exception:
            continue
        tool_calls = step.get("tool_calls", [])
        for tc in tool_calls:
            if isinstance(tc, dict) and tc.get("name") == "send_message":
                args = tc.get("args") or tc.get("parameters") or {}
                msg = args.get("Message", "")
                if "INTEGRITY_PASS" in msg or "INTEGRITY_FAIL" in msg or "VERDICT" in msg.upper():
                    last_response = msg
                    break
        if last_response:
            break

    # Look for model responses if not found in tool calls
    if not last_response:
        for line in reversed(lines):
            try:
                step = json.loads(line)
            except Exception:
                continue
            if step.get("source") == "MODEL" and step.get("type") == "PLANNER_RESPONSE":
                content = step.get("content", "")
                if "INTEGRITY_PASS" in content or "INTEGRITY_FAIL" in content or "VERDICT" in content.upper():
                    last_response = content
                    break
    
    if not last_response:
        for line in reversed(lines):
            try:
                step = json.loads(line)
            except Exception:
                continue
            if step.get("source") == "MODEL":
                last_response = step.get("content", "")
                if last_response:
                    break
                
    if not last_response:
        raise ValueError(f"Could not extract model response from transcript for {conversation_id}")
        
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    raw_filename = f"{task_id}_E4_RAW_{ts}.md"
    raw_path = ROOT / "verification" / "raw" / raw_filename
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    
    raw_path.write_text(last_response.strip() + "\n", encoding="utf-8")
    sha256 = hashlib.sha256(raw_path.read_bytes()).hexdigest()
    
    print(f"CAPTURED_FILE: {raw_path.as_posix()}")
    print(f"RAW_SHA256: {sha256}")
    print(f"VERIFIER_ID: {conversation_id}")
    print(f"CANDIDATE_SHA: {candidate_sha}")
    print(f"TIMESTAMP: {ts}")
    
    return raw_path, sha256

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python capture_verifier_output.py CONVERSATION_ID CANDIDATE_SHA [TASK_ID]")
        sys.exit(1)
    capture_verifier_output(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "YM-002AR1")

