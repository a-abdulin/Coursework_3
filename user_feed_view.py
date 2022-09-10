import requests
from flask import Blueprint, render_template, request

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user

# Создаем блупринт
user_feed_blueprint = Blueprint('user_feed_blueprint', __name__, template_folder="templates")


# Создаем вьюшку для поиска по пользователю
@user_feed_blueprint.route('/users/<username>')
def user_feed(username):
    posts = get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts)
