from flask import Flask, render_template
from post import Post

blog_url = "https://api.npoint.io/674d2f1dd978c701f368"
posts = Post(url=blog_url)

app = Flask(__name__)


@app.route('/')
def home():
    all_posts = posts.get_posts()
    return render_template("index.html", all_posts=all_posts)


@app.route('/post/<int:id>')
def each_post(id):
    post = posts.get_each_post(id=id)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
