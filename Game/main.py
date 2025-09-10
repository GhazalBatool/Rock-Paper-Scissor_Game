from flask import Flask, render_template, request, jsonify
from game_logic.rps_ai import random_ai_choice, learning_ai_choice, decide_winner, user_counts

app = Flask(__name__, template_folder="frontend/templates", static_folder="frontend/static")

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/play", methods=["POST"])
def play():
    data = request.json
    user_move = data.get("move")
    mode = data.get("mode", "random")

    if mode == "learning":
        ai_move = learning_ai_choice(user_counts)
    else:
        ai_move = random_ai_choice()

    result = decide_winner(user_move, ai_move)
    user_counts[user_move] += 1  # update learning history

    return jsonify({"user": user_move, "ai": ai_move, "result": result})

if __name__ == "__main__":
    app.run(debug=True)
