# tests/test_app.py

from server.app import app

def test_index_text():
    '''displays "Python Operations with Flask Routing and Views" in h1 in browser.'''
    response = app.test_client().get('/')
    assert 'Hello, World!' in response.data.decode()
