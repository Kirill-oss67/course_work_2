from flask import Blueprint, render_template

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id

index_blueprint = Blueprint('index_blueprint', __name__, template_folder="templates")


@index_blueprint.route("/")
def index():
    list_data = get_posts_all()
    return render_template('index.html', content=list_data)


@index_blueprint.route("/posts/<int:post_id>")
def get_post(post_id):
    list_comments = get_comments_by_post_id(post_id)
    the_post = get_post_by_pk(post_id)
    len_list = len(list_comments)
    return render_template('post.html', post_info=the_post, list_comments=list_comments, len_list=len_list)
