import pytest

from main import app


def test_app_posts():
    response = app.test_client().get('/api/posts')
    posts = response.json

    assert response.status_code == 200
    assert type(posts) is list
    assert posts[0].get("poster_name") == "leo"

def test_app_post_by_pk():
    response = app.test_client().get('/api/posts/1')
    post = response.json
    assert response.status_code == 200
    assert type(post) is dict
    assert post.get("poster_name") == "leo"
