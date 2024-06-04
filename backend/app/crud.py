from sqlalchemy.orm import Session
from . import models, schemas

def get_paper(db: Session, paper_id: int):
    return db.query(models.Paper).filter(models.Paper.id == paper_id).first()

def get_papers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Paper).offset(skip).limit(limit).all()

def create_paper(db: Session, paper: schemas.PaperCreate):
    db_paper = models.Paper(**paper.dict())
    db.add(db_paper)
    db.commit()
    db.refresh(db_paper)
    return db_paper

def get_top_papers(db: Session, limit: int = 10):
    return db.query(models.Paper).order_by(models.Paper.votes.desc()).limit(limit).all()

def vote_paper(db: Session, paper_id: int):
    paper = db.query(models.Paper).filter(models.Paper.id == paper_id).first()
    if paper:
        paper.votes += 1
        db.commit()
        db.refresh(paper)
        return paper
    return None

def create_comment(db: Session, paper_id: int, comment: schemas.CommentCreate):
    db_comment = models.Comment(paper_id=paper_id, content=comment.content)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
