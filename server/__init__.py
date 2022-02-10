from flask import Flask, jsonify, render_template

app = Flask(__name__, static_url_path="/")
app.config.from_object('config')
basedir = app.config["BASEDIR"]
app.template_folder = f"{basedir}/phaser"

app.static_folder = f"{basedir}/dist"


@app.route("/phaser", methods=["GET"])
def index():
    return render_template("index.html")
