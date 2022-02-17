from flask import Flask, render_template, url_for
from markupsafe import escape
app = Flask(__name__, static_url_path='/static', static_folder='node_modules')

@app.route("/")
def index():
    return "<h1>Index</h1><a href='wellcome/jc'>say hola</a>"

@app.route("/wellcome/<name>")
def holamundo(name):
    return f"<p>hola <strong>mundo</strong>: {escape(name)}</p>"

@app.route("/projects/")
def projects():
    return 'page projects'

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/api")
def api():
    return {
        "username": 'jpena',
        "theme": 'themejx',
        "image": url_for("static", filename='user.image.jpg'),
    }