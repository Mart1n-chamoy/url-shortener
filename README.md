# URL Shortener API

Proyecto desarrollado con FastAPI para generar URLs cortas.

## Tecnologías
- Python
- FastAPI
- SQLite
- SQLAlchemy

## Ejecutar proyecto
Windows:
```bash
python -m venv venv
source venv/Scripts/activate
```
Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```
```bash
uvicorn app.main:app --reload
```
## Ejecutar con Docker

```bash
docker build -t url-shortener .
docker run -p 8000:8000 url-shortener
```

Abrir:

http://localhost:8000


