import os
import json
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

MODEL = "models/gemini-2.5-flash"

MISTAKE_SCHEMA = {
  "type": "object",
  "properties": {
    "mistakes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "span": {"type": "string"},
          "type": {"type": "string"},
          "fix": {"type": "string"},
          "severity": {"type": "integer"}   # ← 去掉 minimum / maximum
        },
        "required": ["span", "fix", "severity"]
      }
    }
  },
  "required": ["mistakes"]
}

def analyze_mistakes(note_text: str):
  model = genai.GenerativeModel(MODEL)
  resp = model.generate_content(
    note_text,
    generation_config={
      "response_mime_type": "application/json",
      "response_schema": MISTAKE_SCHEMA
    }
  )
  return json.loads(resp.text)


# ---------- Feature ②: Translate + Plain English ----------
import json as _json  # 防止上面没有导入json时出错；若已有import json也没关系

TRANSLATE_SCHEMA = {
  "type": "object",
  "properties": {
    "translation": {"type": "string"},
    "plain_en": {"type": "string"},
    "examples": {"type": "array", "items": {"type": "string"}}
  },
  "required": ["translation", "plain_en"]
}

def translate_with_explain(text: str, target_lang: str):
    """
    Translate text into target_lang (e.g., 'zh-CN' or 'en'),
    and explain key terms in Plain English with 1–2 examples.
    Returns a dict per TRANSLATE_SCHEMA.
    """
    model = genai.GenerativeModel(MODEL)
    prompt = (
      "You are a bilingual teaching assistant. "
      "Translate between English and Simplified Chinese as requested. "
      "Also explain key terms in CEFR-B1 Plain English and include 1–2 concrete usage examples.\n\n"
      f"Target language: {target_lang}\n"
      f"Text:\n{text}\n\n"
      "Return ONLY valid JSON per schema."
    )
    resp = model.generate_content(
        prompt,
        generation_config={
            "response_mime_type": "application/json",
            "response_schema": TRANSLATE_SCHEMA
        }
    )
    return _json.loads(resp.text)

def translate_with_explain(text: str, target_lang: str):
    """
    Translate text into target_lang (e.g., 'zh-CN' or 'en'),
    and explain key terms in Plain English with 1–2 examples.
    Returns a dict per TRANSLATE_SCHEMA.
    """
    model = genai.GenerativeModel(MODEL)
    prompt = (
      "You are a bilingual teaching assistant. "
      "Translate between English and Simplified Chinese as requested. "
      "Also explain key terms in CEFR-B1 Plain English and include 1–2 concrete usage examples.\n"
      "Use CEFR-B1 vocabulary; keep plain_en ≤ 2 sentences.\n"
      "Return at most 2 examples, each ≤ 1 sentence.\n\n"
      f"Target language: {target_lang}\n"
      f"Text:\n{text}\n\n"
      "Return ONLY valid JSON per schema."
    )
    resp = model.generate_content(
        prompt,
        generation_config={
            "response_mime_type": "application/json",
            "response_schema": TRANSLATE_SCHEMA
        }
    )
    return json.loads(resp.text)

# ---------- Feature ④: Make study cards (Anki/Quizlet) ----------
import json as _json  # 若上面已 import json 也不会冲突

CARDS_SCHEMA = {
  "type": "object",
  "properties": {
    "cards": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "term": {"type": "string"},
          "definition": {"type": "string"}
        },
        "required": ["term", "definition"]
      }
    }
  },
  "required": ["cards"]
}

def card_graphics(term: str):
    # Returns a dict with icon and color for a given term
    if any(x in term.lower() for x in ["limit", "integral", "derivative", "sum"]):
        return {"icon": "📐", "color": "#3b82f6"}
    if any(x in term.lower() for x in ["language", "translate", "word"]):
        return {"icon": "🌐", "color": "#22c55e"}
    return {"icon": "📝", "color": "#f59e42"}

