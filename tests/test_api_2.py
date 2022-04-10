import pytest
from run import app
from utils import get_posts_all, get_post_by_pk


def test_posts():
    response = app.test_client().get('/api/posts/1')
    assert type(response.json) == dict

def test_keys():
    response = app.test_client().get('/api/posts/1')
    list_keys = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    test_data = response.json
    assert set(test_data.keys()) == set(list_keys)
