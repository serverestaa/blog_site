from fastapi import APIRouter, Depends
from database import db_post
from database.database import get_db
from routers.schemas import PostBase, PostDisplay
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('')
def create(request: PostBase, db: Session = Depends(get_db())):
    return db_post.create(db, request)
