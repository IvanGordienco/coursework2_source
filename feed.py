import json
import static
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
# Главная страница "лента"
def feed():

    with open('data/data.json', encoding='utf-8') as file:
        feed_ = json.load(file)
    for feeds in feed_:
        return render_template('user-feed.html', **feeds)


app.run()
