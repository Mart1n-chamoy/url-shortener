from fastapi import FastAPI
from app.database import engine, Base
from app.schemas import URLCreate

app = FastAPI(
    title="URL Shortener API",
    description="API para acortar URLs",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "URL Shortener API funcionando 🚀"}


@app.post("/shorten")
def shorten_url(url_data: URLCreate):
    return {
        "url_recibida": url_data.url
    }
    