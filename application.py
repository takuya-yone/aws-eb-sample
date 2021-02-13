from flask import Flask

# print a nice greeting.
def say_hello(username = "World"):
    return {"text": "hello world!"}

application = Flask(__name__)

application.add_url_rule('/', 'index', (lambda: say_hello()))

application.add_url_rule('/<username>', 'hello', (lambda username: say_hello(username)))

# run the app.
if __name__ == "__main__":
    application.debug = True
    application.run()