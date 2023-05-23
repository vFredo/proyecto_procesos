from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Anotacion(BaseModel):
    id_dispositivo: str
    fecha: datetime
    anotacion: str
