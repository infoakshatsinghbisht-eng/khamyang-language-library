import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

seen_en = set()
unique_records = []
with open('nlp_corpus/khamyang_en_hi_daily_part_001.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        r = json.loads(line)
        en = r['english'].strip().lower()
        if en not in seen_en:
            seen_en.add(en)
            unique_records.append(r)
        if len(unique_records) >= 60:
            break

for i, r in enumerate(unique_records[:40]):
    print(f"{i+1}. [{r['domain']}]")
    print(f"   Tai:    {r['khamyang_tai']}")
    print(f"   Roman:  {r['khamyang_roman']}")
    print(f"   EN:     {r['english']}")
    print(f"   HI:     {r['hindi']}")
