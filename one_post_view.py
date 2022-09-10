import requests
from flask import Blueprint, render_template, request

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user

# Создаем блупринт
post_one_blueprint = Blueprint('post_one_blueprint', __name__, template_folder="templates")


# Создаем вьюшку для одного поста с комментами
@post_one_blueprint.route('/posts/<postid>')
def page_post_one(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', post=post, comments=comments, comments_count=len(comments))
