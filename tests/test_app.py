from app import app


def test_homepage():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_valid_email():
    email = "student@example.com"

    assert "@" in email


def test_invalid_email():
    email = "studentexample.com"

    assert "@" not in email


def test_submit_feedback():
    client = app.test_client()

    response = client.post("/", data={
        "name": "Aalok",
        "email": "aalok@example.com",
        "course": "DevOps",
        "feedback": "Good course"
    })

    assert response.status_code == 200