from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text
from sqlalchemy.orm import aliased, contains_eager, joinedload, selectinload

from database import Base, sync_engine, session_factory
from models import ClientsORM


def create_tables():
    sync_engine.echo = False
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


def insert_tables():
    with session_factory() as session:
        client = ClientsORM(client_name='Сашко')
        client2 = ClientsORM(client_name='Екатерина')
        session.add_all([client, client2])
        session.commit()
