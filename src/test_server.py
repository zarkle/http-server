import requests


def test_server_sends_200_response():
    """test home route works"""
    response = requests.get('http://127.0.0.1:3000')
    assert response.status_code == 200
    assert '<title> cowsay </title>' in response.text


def test_server_sends_200_response_header():
    """test home route works"""
    response = requests.get('http://127.0.0.1:3000')
    assert response.headers['Server'] == 'BaseHTTP/0.6 Python/3.6.4'


def test_server_cowsay_sends_200_response():
    """test cowsay route works"""
    response = requests.get('http://127.0.0.1:3000/cowsay')
    assert response.status_code == 200
    assert 'address bar' in response.text


def test_server_cowsay_sends_200_response_header():
    """test cowsay route works"""
    response = requests.get('http://127.0.0.1:3000/cowsay')
    assert response.headers['Server'] == 'BaseHTTP/0.6 Python/3.6.4'


def test_server_cow_sends_200_response():
    """test message route works"""
    response = requests.get('http://127.0.0.1:3000/cow?msg="hello world"')
    assert response.status_code == 200
    assert 'hello world' in response.text


def test_server_cow_sends_200_response_header():
    """test message route works"""
    response = requests.get('http://127.0.0.1:3000/cow?msg="hello world"')
    assert response.headers['Server'] == 'BaseHTTP/0.6 Python/3.6.4'


def test_server_cow_sends_400_response():
    """test cow route sends 400"""
    response = requests.get('http://127.0.0.1:3000/cow?msg=hello')
    assert response.status_code == 400
    assert response.text == 'Incorrect format'


def test_server_cow_sends_400_response_header():
    """test cow route sends 400"""
    response = requests.get('http://127.0.0.1:3000/cow?msg=hello')
    assert response.headers['Server'] == 'BaseHTTP/0.6 Python/3.6.4'


def test_server_sends_404_response():
    """test bad route"""
    response = requests.get('http://127.0.0.1:3000/cowsa')
    assert response.status_code == 404
    assert response.text == 'Not Found'


def test_server_sends_404_response_header():
    """test bad route"""
    response = requests.get('http://127.0.0.1:3000/cowsa')
    assert response.headers['Server'] == 'BaseHTTP/0.6 Python/3.6.4'


def test_server_cow_post_sends_200_response():
    """test post route works"""
    response = requests.post('http://127.0.0.1:3000/cow', json={'msg': 'test'})
    assert response.status_code == 200
    assert 'test' in response.text


def test_server_cow_post_sends_200_response_header():
    """test post route works"""
    response = requests.post('http://127.0.0.1:3000/cow', json={'msg': 'test'})
    assert response.headers['Server'] == 'BaseHTTP/0.6 Python/3.6.4'
    assert response.headers['Content-Type'] == 'application/json'


def test_server_cow_post_sends_400_response():
    """test post route 400 works"""
    response = requests.post('http://127.0.0.1:3000/cow?"ms4g=hello')
    assert response.status_code == 400
    assert response.text == 'Incorrect format'


def test_server_cow_post_sends_400_response_header():
    """test post route 400 works"""
    response = requests.post('http://127.0.0.1:3000/cow?"ms4g=hello')
    assert response.headers['Server'] == 'BaseHTTP/0.6 Python/3.6.4'


def test_server_post_sends_404_response():
    """test post route 404 error works"""
    response = requests.post('http://127.0.0.1:3000/cowsa')
    assert response.status_code == 404
    assert response.text == 'Not Found'


def test_server_post_sends_404_response_header():
    """test post route 404 error works"""
    response = requests.post('http://127.0.0.1:3000/cowsa')
    assert response.headers['Server'] == 'BaseHTTP/0.6 Python/3.6.4'
