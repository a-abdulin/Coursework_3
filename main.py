import logging

from flask import Flask, render_template, jsonify

# Импортируем блюпринт
from utils import load_posts, get_post_by_pk_in_list
from all_posts_view import posts_blueprint
from one_post_view import post_one_blueprint
from search_view import search_post_blueprint
from user_feed_view import user_feed_blueprint
from all_posts_view import api_posts_blueprint
from all_posts_view import api_post_one_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

logging.basicConfig(filename="api.log", level=logging.INFO, encoding='utf-8',
                    format='%(asctime)s [%(levelname)s] %(message)s')

app.register_blueprint(posts_blueprint)
app.register_blueprint(post_one_blueprint)
app.register_blueprint(search_post_blueprint)
app.register_blueprint(user_feed_blueprint)
app.register_blueprint(api_posts_blueprint)
app.register_blueprint(api_post_one_blueprint)

@app.errorhandler(404)
def page_not_found(e):
    logging.error('Ошибка URL')
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_internal_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run()
