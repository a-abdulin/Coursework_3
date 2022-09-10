import json

from dao.posts_dao import PostsDAO
from dao.comments_dao import CommentsDao


def load_posts():
    with open(".\data\posts.json", "r", encoding='utf-8') as file:
        posts_data = json.load(file)
    return posts_data


def get_posts_all():
    posts_data = load_posts()
    posts = []
    for post in posts_data:
        posts.append(PostsDAO(post["poster_name"], post["poster_avatar"], post["pic"], post["content"],
                              post["views_count"], post["likes_count"], post["pk"], ))
    return posts


def load_comments():
    path = ".\data\comments.json"
    with open(path, "r", encoding='utf-8') as file:
        comments_data = json.load(file)
    return comments_data


def get_comments_all():
    comments_data = load_comments()
    comments = []
    for comment in comments_data:
        comments.append(CommentsDao(comment["post_id"], comment["commenter_name"],
                                    comment["comment"], comment["pk"], ))
    return comments


def get_posts_by_user(user_name):
    posts = get_posts_all()
    posts_by_user = []
    for post in posts:
        if user_name == post.poster_name:
            posts_by_user.append(post)
    if posts_by_user != []:
        return posts_by_user
    raise ValueError("Такого пользователя нет среди постеров!")


def get_comments_by_post_id(post_id):
    comments = get_comments_all()
    comments_by_post_id = []
    for comment in comments:
        if int(post_id) == comment.post_id:
            comments_by_post_id.append(comment)
    if comments_by_post_id == []:
        raise ValueError("Комментариев к этому посту нет!")
    return comments_by_post_id


def search_for_posts(query):
    posts = get_posts_all()
    posts_by_query = []
    for post in posts:
        if post.content != '' and query is not None:
            content_lower = post.content.lower()
            query_lower = query.lower()
            if query_lower in content_lower:
                posts_by_query.append(post)
    return posts_by_query


def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if int(pk) == post.pk:
            return post


def get_post_by_pk_in_list(pk):
    posts = load_posts()
    for post in posts:
        if int(pk) == post.get("pk"):
            return post


post = get_post_by_pk_in_list(3)
print(post.keys())
