import requests

def getRandomStories():
    url="https://funtranslations.com/api/translate"
    resonse=requests.get(url)
    if resonse.status_code ==200:
        data=resonse
        print(data.json())


getRandomStories()