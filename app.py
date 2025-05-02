from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/static/css')
def StyleF():
    return render_template("style.css")

@app.route('/api/posts')
def get_posts():
    with open('Tweets.json', "r") as file:
        posts = json.load(file)
    return jsonify(posts)

@app.route('/api/post', methods=['POST'])
def add_posts():
    new_post = request.get_json()

    with open('Tweets.json', "r") as file:
        posts = json.load(file)
        posts.insert(0, new_post)

    with open ('Tweets.json', 'w') as file:
        json.dump(posts, file, indent=4)

    return jsonify({'status': 'success'}), 201


if __name__ == '__main__':
    app.run(debug=True)