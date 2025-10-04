from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.services.gemini_service import GeminiService
from app.services.latex_ocr_service import LaTeXOCRService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

gemini = GeminiService()
latex_ocr = LaTeXOCRService()

class MistakeRequest(BaseModel):
    note: str

class TranslateRequest(BaseModel):
    text: str
    target_lang: str

class LatexRequest(BaseModel):
    expr: str

class CardsRequest(BaseModel):
    note: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Bingle Bongle backend!"}

@app.post("/api/mistakes")
def api_mistakes(req: MistakeRequest):
    result = gemini.analyze_mistakes(req.note)
    return JSONResponse(content=result)

@app.post("/api/translate")
def api_translate(req: TranslateRequest):
    result = gemini.translate_with_explain(req.text, req.target_lang)
    return JSONResponse(content=result)

@app.post("/api/latex")
def api_latex(req: LatexRequest):
    result = gemini.image_to_latex(req.expr)
    return JSONResponse(content=result)

@app.post("/api/cards")
def api_cards(req: CardsRequest):
    result = gemini.make_cards(req.note)
    return JSONResponse(content=result)