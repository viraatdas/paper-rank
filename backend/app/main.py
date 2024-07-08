from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas, arxiv_fetcher
from .database import SessionLocal, engine

# Load environment variables from a .env file if it exists
load_dotenv()

# Determine the mode
debug_mode = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

if debug_mode:
    print("Running in Debug Mode")
else:
    print("Running in Production Mode")

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations as endpoints

@app.post("/papers/", response_model=schemas.Paper)
def create_paper(paper: schemas.PaperCreate, db: Session = Depends(get_db)):
    db_paper = crud.get_paper_by_arxiv_id(db, paper.arxiv_id)
    if db_paper:
        raise HTTPException(status_code=400, detail="Paper already exists")
    return crud.create_paper(db=db, paper=paper)

@app.get("/papers/", response_model=list[schemas.Paper])
def read_papers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    papers = crud.get_papers(db, skip=skip, limit=limit)
    return papers

@app.get("/papers/top/", response_model=list[schemas.Paper])
def read_top_papers(limit: int = 10, db: Session = Depends(get_db)):
    papers = crud.get_top_papers(db, limit=limit)
    return papers

@app.get("/papers/{paper_id}", response_model=schemas.Paper)
def read_paper(paper_id: int, db: Session = Depends(get_db)):
    db_paper = crud.get_paper(db, paper_id=paper_id)
    if db_paper is None:
        raise HTTPException(status_code=404, detail="Paper not found")
    return db_paper

@app.post("/papers/{paper_id}/vote/", response_model=schemas.Paper)
def vote_paper(paper_id: int, db: Session = Depends(get_db)):
    paper = crud.vote_paper(db, paper_id=paper_id)
    if paper is None:
        raise HTTPException(status_code=404, detail="Paper not found")
    return paper

@app.post("/papers/{paper_id}/comment/", response_model=schemas.Comment)
def create_comment(paper_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_paper = crud.get_paper(db, paper_id=paper_id)
    if db_paper is None:
        raise HTTPException(status_code=404, detail="Paper not found")
    return crud.create_comment(db=db, paper_id=paper_id, comment=comment)

@app.post("/papers/search/", response_model=list[schemas.Paper])
def search_papers(query: str, db: Session = Depends(get_db)):
    papers = arxiv_fetcher.fetch_papers(query=query)
    return papers
