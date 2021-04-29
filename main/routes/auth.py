from flask			import render_template, redirect, request, flash
from flask_login    import login_required, current_user, login_user, logout_user

from main           import db

from main.models    import UserModel
from main.funcs 	import decorator

@decorator
def login(_):
    if current_user.is_authenticated:
        return redirect('/')
     
    if request.method == 'POST':
        email = request.form['email']
        user = UserModel.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            flash(f'Привет, {current_user.username}!', 'dark')
            return redirect('/')
        
        flash('Данные не верны или пользователь не зарегестрирован.', 'danger')
     
    return render_template('auth/login.html')

@decorator
def register(_):
    if current_user.is_authenticated:
        return redirect('/')
     
    if request.method == 'POST':
        email 	 = request.form['email']
        username = request.form['username']
        password = request.form['password']
 
        if UserModel.query.filter_by(email=email).first():
            flash('Такая почта уже зарегестрирована.', 'danger')
             
        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash('Пользователь зарегестрирован.', 'dark')
        return redirect('/login')

    return render_template('auth/register.html')

@decorator
def logout(_):
    logout_user()
    return redirect('/')