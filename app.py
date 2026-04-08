from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import TextSummarizer
from utils import extract_keywords

app = FastAPI(title="AI Smart Summarizer")

summarizer = TextSummarizer()

class RequestData(BaseModel):
    text: str
    max_length: int = 120
    min_length: int = 30
    tone: str = "formal"
    format: str = "paragraph"

@app.post("/summarize")
def summarize_text(data: RequestData):
    if data.format == "bullet":
        summary = summarizer.bullet_summary(data.text)
    else:
        summary = summarizer.summarize(
            data.text,
            data.max_length,
            data.min_length,
            data.tone
        )

    keywords = extract_keywords(data.text)

    return {
        "summary": summary,
        "keywords": keywords
    }
