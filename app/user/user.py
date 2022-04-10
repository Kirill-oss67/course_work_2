from flask import Blueprint, render_template, request
from utils import get_posts_by_user

user_blueprint = Blueprint('user_blueprint', __name__, template_folder="templates")


@user_blueprint.route('/posts/<username>')
def users(username):
    users_posts = get_posts_by_user(username)
    user_name = users_posts[0]["poster_name"]
    return render_template('user-feed.html', users_posts=users_posts, user_name=user_name)
