from flask import Flask, request, redirect
import json
import os

app = Flask(__name__)

@app.route("/redirect")
def handle_redirect():
    user_id = request.args.get("uid")
    username = request.args.get("un", "NoUsername")
    if not user_id:
        return "Thiếu thông tin uid", 400

    try:
        with open("points.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    if user_id not in data:
        data[user_id] = {"username": username, "points": 0}
    data[user_id]["points"] += 5

    with open("points.json", "w") as f:
        json.dump(data, f, indent=4)

    return redirect("https://www.mediafire.com/file/qssaxxqa84srjeq/%E5%85%89%E9%80%9F%E8%99%9A%E6%8B%9F%E6%9C%BA_2.4.0.apk/file?dkey=7qfidr4fmzl&r=477", code=302)
