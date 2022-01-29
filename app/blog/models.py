from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    body = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id}, title={self.title})>"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

    blogs = relationship("Blog", back_populates="creator")

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id}, name={self.name})>"