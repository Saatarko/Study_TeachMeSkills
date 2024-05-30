from flask_bootstrap import Bootstrap
from sqlalchemy import String, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
import sqlite3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config import settings, Config

# sync_engine = settings.database_url_psycopg

sync_engine = "sqlite:///my.db"  # заготовка для случая отсуствия постгреса

# session_factory = sessionmaker(sync_engine)  # Объявляем сессию

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = sync_engine
app.config.from_object(Config)
# app.app_context().push()
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


