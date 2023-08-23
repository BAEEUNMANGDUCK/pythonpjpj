from flask import Flask

app = Flask(__name__)
# __name__은 무엇인가?

print(__name__)  # __main__이 나온다. 외부에서 import한 모듈이 아니라는 뜻. 외부에서 호출될 시에는 hello가 나올 것


# Python Decorators --> 데코레이터란 이미 있는 함수에 기능을 더하는 함수이다.

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()




# PS C:\path\to\app> $env:FLASK_APP = "hello.py" -> flask run
# kernel: 피스타치오의 알맹이 부분 --> 운영체제의 핵심부
# Shell: 피스타치오의 껍질 --> 사용자 인터페이스/GUI, CLI 등이 있다.
