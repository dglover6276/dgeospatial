# This is a sandbox test for setting up Git and github
# File is not for production.


from flask import Flask

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!!!'


if __name__ == '__main__':
    app.run()
