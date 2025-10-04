import time, json
from ai.promptKit import analyze_mistakes, translate_with_explain, image_to_latex, make_cards

def check(required, obj):
    return isinstance(obj, dict) and all(k in obj for k in required)

def run():
    t0 = time.time()
    total = passed = 0

    tests = {
        "mistakes": ["The limt of sin(x)/x as x->0 is 0"],
        "translate": [("闭区间上的连续函数一定能取到最大最小值", "en")],
        "latex": ["integral from 0 to infinity of e^(-x^2) dx"],
        "cards": ["Limit, continuity, differentiability, L'Hôpital, Taylor expansion"]
    }

    for note in tests["mistakes"]:
        total += 1
        r = analyze_mistakes(note)
        ok = "mistakes" in r
        print("Mistakes:", "✅" if ok else "❌", json.dumps(r)[:120])
        passed += 1 if ok else 0

    for text, lang in tests["translate"]:
        total += 1
        r = translate_with_explain(text, lang)
        ok = check(["translation", "plain_en"], r)
        print("Translate:", "✅" if ok else "❌", json.dumps(r, ensure_ascii=False)[:120])
        passed += 1 if ok else 0

    for expr in tests["latex"]:
        total += 1
        r = image_to_latex(expr)
        ok = check(["latex"], r)
        print("LaTeX:", "✅" if ok else "❌", json.dumps(r, ensure_ascii=False)[:120])
        passed += 1 if ok else 0

    for note in tests["cards"]:
        total += 1
        r = make_cards(note)
        ok = "cards" in r and isinstance(r["cards"], list)
        print("Cards:", "✅" if ok else "❌", len(r.get("cards", [])))
        passed += 1 if ok else 0

    print(f"\nSummary: {passed}/{total} tests passed | {time.time()-t0:.1f}s elapsed")

if __name__ == "__main__":
    run()
