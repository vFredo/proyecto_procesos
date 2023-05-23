from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Notificacion(BaseModel):
    id_domicilio: str
    fecha: datetime
    mensaje: str

