from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from .. import database, schemas, actions
from ..oauth2 import get_current_user

router = APIRouter(tags=["Blogs"], prefix="/blog")


@router.get("/", response_model=List[schemas.GetBlog])
def all(
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return actions.blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    blog: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return actions.blog.create(blog, current_user, db)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def destroy(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return actions.blog.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    blog: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return actions.blog.update(id, blog, db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.GetBlog,
)
def get(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return actions.blog.get(id, db)