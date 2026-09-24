from flask import Flask, render_template, request

app = Flask(__name__)

feedback_list = []


def is_valid_email(email):
    return email.endswith("@niet.co.in")


@app.route("/", methods=["GET", "POST"])
def index():
    error = None

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]
        feedback = request.form["feedback"]

        if not is_valid_email(email):
            error = "Please use your NIET email address (@niet.co.in)."
        else:
            feedback_list.append({
                "name": name,
                "email": email,
                "course": course,
                "feedback": feedback
            })

    return render_template(
        "index.html",
        feedbacks=feedback_list,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)