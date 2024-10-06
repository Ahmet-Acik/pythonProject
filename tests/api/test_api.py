import requests
from tenacity import retry, stop_after_attempt, wait_fixed

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def test_get_request():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    # {
    #     "userId": 1,
    #     "id": 1,
    #     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    #     "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    # }
    assert response.status_code == 200
    assert response.json()['id'] == 1
    assert response.json()['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
    assert response.json()['body'] == 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'

