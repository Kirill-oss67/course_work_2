import pytest
from run import app
from utils import get_posts_all


def test_posts():
    response = app.test_client().get('/GET/api/posts')
    assert type(response.json) == list

def test_keys():
    response = app.test_client().get('/GET/api/posts')
    list_keys = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    test_data = response.json
    test_post = test_data[0]
    assert set(test_post.keys()) == set(list_keys)


