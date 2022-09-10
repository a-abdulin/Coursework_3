import requests
from flask import Blueprint, render_template, request

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user

# Создаем блупринт
search_post_blueprint = Blueprint('search_post_blueprint', __name__, template_folder="templates")


# Создаем вьюшку для поиска по тексту
@search_post_blueprint.route('/search')
def search_page():
    search__input = request.args.get('s')
    posts_by_query = search_for_posts(search__input)
    posts_count = 0
    if posts_by_query is not None:
        posts_count = len(posts_by_query)
    return render_template("search.html", hash=search__input, posts=posts_by_query, posts_count=posts_count)
