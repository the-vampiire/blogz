from app import INSPECTOR, DB
from models.user import User
from models.blog import Blog

# check if tables exist - create if they do not
tables = INSPECTOR.get_table_names()
if not tables: DB.create_all()