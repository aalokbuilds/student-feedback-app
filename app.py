from flask import Flask, render_template, request

app = Flask(__name__)

feedback_list = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]
        feedback = request.form["feedback"]

        feedback_list.append({
            "name": name,
            "email": email,
            "course": course,
            "feedback": feedback
        })

    return render_template("index.html", feedbacks=feedback_list)


if __name__ == "__main__":
    app.run(debug=True)