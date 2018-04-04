import requests


def test_server_sends_200_response():
    """"""
    response = requests.get('http://127.0.0.1:3000')
    assert response.status_code == 200
    assert '<title> cowsay </title>' in response.text


def test_server_cowsay_sends_200_response():
    """"""
    response = requests.get('http://127.0.0.1:3000/cowsay')
    assert response.status_code == 200
    assert 'address bar' in response.text


def test_server_cow_sends_200_response():
    """"""
    response = requests.get('http://127.0.0.1:3000/cow?msg="hello world"')
    assert response.status_code == 200
    assert 'hello world' in response.text


def test_server_cow_sends_400_response():
    """"""
    response = requests.get('http://127.0.0.1:3000/cow?msg=hello')
    assert response.status_code == 400
    assert response.text == 'Incorrect format'


def test_server_sends_404_response():
    """"""
    response = requests.get('http://127.0.0.1:3000/cowsa')
    assert response.status_code == 404
    assert response.text == 'Not Found'


def test_server_cow_post_sends_200_response():
    """"""
    response = requests.post('http://127.0.0.1:3000/cow?msg="hello world"')
    assert response.status_code == 200
    assert 'hello world' in response.text


def test_server_cow_post_sends_400_response():
    """"""
    response = requests.post('http://127.0.0.1:3000/cow?"ms4g=hello')
    assert response.status_code == 400
    assert response.text == 'Incorrect format'


def test_server_post_sends_404_response():
    """"""
    response = requests.post('http://127.0.0.1:3000/cowsa')
    assert response.status_code == 404
    assert response.text == 'Not Found'



