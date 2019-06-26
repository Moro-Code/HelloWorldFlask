from flask import blueprints, render_template

bp = blueprints.Blueprint('hello_world', __name__)

@bp.route("/", methods = ("GET",))
def hello_world():
    return render_template("index.html", name = "Sean")