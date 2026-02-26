from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

SCHOLAR_USER_ID = "8-IhrB0AAAAJ"   # your Google Scholar user ID
OUT_PATH = "assets/json/citations.json"

author: dict = scholarly.search_author_id(SCHOLAR_USER_ID)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

with open(f'assets/json/citations.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)


shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'assets/json/citations_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
