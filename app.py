from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from generator import generate_argument
from topics import topics_dict

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for sessions

topics = list(topics_dict.keys())

# Login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "user" and password == "User@0000":
            session["logged_in"] = True
            return redirect(url_for("generator_page"))
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html", error="")

# Generator page
@app.route("/generate", methods=["GET", "POST"])
def generator_page():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    result = ""
    topic_input = ""
    mode = "supportive"
    if request.method == "POST":
        topic_input = request.form.get("topic")
        mode = request.form.get("mode")
        result = generate_argument(topic_input, mode)
    return render_template("generate.html", result=result, topic_input=topic_input, mode=mode)

# Logout
@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))

# API endpoint for search suggestions
@app.route("/suggest")
def suggest():
    if not session.get("logged_in"):
        return jsonify([])
    query = request.args.get("q", "").lower()
    suggestions = [t for t in topics if query in t.lower()]
    return jsonify(suggestions[:5])

if __name__ == "__main__":
    app.run(debug=True)
