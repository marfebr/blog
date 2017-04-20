from flask import render_template, Blueprint, redirect, request, flash,url_for
from flask_login import login_user,logout_user, login_required, login_manager

from wfdb.models import Movie, Actor, User, db
from wfdb.forms import LoginForm,RegisterForm

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main'
)


@main_blueprint.route("/")

def home():
    latest_movies = Movie.query.order_by(
        Movie.release_date.desc()
    ).limit(5).all()

    return render_template("index.html", latest_movies=latest_movies)

@main_blueprint.route("/actor/<int:actor_id>")
@login_required

def actor(actor_id):
    actor = Actor.query.get_or_404(actor_id)

    return render_template("actor.html", actor=actor)


@main_blueprint.route("/movie/<int:movie_id>")
def movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    return render_template("movie.html", movie=movie)


@main_blueprint.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()

        login_user(user)
        return redirect(request.args.get("next") or url_for("main.home"))
        flash("login success",category='success')
    return render_template("login.html",form=form)

@main_blueprint.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User()
        print(form.username.data)
        user.username = form.username.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Your user has be created please login",category='success')
        return redirect(request.args.get("next") or url_for("main.home"))
    
    return render_template("register.html",form=form)