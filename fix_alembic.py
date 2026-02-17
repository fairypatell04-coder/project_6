from services.app.db.session import engine
from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS alembic_version"))
    conn.commit()

print("✅ alembic_version table dropped")
