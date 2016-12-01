# This short code makes requests to wordniks API to get definitions

import requests

WORDNIK_URL = 'http://api.wordnik.com:80/v4/word.json/article/definitions?limit=200&includeRelated=true&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'

response = requests.get(WORDNIK_URL)

print(response)

print(response.text)

print(response.headers)

print(response.content)

definitions = response.json()

print(definitions[0])

print(definitions[0]['text'])

len(definitions)

texts = []
l = 0

for k in definitions:
    texts.append(definitions[l]['text'])
    l += 1

for definition in definitions:
    print('+', definition['text'])

print(texts)
