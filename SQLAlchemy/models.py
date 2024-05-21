import datetime
import enum

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class ClientsORM(Base):
    __tablename__ = "Clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_name: Mapped[str]