def make_cards(note_text: str, limit: int=10):
    model = genai.GenerativeModel(MODEL)
    prompt = (
      f"Create up to {limit} concise term-definition pairs from the note below.\n"
      "Each definition ≤ 2 sentences, concrete, self-contained.\n"
      "Return ONLY valid JSON per schema.\n\n"
      f"{note_text}"
    )
    resp = model.generate_content(
        prompt,
        generation_config={
            "response_mime_type": "application/json",
            "response_schema": CARDS_SCHEMA
        }
    )
    cards = _json.loads(resp.text)
    # Add icon/color for each card
    for c in cards.get("cards", []):
        c.update(card_graphics(c.get("term", "")))
    return cards

def to_anki_tsv(cards_json: dict) -> str:
    # Add icon as first column
    return "\n".join(
        f"{c.get('icon','')}\t{c.get('term','')}\t{c.get('definition','')}"
        for c in cards_json.get("cards", [])
    )

# ---------- Feature ③: Convert handwritten math to LaTeX ----------
import json as _json  # 若上面已 import json 也无冲突

LATEX_SCHEMA = {
  "type": "object",
  "properties": {
    "latex": {"type": "string"},
    "description": {"type": "string"}
  },
  "required": ["latex"]
}

def image_to_latex(math_text: str):
    """
    Convert a handwritten or plain math expression into LaTeX code.
    If the input is already typed, just standardize it.
    Returns: dict with 'latex' and optional 'description'.
    """
    model = genai.GenerativeModel(MODEL)
    prompt = (
      "You are a math notation assistant. "
      "Given a handwritten or plain text math expression, convert it into valid LaTeX syntax. "
      "Keep it minimal (no extra spaces), and escape LaTeX properly. "
      "Also include a short plain English description of what the expression means.\n\n"
      f"Expression:\n{math_text}\n\n"
      "Return ONLY JSON per schema."
    )
    resp = model.generate_content(
        prompt,
        generation_config={
            "response_mime_type": "application/json",
            "response_schema": LATEX_SCHEMA
        }
    )
    return _json.loads(resp.text)



# ========== Elaborate Based on Tone ==========

PROMPT_ELABORATE_TONE = """
You are EchoClass. Elaborate the idea for ESL students in {audience} with the requested tone.
Requirements:
- Tone: {tone}
- Length: {length_hint}
- Level: CEFR A2–B1 (plain, concrete English)
- Be inclusive and non-judgmental.
- Avoid jargon unless explained.
Return only the rewritten text (no preface).
Original:
{original}
""".strip()

def elaborate_note(
    text: str,
    tone: str = "friendly and encouraging",
    audience: str = "undergraduate students",
    length: str = "short",
    use_model: bool = True,
    model_name: str | None = None,
    temperature: float = 0.4,
) -> str:
    """
    Expand the note with a specific tone and audience.
    length ∈ {"very short","short","medium","long"}.
    """
    original = (text or "").strip()
    if not original:
        return ""

    length_map = {
        "very short": "2–3 sentences",
        "short": "4–6 sentences",
        "medium": "1–2 paragraphs",
        "long": "2–3 paragraphs",
    }
    length_hint = length_map.get(length, "4–6 sentences")

    if not use_model:
        # 简单回退规则
        base = original.rstrip(".")
        return f"{base}. In simple words, {base.lower()}. This version is {tone} for {audience}."

    import os
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    model_name = model_name or os.getenv("ECHOCLASS_MODEL", "gemini-1.5-flash")
    try:
        import google.generativeai as genai
        if not api_key:
            raise RuntimeError("No API key")
        genai.configure(api_key=api_key)
        prompt = PROMPT_ELABORATE_TONE.format(
            audience=audience, tone=tone, length_hint=length_hint, original=original
        )
        resp = genai.GenerativeModel(model_name).generate_content(
            prompt, generation_config={"temperature": float(temperature), "top_p": 0.9, "top_k": 40}
        )
        return (getattr(resp, "text", "") or "").strip()
    except Exception:
        base = original.rstrip(".")
        return f"{base}. In simple words, {base.lower()}. This version is {tone} for {audience}."


# ========== Local Source Retrieval (TF-IDF over docs/) ==========

from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Optional
import re

@dataclass
class RetrievedDoc:
    path: str
    title: str
    snippet: str
    score: float

