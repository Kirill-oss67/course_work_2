from flask import Flask

from app.index.views import index_blueprint

app = Flask(__name__)

app.register_blueprint(index_blueprint)
if __name__ == "__main__":
    app.run(debug=True, port=5100)
