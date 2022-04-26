def test_healthcheck(test_client):
    response = test_client.head("/healthcheck")
    assert response.status_code == 200


def test_greetings(test_client):
    test_name = "bernard"
    response = test_client.get(f"/hello/{test_name}")
    assert response.status_code == 200
    assert response.json() == {"greetings": test_name}
