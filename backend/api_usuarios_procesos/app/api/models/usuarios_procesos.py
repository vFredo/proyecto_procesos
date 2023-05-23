from typing import Optional
from pydantic import BaseModel

class Usuario(BaseModel):
    user: str
    password: str
    multas: Optional[int] = 0
    deuda: Optional[float] = 0.0

class Credentials(BaseModel):
    user: str
    password: str

class PasswordModel(BaseModel):
    password: str