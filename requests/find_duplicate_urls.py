import requests


url = "https://jsonplaceholder.typicode.com/photos"
response = requests.get(url)
response_json = response.json()

list_of_urls = []
duplicate_urls = []
for record in response_json:
    if record['url'] not in list_of_urls:
        list_of_urls.append(record['url'])
    else:
        duplicate_urls.append(record['url'])

print("List of duplicate urls: %s" % duplicate_urls)
