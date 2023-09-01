from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    name = "Eunbae Kim"
    return render_template("index.html",
                           num=random_number,
                           cur_year=year,
                           my_name=name)


@app.route('/guess/<string:name>')
def guess(name):
    params = {
        'name': name
    }

    req_gen = requests.get("https://api.genderize.io", params=params)
    res_gen = req_gen.json()['gender']
    req_age = requests.get("https://api.agify.io", params=params)
    res_age = req_age.json()['age']

    return render_template("guess.html", name=name, gender=res_gen, age=res_age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/674d2f1dd978c701f368"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
