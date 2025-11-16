#!/usr/bin/env python3
import os
import json
import requests
from bs4 import BeautifulSoup

# === CONFIG ===
SCHOLAR_USER_ID = "8-IhrB0AAAAJ"   # your Google Scholar user ID
OUT_PATH = "assets/json/citations.json"

def fetch_total_citations():
    url = f"https://scholar.google.com/citations?user={SCHOLAR_USER_ID}&hl=en"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        )
    }
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    # On Scholar, the total citations is in the first cell of this table
    table = soup.find("table", id="gsc_rsb_st")
    if not table:
        raise RuntimeError("Could not find citation stats table on Google Scholar page.")

    cells = table.find_all("td", class_="gsc_rsb_std")
    if not cells:
        raise RuntimeError("Could not find citation value cell on Google Scholar page.")

    total_citations = cells[0].get_text(strip=True)
    return total_citations

def main():
    citations = fetch_total_citations()
    print(f"Total citations: {citations}")

    data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": citations,
        "color": "9cf"
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    print(f"Wrote {OUT_PATH}")

if __name__ == "__main__":
    main()
