from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres.ykrmemoqdxuwljqnbbcy:IW4Jq2jHJruL9g5Z@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"  # Use SQLite for simplicity

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
