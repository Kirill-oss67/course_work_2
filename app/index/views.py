from flask import Blueprint, render_template

from utils import get_posts_all

index_blueprint = Blueprint('index_blueprint', __name__, template_folder="templates")

@index_blueprint.route("/")
def index():
    _data_ = get_posts_all()
    return render_template('index.html', content = _data_)

@index_blueprint.route("/posts/<postid>")
def post():
    pass