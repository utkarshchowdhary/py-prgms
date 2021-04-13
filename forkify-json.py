import urllib.request, urllib.parse, urllib.error
import json

forkifyurl = "https://forkify-api.herokuapp.com/api/search?"

while True:
    q = input("Enter Keyword: ")
    if len(q) < 1:
        break

    url = forkifyurl + urllib.parse.urlencode({"q": q})

    try:
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        print("Retrived", len(data), "characters")

    except urllib.error.HTTPError as e:
        print("HTTPError: {}".format(e.code))
    except urllib.error.URLError as e:
        print("URLError: {}".format(e.reason))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "error" in js:
        print("Failure to retrive data")
        continue

    print("Retrived", js["count"], "results")
    print(json.dumps(js, indent=4))

# json.loads() takes in a string and returns a json object.
# json.dumps() takes in a json object and returns a string
