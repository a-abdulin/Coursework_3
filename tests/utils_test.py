import pytest

from ..utils import get_posts_all, get_posts_by_user, search_for_posts, get_post_by_pk


def test_get_posts_all():
    posts = get_posts_all()
    assert posts != [], "Данные постов не найдены"

def test_get_posts_by_user_1():
    post = get_posts_by_user("leo")
    assert post.pk == 1, "Данные пользователя не найдены"

def test_get_posts_by_user_2():
    with pytest.raises(ValueError):
        get_posts_by_user("Valentino")

def test_search_for_posts():
    posts_by_query = search_for_posts("ржавые елки")
    assert posts_by_query != [], "Не работает поиск"

def test_get_post_by_pk():
    posts_by_pk = get_post_by_pk("1")
    assert posts_by_pk != None, 'Не работает подбор по str pk'
