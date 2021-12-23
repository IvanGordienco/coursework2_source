from flask import Flask, request, render_template, send_from_directory
import static
from functions import load_data, get_post_by_id, get_comments_by_postid

# POST_PATH = "data/data.json"

posts, comments, bookmarks = load_data()
app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>')
def posts_page(postid):
    post = get_post_by_id(postid)
    comments = get_comments_by_postid(postid)
    comments_counts = len(comments)
    return render_template('post.html', post=post, comments=comments, comments_counts=comments_counts)


app.run(debug=True)
