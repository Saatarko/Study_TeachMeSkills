from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


from models import Servises,PetsORM

#
# class ClientsAddDTO(BaseModel):
#     client_name: str
#
#
# class ClientsDTO(ClientsAddDTO):
#     id: int
#
#
# class PetsAddDTO(BaseModel):
#     pets_name: str
#     pets_age: int
#     pets_breed: [Optional[str]]
#     client_id: int
#
#
# class PetsDTO(PetsAddDTO):
#     id: int
#
#
# class PetsServicesAddDTO(BaseModel):
#     services_name: Servises
#     services_cost: int
#     pets_id: int
#
#
# class PetsServicesDTO(PetsServicesAddDTO):
#     id: int
#     services_creation_at: datetime
#
#
# class ClientsRelDTO(ClientsDTO):
#     pets: List["PetsDTO"]
#
#
# class PetsRelDTO(PetsDTO):
#     clients: "ClientsDTO"
#     servise: "PetsServicesDTO"
#
#
# class PetsServicesRelDTO(PetsServicesDTO):
#     pets_s: "PetsORM"
