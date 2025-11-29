from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine=create_engine('postgresql://neondb_owner:npg_aEAvjDXMk0e4@ep-tight-sky-a89qm5c1-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require')
session_local=sessionmaker(autoflush=False,autocommit=False,bind=engine)