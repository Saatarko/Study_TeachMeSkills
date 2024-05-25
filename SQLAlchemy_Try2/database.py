from sqlalchemy import String, create_engine, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from config import settings


sync_engine = create_engine(   # соаздает движек для подключения
    url=settings.database_url_psycopg,    # грузим собранную сторку для соединения с базой
    echo=False,      # Выводит логи транзщаций
)

# sync_engine = create_engine('sqlite+pysqlite:///:memory:,')   # заготовка для случая отсуствия постгреса

session_factory = sessionmaker(sync_engine)   # Объявляем сессию



