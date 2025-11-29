from sqlalchemy import create_engine, text

# Database URL
DATABASE_URL = "postgresql://neondb_owner:npg_X2bkn7WgLdmv@ep-rough-cell-a8byg7ew-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require"

# Create engine
engine = create_engine(DATABASE_URL)

try:
    # Delete the alembic_version table content
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM alembic_version"))
        conn.commit()
        print("Successfully reset alembic_version table")
except Exception as e:
    print(f"Error: {e}")
    # If table doesn't exist, create it
    try:
        with engine.connect() as conn:
            conn.execute(text("CREATE TABLE IF NOT EXISTS alembic_version (version_num VARCHAR(32) NOT NULL)"))
            conn.commit()
            print("Created alembic_version table")
    except Exception as e2:
        print(f"Error creating table: {e2}") 