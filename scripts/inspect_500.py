import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

input_file = "nlp_corpus/khamyang_en_hi_daily_part_001.jsonl"
with open(input_file, "r", encoding="utf-8") as f:
    sentences = []
    for i in range(500):
        line = f.readline()
        if not line:
            break
        sentences.append(json.loads(line))

print(f"Total loaded: {len(sentences)}")

# Check uniqueness of English and Hindi sentences
en_set = set(s['english'] for s in sentences)
hi_set = set(s['hindi'] for s in sentences)
tai_set = set(s['khamyang_tai'] for s in sentences)
print(f"Unique English: {len(en_set)}")
print(f"Unique Hindi: {len(hi_set)}")
print(f"Unique Khamyang Tai: {len(tai_set)}")

# Print 20 diverse samples from different positions
step = len(sentences) // 20
for i in range(0, len(sentences), step):
    s = sentences[i]
    print(f"[{i+1}] {s['domain']} | {s['khamyang_roman']}")
    print(f"    Tai:     {s['khamyang_tai']}")
    print(f"    English: {s['english']}")
    print(f"    Hindi:   {s['hindi']}")
    print()
