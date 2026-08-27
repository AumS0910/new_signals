import re
import requests

html = requests.get("https://www.zeebusinesslive.com/", timeout=20).text
scripts = re.findall(r'<script[^>]+src="([^"]+)', html)
print("scripts", len(scripts))
for src in scripts:
    url = "https://www.zeebusinesslive.com" + src if src.startswith("/") else src
    text = requests.get(url, timeout=20).text
    hits = sorted(set(re.findall(r"[^\"']{0,100}(?:/api/|signals|recommend|trades)[^\"']{0,160}", text, re.I)))
    if hits:
        print("\n--", src)
        print("\n".join(hits[:100]))

response = requests.get("https://www.zeebusinesslive.com/api/trades?day=0", timeout=20)
print("\nTRADES", response.status_code, len(response.text))
data = response.json()
print("keys", data.keys())
items = data.get("data", [])
print("count", len(items))
import json
with open("website_trades_2026-08-27.json", "w", encoding="utf-8") as handle:
    json.dump(data, handle, ensure_ascii=False, indent=2)
print("item keys", sorted(items[0].keys()) if items else [])
for item in items[:5]:
    print(json.dumps(item, ensure_ascii=False))
