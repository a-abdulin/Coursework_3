import requests
from flask import Blueprint, render_template, request

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user

# Создаем блупринт
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")
post_one_blueprint = Blueprint('post_one_blueprint', __name__, template_folder="templates")
search_post_blueprint = Blueprint('search_post_blueprint', __name__, template_folder="templates")
user_feed_blueprint = Blueprint('user_feed_blueprint', __name__, template_folder="templates")

# Создаем вьюшку для постов
@posts_blueprint.route('/')
def page_posts_all():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)

# Создаем вьюшку для одного поста с комментами
@post_one_blueprint.route('/posts/<postid>')
def page_post_one(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', post=post, comments=comments, comments_count=len(comments))

# Создаем вьюшку для поиска по тексту
@search_post_blueprint.route('/search')
def search_page():
    search__input = request.args.get('s')
    posts_by_query = search_for_posts(search__input)
    posts_count = 0
    if posts_by_query is not None:
        posts_count = len(posts_by_query)
    return render_template("search.html", hash=search__input, posts=posts_by_query, posts_count=posts_count)


# Создаем вьюшку для поиска по пользователю
@user_feed_blueprint.route('/users/<username>')
def user_feed(username):
    posts = get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts)