def _read_text_file(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return p.read_text(errors="ignore")

def _read_pdf_file(p: Path) -> str:
    try:
        import pypdf
        reader = pypdf.PdfReader(str(p))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception:
        return ""

def _make_title(p: Path) -> str:
    return p.stem.replace("_"," ").replace("-"," ").title()

def _make_snippet(text: str, query: str, max_len: int = 200) -> str:
    q = re.escape(query.split()[0]) if query.strip() else ""
    if q:
        m = re.search(q, text, flags=re.I)
        if m:
            i = max(0, m.start() - 80)
            return (text[i:i+max_len].replace("\n", " ")).strip()
    return (text[:max_len].replace("\n", " ")).strip()

def retrieve_sources(
    query: str,
    root: str | Path = "docs",
    patterns: tuple = ("*.md","*.txt","*.pdf"),
    top_k: int = 3,
) -> List[Dict]:
    """
    Simple local retrieval over docs/ using TF-IDF cosine similarity.
    Returns: [{"path","title","snippet","score"}]
    """
    root = Path(root)
    files = []
    for pat in patterns:
        files.extend(root.rglob(pat))
    if not files:
        return []

    corpus = []
    texts = []
    for p in files:
        if p.suffix.lower() == ".pdf":
            txt = _read_pdf_file(p)
        else:
            txt = _read_text_file(p)
        txt = (txt or "").strip()
        if not txt:
            continue
        corpus.append(p)
        texts.append(txt)

    if not texts:
        return []

    # TF-IDF
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        vect = TfidfVectorizer(max_features=5000, ngram_range=(1,2), stop_words="english")
        X = vect.fit_transform(texts)
        qv = vect.transform([query])
        sims = cosine_similarity(qv, X).ravel()
        idxs = sims.argsort()[::-1][:top_k]
    except Exception:
        # 退化为关键词计数
        sims = [sum(txt.lower().count(w) for w in query.lower().split()) for txt in texts]
        idxs = sorted(range(len(sims)), key=lambda i: sims[i], reverse=True)[:top_k]

    out: List[Dict] = []
    for i in idxs:
        p = corpus[i]
        t = texts[i]
        score = float(sims[i])
        out.append({
            "path": str(p),
            "title": _make_title(p),
            "snippet": _make_snippet(t, query),
            "score": round(score, 4),
        })
    return out


PROMPT_ANSWER_WITH_SOURCES = """
You are EchoClass. Answer the user's question using ONLY the provided sources.
Write for ESL students (CEFR A2–B1). Be concise and concrete.
Insert inline citations like [1], [2] matching the numbered SOURCES.
If a fact isn't in sources, say you don't have that info.

QUESTION:
{question}

SOURCES:
{sources_block}

FORMAT:
Answer first (2–6 sentences), then a line "References: [1], [2]".
""".strip()

def answer_with_sources(
    question: str,
    root: str | Path = "docs",
    top_k: int = 3,
    use_model: bool = True,
    model_name: str | None = None,
    temperature: float = 0.2,
) -> Dict[str, object]:
    """
    Retrieves local sources then (optionally) asks Gemini to write an answer with [n] citations.
    Returns: {"answer": str, "sources": list[dict]}
    """
    hits = retrieve_sources(question, root=root, top_k=top_k)
    if not use_model or not hits:
        # 没模型或没命中时，仅返回命中列表
        return {"answer": "", "sources": hits}

    import os
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    model_name = model_name or os.getenv("ECHOCLASS_MODEL", "gemini-1.5-flash")
    try:
        import google.generativeai as genai
        if not api_key:
            raise RuntimeError("No API key")
        genai.configure(api_key=api_key)
        # 组装 sources_block
        lines = []
        for i, h in enumerate(hits, start=1):
            lines.append(f"[{i}] {h['title']} — {h['snippet']}")
        sources_block = "\n".join(lines)
        prompt = PROMPT_ANSWER_WITH_SOURCES.format(question=question, sources_block=sources_block)
        resp = genai.GenerativeModel(model_name).generate_content(
            prompt, generation_config={"temperature": float(temperature), "top_p": 0.9, "top_k": 40}
        )
        answer = (getattr(resp, "text", "") or "").strip()
        return {"answer": answer, "sources": hits}
    except Exception:
        return {"answer": "", "sources": hits}
