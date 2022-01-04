import requests
import json


def search_wiki(query):
    url = f"https://en.wikipedia.org/w/api.php?action=query&origin=*&format=json&generator=search&gsrnamespace=0&gsrlimit=5&gsrsearch='{query}'"
    response = requests.get(url)
    info = response.json()['query']['pages']
    data = []
    for i in list(info):
        data.append(info[i]['title'])

    return data


def get_summary(title):
    url = f"https://en.wikipedia.org/w/api.php?action=query&origin=*&format=json&prop=extracts&exintro=&explaintext=&titles={title}"
    response = requests.get(url)
    info = response.json()['query']['pages']
    data = []
    for i in list(info):
        data.append(info[i]['extract'])

    return data


def research_wiki(query):
    data = search_wiki(query)
    summary = []
    for i in data:
        summary.append(get_summary(i)[0])

    return {'data': data, 'summary': summary}
