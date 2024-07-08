import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()

# Determine the mode
debug_mode = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

# Set the DATABASE_URL based on the mode
if debug_mode:
    db_path = os.path.join(os.path.dirname(__file__), '../db/local_test.db')
    DATABASE_URL = f"sqlite:///{os.path.abspath(db_path)}"
    print("Running in Debug Mode")
else:
    db_path = os.path.join(os.path.dirname(__file__), '../db/local_test.db')  # Update this for production as needed
    DATABASE_URL = f"sqlite:///{os.path.abspath(db_path)}"
    print("Running in Production Mode")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
