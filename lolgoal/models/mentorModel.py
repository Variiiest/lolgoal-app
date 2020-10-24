from .meta import Base
from sqlalchemy import Column, Integer, Boolean, DateTime, String
from sqlalchemy.orm import relationship
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class Mentor(Base):
    """ Mentors Model for storing Mentor related details """
    __tablename__ = "mentor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(100), nullable=False)

    varified = Column(Boolean, nullable=False, default=False)
    admin = Column(Boolean, nullable=False, default=False)

    registered_on = Column(DateTime, nullable=False)
    last_updated_on = Column(DateTime, nullable=False)

    # Relationship begins here
    project = relationship("project", secondary = "link")

    
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
        return "<Mentors '{}'>".format(self.username)
    