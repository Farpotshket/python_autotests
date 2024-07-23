import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = '5df6ea41c667350a35280389f5372e54'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : TOKEN
    } 

BODY_CREATE_POKEMON = {
    "name": "Жмых",
    "photo_id": 132
}

BODY_CHANGE_NAME = {
    "pokemon_id": "44663",
    "name": 'Жмышок',
    "photo_id" : 133
}

BODY_POKEBALL = {
    "pokemon_id": "44662"
}

'''response = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = BODY_CREATE_POKEMON)
print(response.text)

message = response.json()['message']
print(message)'''


'''response_name = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = BODY_CHANGE_NAME)
print(response_name.text)

message = response_name.json()['message']
print(message)'''

'''response_pokeball = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = BODY_POKEBALL)
print(response_pokeball.text)

message = response_pokeball.json()['message']
print(message)'''