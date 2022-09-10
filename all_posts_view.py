import requests
from flask import Blueprint, render_template, request, jsonify

from utils import get_posts_all, load_posts, get_post_by_pk_in_list

# Создаем блупринт
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")
api_posts_blueprint = Blueprint('api_posts_blueprint', __name__)
api_post_one_blueprint = Blueprint('api_post_one_blueprint', __name__)


# Создаем вьюшку для постов
@posts_blueprint.route('/')
def page_posts_all():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


# Создаем вьюшки для api
@api_posts_blueprint.route('/api/posts', methods=["GET"])
def read_posts():
    posts = load_posts()
    return jsonify(posts)


@api_post_one_blueprint.route('/api/posts/<postid>', methods=["GET"])
def read_post_by_postid(postid):
    post = get_post_by_pk_in_list(postid)
    return jsonify(post)
