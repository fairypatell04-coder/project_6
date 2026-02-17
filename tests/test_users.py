def get_token(client):
    client.post(
        "/auth/register",
        json={
            "name": "apiuser",
            "email": "api@example.com",
            "password": "1234"
        }
    )

    res = client.post(
        "/auth/login",
        json={
            "email": "api@example.com",
            "password": "1234"
        }
    )

    return res.json()["access_token"]


def test_get_me(client):
    token = get_token(client)

    res = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 200
    assert res.json()["email"] == "api@example.com"


def test_users_requires_auth(client):
    res = client.get("/users/")
    assert res.status_code == 401
