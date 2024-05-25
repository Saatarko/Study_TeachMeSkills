from __future__ import annotations

import datetime
import enum
from typing import Optional

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, Index, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class ClientsORM(Base):  # деклараруем создание новой базы клиентов
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_name: Mapped[str]
    client_phone: Mapped[Optional[int]]
    pets: Mapped["PetsORM"] = relationship(
        back_populates='clients',
        # primaryjoin = "and_(ClientsORM.id == PetsORM.client_id, PetsORM.breed == 'метис')"   # нужно для доп условий

    )    # создаем модели relationship

    repr_cols_num = 1  # для каждой таблицы отдельно
    repr_cols = tuple()  # для каждой таблицы отдельно


class PetsORM(Base):  # деклараруем создание новой базы питомцев
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)
    pets_name: Mapped[str]
    pets_age: Mapped[int]
    pets_breed: Mapped[Optional[str]]
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.id',
                                                      ondelete='CASCADE'))
    clients: Mapped["ClientsORM"] = relationship(
        back_populates='pets',    # указывает явную связь между моделями
    )

    servise: Mapped["PetsServicesORM"] = relationship(
        back_populates='pets_s',
    )

    repr_cols_num = 4  # для каждой таблицы отдельно
    repr_cols = tuple()  # для каждой таблицы отдельно

class Servises(enum.Enum):
    chipping = 'Чипирование'
    deworming = 'Дегельминтизация'
    ultrasound = 'УЗИ'
    x_ray = 'Рентген'
    preliminary_examination = 'Предварительный осмотр'
    sterilization = 'Стерилизация'
    operation = 'Операции'


class PetsServicesORM(Base):  # деклараруем создание новой базы услуг для питомцев
    __tablename__ = "pets-services"

    id: Mapped[int] = mapped_column(primary_key=True)
    services_name: Mapped[Servises]
    services_cost: Mapped[int]
    services_creation_at: Mapped[datetime.datetime] = mapped_column(server_default=
                                                                    func.now())
    pets_id: Mapped[int] = mapped_column(ForeignKey('pets.id',
                                                    ondelete='CASCADE'))
    pets_s: Mapped["PetsORM"] = relationship(
        back_populates='servise',

    )
    repr_cols_num = 3  # для каждой таблицы отдельно
    repr_cols = tuple()  # для каждой таблицы отдельно

    __table_agrs__ = (
        Index("services_name_index","services_name"),  # создание индекса
        CheckConstraint("services_cost > 0 ", name = "check_cost")  # предвариательная проверка данных
    )