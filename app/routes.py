from flask import render_template, flash, redirect, request, url_for
from app import db, app
from app.models import User
from app.forms import NameInputForm, DeleteDatabaseForm, LetterForm

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def name_form():
    name_form = NameInputForm()
    delete_data_form = DeleteDatabaseForm()
    letter_form = LetterForm()
    letter = request.form.get('letter', None)
    print(request.form)
    print("xxxx", letter)
    if letter:
        print(letter)
        users = User.query.filter(User.username.like(letter + '%')).all()
    else:
        users = User.query.all()
    if request.form.get('submit_name'):
        flash('Added to database {}'.format(name_form.username.data))
        u = User(username=name_form.username.data)
        db.session.add(u)
        db.session.commit()
        return redirect('/')
    elif request.form.get('submit_delete'):
        flash(f'Database deleted')
        users = User.query.all()
        for u in users:
            db.session.delete(u)
        db.session.commit()
        return redirect('/')
    return render_template('name_input.html', title="Name", form=name_form, delete_button=delete_data_form, users=users,
                       letter_form=letter_form)


