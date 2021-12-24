import json


def read_json(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def load_data():
    with open("data/data.json", "r", encoding='utf-8') as f:
        posts = json.load(f)
    with open("data/comments.json", "r", encoding='utf-8') as f:
        comments = json.load(f)

    posts = attach_comments_to_posts(posts, comments)

    with open("data/bookmarks.json", "r", encoding='utf-8') as f:
        bookmarks = json.load(f)

    return posts, comments, bookmarks


def attach_comments_to_posts(posts, comments):
    for i, post in enumerate(posts):
        pk = post.get("pk")
        post_comments = []
        for comment in comments:
            if comment.get("post_id") == pk:
                post_comments.append(comment)
        posts[i]["comment_count"] = post_comments

    return posts


def get_post_by_id(postid):
    # функция для поиска поста по ID
    data = read_json('data/data.json')

    for post in data:
        if post.get("pk") == postid:
            return post


def get_comments_by_postid(postid):
    # Получаем комментарии для конкретного поста
    comments = read_json('data/comments.json')

    post_comments = []
    for comment in comments:
        if comment.get("post_id") == postid:
            post_comments.append(comment)
            return post_comments


def search_posts_by_word(word):
    # функция для поиска
    word = word.lower()
    posts = read_json('data/data.json')
    comments = read_json('data/comments.json')

    posts_search = [x for x in posts if word in x.get("content").lower()]
    posts_with_comments = attach_comments_to_posts(posts_search, comments)
    return posts_with_comments


def search_by_name(username):
    # Функция для получение всех постов конкретного человека
    data = read_json('data/data.json')
    posts_by_user = []

    for post in data:
        if post.get("poster_name") == username:
            posts_by_user.append(post)
    return posts_by_user
