from .meta import Base
from .mentorModel import Mentor
from .projectModel import Project, MPlink
from .studentModel import Student, SPlink
from lolgoal import db, login_manager

from flask_login import UserMixin

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

@login_manager.user_loader
def load_student(id):
    return Student.query.get(int(id))
