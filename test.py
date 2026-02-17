from sqlalchemy import create_engine, inspect



DATABASE_URL = "postgresql+psycopg2://postgres:postgres123@localhost:5432/users_db"

engine = create_engine(DATABASE_URL)
inspector = inspect(engine)
print(inspector.get_table_names())
