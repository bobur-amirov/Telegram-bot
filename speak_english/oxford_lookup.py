import requests


app_id = "39a92da8"
app_key = "4d1a1e89248358685545d7c28f362bd7"
language = "en-gb"

def get_definitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    response = requests.get(url, headers={"app_id": app_id, "app_key":app_key})
    response = response.json()
    if 'error' in response.keys():
        return False

    output = {}
    senses = response['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"-> {sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    if response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output


if __name__ == '__main__':
    from pprint import pprint as print
    print(get_definitions('uzbekistan'))
    print(get_definitions('russia'))