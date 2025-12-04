import httpx

URL = "https://musical-giggle-wrj4w9jxrjvp25w5p-3000.app.github.dev"


def test_login_success():
    authData = {
        "id": "phillip.bradford@uconn.edu",
        "uuid-token": "925a4dfa-86b7-4c06-8f3e-fdccb0a748b2",
    }

    response = httpx.post(
        URL + "/login",
        data=authData,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    print("Success test:", response.status_code, response.text)


def test_login_invalid_token():
    authData = {
        "id": "phillip.bradford@uconn.edu",
        "uuid-token": "bad-token",
    }

    response = httpx.post(
        URL + "/login",
        data=authData,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    print("Invalid token test:", response.status_code, response.text)


if __name__ == "__main__":
    test_login_success()
    test_login_invalid_token()
