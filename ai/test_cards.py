import json
from promptKit import make_cards, to_anki_tsv

note = "Limit definition, epsilon-delta, continuity, differentiability, L'Hôpital, Taylor expansion."
cards = make_cards(note, limit=8)
print(json.dumps(cards, indent=2, ensure_ascii=False))

print("\n--- Anki TSV ---\n")
tsv = to_anki_tsv(cards)
print(tsv)

# 可选：写入文件，方便前端或你导入 Anki
with open("anki_cards.tsv", "w", encoding="utf-8") as f:
    f.write(tsv)
print("\nSaved: anki_cards.tsv")
