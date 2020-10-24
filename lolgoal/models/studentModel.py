from .meta import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Student(Base):
    """ Students Model for storing Students related details """
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username= Column(String(255),unique=True, nullable= False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(100), nullable=False)

    varified = Column(Boolean, nullable=False, default=False)

    registered_on = Column(DateTime, nullable=False)
    last_updated_on = Column(DateTime, nullable=False)

    # Relationship begins here
    mplink = relationship("mplink", secondary = "splink")

    
    @property
    def password(self):
        raise AttributeError('Password: write-only field')


    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password
        ).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


    def __repr__(self):
        return "<Students '{}'>".format(self.username)
    

class SPlink(Base):
    """ Link Model to relate many-to-many relation beetween student and MPlink """
    __tablename__ = "splink"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    mplink_id = Column(Integer, ForeignKey('mplink.id'), primary_key=True)