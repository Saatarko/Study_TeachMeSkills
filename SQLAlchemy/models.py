from __future__ import annotations

import datetime

from typing import Annotated

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

intpkey = Annotated[int, mapped_column(primary_key=True)]  # Аннотируем главный ключ (primary key)


class ClientsORM(Base):              # деклараруем создание новой базы клиентов
    __tablename__ = "clients"

    id: Mapped[intpkey]
    client_name: Mapped[str]
    client_phone: Mapped[int]


class PetsORM(Base):                 # деклараруем создание новой базы питомцев
    __tablename__ = "pets"

    id_pets: Mapped[intpkey]
    pets_name: Mapped[str]
    pets_age: Mapped[int]
    pets_breed: Mapped[int | None]
    pets_creation_at: Mapped[datetime.datetime] = mapped_column(server_default=
                                                                func.now())
    client_id: Mapped[int] = mapped_column(ForeignKey('Clients.id',
                                                      ondelete='CASCADE'))
