from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas, models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()

    return blogs


def get(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not found",
        )

    return blog


def create(
    blog: schemas.Blog,
    current_user: schemas.User,
    db: Session
) -> models.Blog:
    user = (
        db.query(models.User)
        .filter(models.User.email == current_user.email).first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the email {current_user.email} is not found",
        )
    else:
        new_blog = models.Blog(
            title=blog.title,
            body=blog.body,
            user_id=user.id,
        )
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)

        return new_blog


def destroy(id: int, db: Session):
    blog_qs = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog_qs.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not found",
        )
    else:
        blog_qs.delete(synchronize_session=False)

    db.commit()


def update(id: int, blog: schemas.Blog, db: Session):
    blog_qs = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog_qs.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not found",
        )
    else:
        blog_qs.update(blog.dict())

    db.commit()