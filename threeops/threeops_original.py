import sys
import requests
import json

url = "http://www.bbc.co.uk/radio1/playlist.json"

def main(argv):
    print("Hello world!")
    print("I just printed hello world")
    print("Now loading BBC data")

    data = json.loads(requests.get(url).text)
    print len(data['playlist']), "songs"

    for list_key in data['playlist']:
        record = data['playlist'][list_key][0]
        print record['title']

if __name__ == "__main__":
    main(sys.argv)

