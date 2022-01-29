from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import database, schemas, actions

router = APIRouter(tags=["Users"], prefix="/user")


@router.post("/", response_model=schemas.GetUser)
def create_user(user: schemas.User, db: Session = Depends(database.get_db)):
    return actions.user.create(user, db)


@router.get("/", response_model=schemas.GetUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return actions.user.get(id, db)