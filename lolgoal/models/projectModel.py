from .meta import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Interval
from sqlalchemy.orm import relationship


class Project(Base):
    """ Projects Model for storing Project related details """
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True)
    topic = Column(String(127), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    duration = Column(Interval)
    price = Column(Integer, nullable=False)
    added_on = Column(DateTime, nullable=False)

    # Relationship begins here
    mentor = relationship("mentor", secondary = "link")
    

class MPlink(Base):
    """ Link Model to relate many-to-many relation beetween mentor and project """
    __tablename__ = "mplink"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    mentor_id = Column(Integer, ForeignKey('mentor.id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'), primary_key=True)

    # Relationship begins here
    student = relationship("student", secondary = "splink")
