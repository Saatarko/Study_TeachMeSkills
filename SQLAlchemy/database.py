from sqlalchemy import String, create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from config import settings


sync_engine = create_engine(   # соаздает движек для подключения
    url=settings.database_url_psycopg,    # грузим собранную сторку для соединения с базой
    echo=False,      # Выводит логи транзщаций
)

session_factory = sessionmaker(sync_engine)   # Объявляем сессию


class Base(DeclarativeBase):
    pass

    repr_cols_num  = 3            # для каждой таблицы отдельно
    repr_cols = tuple()          # для каждой таблицы отдельно
    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f'{col} = {getattr(self, col)}')
                temp= ','.join(cols)
        return (f'<{self.__class__.__name__}{temp}>')



