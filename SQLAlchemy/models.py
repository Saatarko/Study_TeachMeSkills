from __future__ import annotations

import datetime
from typing import Optional

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class ClientsORM(Base):              # деклараруем создание новой базы клиентов
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_name: Mapped[str]
    client_phone: Mapped[Optional[int]]


class PetsORM(Base):                 # деклараруем создание новой базы питомцев
    __tablename__ = "pets"

    id_pets: Mapped[int] = mapped_column(primary_key=True)
    pets_name: Mapped[str]
    pets_age: Mapped[int]
    pets_breed: Mapped[Optional[str]]
    pets_creation_at: Mapped[datetime.datetime] = mapped_column(server_default=
                                                                func.now())
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.id',
                                                      ondelete='CASCADE'))
