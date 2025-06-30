import requests

def checkUpdates():
    url = "https://example.com/somefile.txt"
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text
        print(content)
    else:
        print(f"Failed to retrieve file. Status code: {response.status_code}")