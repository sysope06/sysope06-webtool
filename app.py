import flask

app = flask.Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return flask.__version__

if __name__ == "__main__":
    app.run(port=8000, debug=True)