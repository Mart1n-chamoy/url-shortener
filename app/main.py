from fastapi import FastAPI

app = FastAPI(
    title="URL Shortener API",
    description="API para acortar URLs",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "URL Shortener API funcionando 🚀"}