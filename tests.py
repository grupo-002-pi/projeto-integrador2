from app import app

#def test_home():
    #response = app.test_client().get('GET /home HTTP/1.1')
    #assert response.status_code == 200
    
def test_home(client):
    response = client.get("/home")
    # Check that there was one redirect response.
    assert len(response.history) == 1
    # Check that the second request was to the index page.
    assert response.request.path == "/home"