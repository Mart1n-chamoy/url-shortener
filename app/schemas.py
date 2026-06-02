from pydantic import BaseModel, HttpUrl
from typing import Optional

class URLCreate(BaseModel):
    url: HttpUrl
    custom_code: Optional[str] = None