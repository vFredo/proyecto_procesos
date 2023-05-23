from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from enum import Enum

class EstadoEntrega(str, Enum):
    completado = "completado"
    por_realizar = "por realizar"
    no_entregado = "no entregado"


class Solicitud(BaseModel):
    user_id: str
    fecha_domicilio: datetime
    hora_llegada: datetime
    hora_salida: datetime
    dispositivo_asociado: str
    peso_carga: float
    lugar_entrega: str
    estado_entrega: EstadoEntrega
