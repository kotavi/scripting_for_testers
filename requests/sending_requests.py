import requests

url = "https://jsonplaceholder.typicode.com/photos"

getRequest = requests.get(url)

print(getRequest.json())
print(getRequest.json()[100])
print(getRequest.headers)
print(getRequest.headers['Content-Encoding'])
print(getRequest.headers.keys())


# post request
payload = {"albumId": 3, "title": "test", "url": "rnd.com", "thumbnailUrl": "thumbnailUrl.com"}
postRequest = requests.post(url, json=payload)
print(postRequest.json())

# put request
# {'albumId': 3, 'id': 101, 'title': 'incidunt alias vel enim', 'url': 'https://via.placeholder.com/600/e743b', 'thumbnailUrl': 'https://via.placeholder.com/150/e743b'}
url = "https://jsonplaceholder.typicode.com/photos/100"
putRequest = requests.put(url, json=payload)
print(putRequest.json())

# delete request
deleteRequest = requests.delete(url)
print(deleteRequest.json())
