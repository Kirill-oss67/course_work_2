from flask import Flask, jsonify
from utils import get_posts_all, get_post_by_pk
from app.index.views import index_blueprint
from app.search.search import search_blueprint
from app.user.user import user_blueprint

app = Flask(__name__)

app.register_blueprint(index_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_blueprint)


@app.route("/GET/api/posts")
def api_1():
    data = get_posts_all()
    return jsonify(data)


@app.route("/GET/api/posts/<int:post_id>")
def api_2(post_id):
    post = get_post_by_pk(post_id)
    return jsonify(post)


if __name__ == "__main__":
    app.run(debug=True, port=5100)
