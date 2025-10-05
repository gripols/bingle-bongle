import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from ai.promptKit import (
    analyze_mistakes, translate_with_explain, image_to_latex, make_cards
)

app = FastAPI(title="EchoClass Demo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

class NoteIn(BaseModel):
    note: str

class TranslateIn(BaseModel):
    text: str
    target_lang: str  # "zh-CN" or "en"

class LatexIn(BaseModel):
    expr: str

class CardsIn(BaseModel):
    note: str
    limit: int | None = 10

@app.post("/api/mistakes")
def api_mistakes(body: NoteIn):
    return analyze_mistakes(body.note)

@app.post("/api/translate")
def api_translate(body: TranslateIn):
    return translate_with_explain(body.text, body.target_lang)

@app.post("/api/latex")
def api_latex(body: LatexIn):
    return image_to_latex(body.expr)

@app.post("/api/cards")
def api_cards(body: CardsIn):
    limit = body.limit if body.limit else 10
    return make_cards(body.note, limit=limit)

# 静态托管前端
app.mount("/", StaticFiles(directory="web", html=True), name="web")
