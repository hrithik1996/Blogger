from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import current_user
from app.models import Post

main = Blueprint('main',__name__)

@main.route('/')
def home():
    if current_user.is_authenticated:
        page= request.args.get('page', 1 , type=int)
        posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
        return render_template('home.html',posts=posts)
    else:
        flash(f'Please login first ','danger')
        return redirect(url_for('users.login'))
    

@main.route('/about')
def about():
    return render_template('about.html',title='About')
