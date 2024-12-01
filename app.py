from flask import Flask, render_template, request
from discover import discover_games

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    genre = request.args.get("genre", "")
    platform = request.args.get("platform", "")
    sort_by = request.args.get("sort_by", "")

    games = discover_games(genre, platform, sort_by)

    return render_template("index.html", games=games)


if __name__ == "__main__":
    app.run(debug=True)
