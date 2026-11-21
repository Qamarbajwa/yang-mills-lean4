import os
import json
import urllib.request
import winreg

def get_token():
    for var in ("ZENODO_TOKEN", "ZENODO_ACCESS_TOKEN", "ZENODO_API_TOKEN"):
        val = os.environ.get(var, "").strip()
        if val:
            return val
    try:
        k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment")
        token, _ = winreg.QueryValueEx(k, "ZENODO_TOKEN")
        if token.strip():
            return token.strip()
    except Exception:
        pass
    return None

def main():
    token = get_token()
    if not token:
        print("No token found")
        return 1

    page = 1
    all_deps = []
    while True:
        url = f"https://zenodo.org/api/deposit/depositions?size=50&page={page}&sort=mostrecent"
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                batch = json.loads(r.read().decode("utf-8"))
                if not batch:
                    break
                all_deps.extend(batch)
                if len(batch) < 50:
                    break
                page += 1
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            break

    print(f"Total depositions found: {len(all_deps)}")
    for i, d in enumerate(all_deps):
        dep_id = d.get("id")
        doi = d.get("doi")
        submitted = d.get("submitted")
        title = (d.get("title") or d.get("metadata", {}).get("title", ""))[:80]
        print(f"{i+1:2d}. ID: {dep_id} | DOI: {doi} | Sub: {submitted} | Title: {title}")

if __name__ == "__main__":
    main()
