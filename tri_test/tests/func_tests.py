import pytest
import json
from tri_test import create_app
from tri_test.db import db
from tri_test.config import TestConfig


@pytest.fixture
def client():
    test_config_to_use = TestConfig()
    test_app = create_app(test_config_to_use)
    db.create_all(app=test_app)
    with test_app.test_client() as client:
        yield client


def test_post_single_messages(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'sender': 'Niclas',
        'receiver': 'Anyone',
        'content': 'This is a message'
    }
    url = '/message/'
    response = client.post(url, json=data)

    assert response.content_type == 'application/json'
    assert response.status_code == 201


def test_delete_single_messages(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'sender': 'Niclas',
        'receiver': 'Anyone',
        'content': 'This is a message'
    }
    post = client.post('/message/', json=data)
    assert json.loads(post.data)['id'] == 1

    response = client.delete('/message/1')
    assert response.status_code == 204

    after_delete = client.get('/message/1', json=data)
    assert after_delete.status_code == 404


def test_get_message_by_index(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data1 = {
        'sender': 'Niclas',
        'receiver': 'Anyone',
        'content': 'This is a message1'
    }
    data2 = {
        'sender': 'Niclas',
        'receiver': 'Anyone',
        'content': 'This is a message2'
    }
    data3 = {
        'sender': 'Niclas',
        'receiver': 'Anyone',
        'content': 'This is a message3'
    }
    url = '/message/'
    client.post(url, json=data1)
    client.post(url, json=data2)
    client.post(url, json=data3)

    response = client.get('message/2')

    assert response.content_type == 'application/json'
    assert response.status_code == 200
    assert json.loads(response.data)['id'] == 2
    assert json.loads(response.data)['content'] == 'This is a message2'


def test_get_multiple_message_by_index(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data1 = {
        'sender': 'Niclas',
        'receiver': 'Anyone',
        'content': 'This is a message1'
    }
    data2 = {
        'sender': 'Niclas',
        'receiver': 'Anyone',
        'content': 'This is a message2'
    }
    data3 = {
        'sender': 'Niclas',
        'receiver': 'Anyone',
        'content': 'This is a message3'
    }
    url = '/message/'
    client.post(url, json=data1)
    client.post(url, json=data2)
    client.post(url, json=data3)

    response = client.get('message/?from_index=2&to_index=3')

    assert response.content_type == 'application/json'
    assert response.status_code == 200

    res = json.loads(response.data)

    assert res[0]['id'] == 2
    assert res[1]['id'] == 3


def test_get_single_messages(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'sender': 'Niclas',
        'receiver': 'Anyone',
        'content': 'This is a message'
    }
    url = '/message/'
    client.post(url, json=data)

    response = client.get('message/1')

    assert response.content_type == 'application/json'
    assert response.status_code == 200
    assert json.loads(response.data)['id'] == 1
    assert json.loads(response.data)['receiver'] == 'Anyone'
