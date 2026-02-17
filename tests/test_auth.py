def test_register_user(client):
    res = client.post(
        "/auth/register",
        json={
            "name": "testuser",
            "email": "test@example.com",
            "password": "1234"
        }
    )

    assert res.status_code == 201
    data = res.json()
    assert data["email"] == "test@example.com"


def test_login_user(client):
    # ensure user exists
    client.post(
        "/auth/register",
        json={
            "name": "loginuser",
            "email": "login@example.com",
            "password": "1234"
        }
    )

    res = client.post(
        "/auth/login",
        json={
            "email": "login@example.com",
            "password": "1234"
        }
    )

    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data
