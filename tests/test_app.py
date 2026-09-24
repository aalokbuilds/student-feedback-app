from app import app, is_valid_email


def test_homepage():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_valid_niet_email():
    email = "student@niet.co.in"

    assert is_valid_email(email)


def test_invalid_email_domain():
    email = "student@gmail.com"

    assert not is_valid_email(email)


def test_email_without_at_symbol():
    email = "studentniet.co.in"

    assert not is_valid_email(email)


def test_submit_feedback():
    client = app.test_client()

    response = client.post("/", data={
        "name": "Aalok",
        "email": "student@niet.co.in",
        "course": "DevOps",
        "feedback": "Good course"
    })

    assert response.status_code == 200