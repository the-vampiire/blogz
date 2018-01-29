from sqlalchemy import create_engine, inspect
from app import db, DB_URI
from app.models.blog import Blog
from app.models.user import User

ENGINE = create_engine(DB_URI)
INSPECTOR = inspect(ENGINE) # used for checking if tables exist on startup

# check if tables exist - create if they do not
tables = INSPECTOR.get_table_names()
if not tables: db.create_all()