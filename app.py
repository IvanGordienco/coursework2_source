from flask import Flask, request, render_template, send_from_directory, abort
import static
import json
from functions import read_json, load_data, get_post_by_id, get_comments_by_postid, search_posts_by_word, search_by_name

POST_PATH = "data/data.json"

posts, comments, bookmarks = load_data()
app = Flask(__name__)


@app.route('/')
def page_index():
    # Главная Страница, представление для всех постов
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>')
def posts_page(postid):
    # представление для одного поста и получение комментариев к посту
    post = get_post_by_id(postid)
    comments = get_comments_by_postid(postid)
    comments_counts = len(comments)

    return render_template('post.html', post=post, comments=comments, comments_counts=comments_counts)


@app.route('/search/')
def search_page():
    # Реализуем поиск по ключевого слово в текст поста.
    word = request.args.get('s')

    if not word:
        # если такого слово нету, возвращаем ошибку 400
        abort(400)

    posts = search_posts_by_word(word)

    return render_template('search.html', word=word, posts=posts, count_posts=len(posts))


@app.route('/users/<username>')
def users_feed(username):
    # Вывод постов конкретного пользователя  у которых poster_name соответствует username из запроса
    posts = search_by_name(username)

    return render_template('user-feed.html', posts=posts)

if __name__ == '__name__':
    app.run(debug=True)
