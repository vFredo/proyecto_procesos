from typing import Optional
from enum import Enum
from pydantic import BaseModel

class EstadoEnum(str, Enum):
    activo = "activo"
    inactivo = "inactivo"

class TipoDispositivoEnum(str, Enum):
    dron = "dron"
    robot = "robot"

class Dispositivo(BaseModel):
    tipo_dispositivo: TipoDispositivoEnum
    color: str
    modelo: str
    marca: str
    nivel_bateria: int
    estado: EstadoEnum
