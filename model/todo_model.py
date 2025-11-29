from sqlalchemy import String, Integer, Boolean, Column, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

class user(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, nullable=False,unique=True)
    password = Column(String, nullable=True)


class Todo(Base):
    __tablename__ = "todo3"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'),nullable=False)
    # users=relationship('user',back_populates="todo")