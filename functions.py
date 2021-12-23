import json

# def read_json(filename):
#     with open(filename, encoding='utf-8') as file:
#         return json.load(file)
from pprint import pprint


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
    with open("data/data.json", "r", encoding='utf-8') as f:
        data = json.load(f)

    for post in data:
        if post.get("pk") == postid:
            return post


def get_comments_by_postid(postid):
    with open("data/comments.json", "r", encoding='utf-8') as f:
        comments = json.load(f)
    post_comments = []
    for comment in comments:
        if comment.get("post_id") == postid:
            post_comments.append(comment)
            return post_comments
# print(get_comments_by_postid(4))
