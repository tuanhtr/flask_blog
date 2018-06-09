from index import app


@app.route('/')
def hello_world():
    return 'Hello World!'
