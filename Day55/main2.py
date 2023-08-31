from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper_func():
        word = func()
        return f"<b>{word}<b>"

    return wrapper_func


def make_emphasis(func):
    def wrapper_func():
        word = func()
        return f"<em>{word}<em>"

    return wrapper_func


def make_underlined(func):
    def wrapper_func():
        word = func()
        return f"<u>{word}<u>"

    return wrapper_func


@app.route('/')
def hello_world():
    return ("<h1 style='text-align: center;'>Hello, World!</h1><p>This is a paragraph</p><img "
            "src='https://media.giphy.com/media/yFQ0ywscgobJK/giphy-downsized.gif' width=200>")


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}!, you are {number} years old"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
