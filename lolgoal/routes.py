from flask import render_template, url_for, flash, redirect,request
from lolgoal.models import Project, Mentor, Student
from lolgoal import app
from flask_login import login_user, current_user, logout_user, login_required
from lolgoal.forms import RegisterStudent, LoginStudent, Project, SignUpMentor , LoginMentor, SubmitProject


#Index or Homepage
@app.route('/')
def home():
    return render_template('index.html')


#Project List Page
@app.route('/project')
def projectlist():
    return render_template('projectlist.html')


@app.route("/createproject", methods=['GET', 'POST'])
def createproject():
    form = SubmitProject()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('createpost.html', title='Post', form=form)

#Project Full Page
@app.route('/projectfull')
def projectfull():
    return render_template('projectfull.html')


#Meetings Page 
@app.route('/meetings')
def meetings():
    return render_template('meetings.html')


#StartUp Page
@app.route('/startup')
def startup():
    return render_template('startup.html')









#---------------------------------------------------------------------------------------
#SignUp Page for student
@app.route("/signup", methods=['GET', 'POST'])

def register():
    if current_user.is_authenticated:
        return redirect(url_for(home))
    form = RegisterStudent()
    if form.validate_on_submit():
        user= Student(username=form.username.data,email= form.email.data,password_hash= form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for(home))
    return render_template('studentsignup.html', title='Register', form=form)



#---------------------------------------------------------------------------------------
#Login Page for student
@app.route("/login", methods=['GET', 'POST'])

def login():
    form = LoginStudent()
    if form.validate_on_submit():
        if form.email.data =='admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for(home))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('studentlogin.html', title='Login', form=form)


#---------------------------------------------------------------------------------------

#SignUp Page for Mentor
@app.route("/mentorsignup", methods=['GET', 'POST'])

def mentorsignup():
    form = SignUpMentor()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for(home))
    return render_template('mentorsignup.html', title='Register', form=form)


#---------------------------------------------------------------------------------------

#Login Page for Mentor
@app.route("/mentorlogin", methods=['GET', 'POST'])

def mentorlogin():
    form = LoginMentor()
    if form.validate_on_submit():
        if form.email.data =='admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for(home))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('mentorlogin.html', title='Login', form=form)


#--------------------------------------------------------------------------------------


#YourWork
@app.route('/yourwork')
def yourwork():
    return render_template('yourwork.html')

   





#---------------------------------------------------------------------------------------
#Error Page





@app.errorhandler(404)
def error_html(error):
        return render_template('error.html'), 404

