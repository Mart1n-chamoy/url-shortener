from fastapi import FastAPI
from app.database import engine, Base
from app.schemas import URLCreate
import random
import string
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database import get_db
from app.models import URL

from fastapi.responses import RedirectResponse
from fastapi import HTTPException


app = FastAPI(
    title="URL Shortener API",
    description="API para acortar URLs",
    version="1.0.0"
)

from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="app/templates")

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/shorten")
def shorten_url(url_data: URLCreate, db: Session = Depends(get_db)):

    short_code = (
    url_data.custom_code
    if url_data.custom_code
    else generate_short_code()

    )
    
    existing = db.query(URL).filter(
        URL.short_code == short_code
    ).first()

    if existing:
        raise HTTPException(
        status_code=400,
        detail="El código ya existe"
        )
    

    new_url = URL(
        original_url=str(url_data.url),
        short_code=short_code
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {
        "original_url": new_url.original_url,
        "short_code": new_url.short_code
    }

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):

    url = db.query(URL).filter(
        URL.short_code == short_code
    ).first()

    if not url:
        raise HTTPException(
            status_code=404,
            detail="URL no encontrada"
)

    url.clicks += 1
    db.commit()

    return RedirectResponse(url=url.original_url)    

@app.get("/stats/{short_code}")
def get_stats(short_code: str, db: Session = Depends(get_db)):

    url = db.query(URL).filter(
        URL.short_code == short_code
    ).first()

    if not url:
        raise HTTPException(
            status_code=404,
            detail="URL no encontrada"
        )

    return {
        "original_url": url.original_url,
        "short_code": url.short_code,
        "clicks": url.clicks
    }

