from index import app


@app.route('/posts/', method=['GET'])
def post_list_get():



    return 'Hello World!'
