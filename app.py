import flask

app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
    return flask.__version__
