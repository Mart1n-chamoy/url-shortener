# URL Shortener API

Proyecto desarrollado con FastAPI para generar URLs cortas.

<img width="739" height="397" alt="image" src="https://github.com/user-attachments/assets/bcd3b26a-ea23-4652-b37d-1d36cee8bb1c" />


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


