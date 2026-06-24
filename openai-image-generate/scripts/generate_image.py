import argparse
import base64
import json
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_CONFIG = ROOT / "private_config.json"
OUTPUT_DIR = ROOT / "outputs"


def load_config():
    if not PRIVATE_CONFIG.exists():
        raise FileNotFoundError(f"missing config: {PRIVATE_CONFIG}")
    with PRIVATE_CONFIG.open("r", encoding="utf-8") as f:
        data = json.load(f)
    for key in ("base_url", "api_key", "model"):
        if not data.get(key):
            raise ValueError(f"missing config field: {key}")
    return data


def ensure_output_dir():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_b64_image(b64_text: str) -> Path:
    ensure_output_dir()
    filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    out = OUTPUT_DIR / filename
    out.write_bytes(base64.b64decode(b64_text))
    return out


def download_image(url: str) -> Path:
    ensure_output_dir()
    filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    out = OUTPUT_DIR / filename
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        out.write_bytes(resp.read())
    return out


def do_request(endpoint: str, api_key: str, payload: dict, timeout_seconds: int):
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
        return json.loads(raw)


def call_api(prompt: str, size: str, n: int, timeout_seconds: int):
    cfg = load_config()
    base_url = cfg["base_url"].rstrip("/")
    api_key = cfg["api_key"]
    model = cfg["model"]
    endpoint = f"{base_url}/images/generations"
    payload = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "n": n,
        "quality": "high",
    }
    try:
        return do_request(endpoint, api_key, payload, timeout_seconds)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        lowered = detail.lower()
        if e.code in (400, 422) and "quality" in lowered:
            fallback_payload = {
                "model": model,
                "prompt": prompt,
                "size": size,
                "n": n,
            }
            try:
                return do_request(endpoint, api_key, fallback_payload, timeout_seconds)
            except urllib.error.HTTPError as e2:
                detail2 = e2.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"http {e2.code}: {detail2[:500]}") from e2
        raise RuntimeError(f"http {e.code}: {detail[:500]}") from e


def extract_first_image_path(result: dict) -> Path:
    data = result.get("data") or []
    if not data:
        raise RuntimeError("no image data returned")
    first = data[0]
    if first.get("b64_json"):
        return save_b64_image(first["b64_json"])
    if first.get("url"):
        return download_image(first["url"])
    raise RuntimeError("unsupported response format: missing b64_json/url")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt")
    parser.add_argument("--size", default="1024x1024")
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=420)
    args = parser.parse_args()

    result = call_api(args.prompt, args.size, args.n, args.timeout)
    image_path = extract_first_image_path(result)
    print(str(image_path))


if __name__ == "__main__":
    main()
