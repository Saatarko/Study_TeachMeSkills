import sys

# Добавление пути к каталогу приложения в PYTHONPATH
path = '/home/Saatarko/site/Flask'
if path not in sys.path:
    sys.path.append(path)

from Flask.database import app as application
