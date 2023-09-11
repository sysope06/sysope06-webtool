from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("request.html",req=request)

if __name__ == "__main__":
    app.run(port=8000, debug=True)