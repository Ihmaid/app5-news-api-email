import requests

# Got from NewsAPI website
api_key = "effb4aae6a1048a69f14a8bacff24504"

# This url was generated by NewsAPI website
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-05-04&sortBy=publ" \
      "ishedAt&apiKey=effb4aae6a1048a69f14a8bacff24504"

# Made a request
request = requests.get(url)

# The method json generates a readable dictionary format
content = request.json()

# Content is a dict of 3 items, where the item "articles" is the key for a list
# of 100 dicts, each one with 8 items. This can be seen by debugger
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

