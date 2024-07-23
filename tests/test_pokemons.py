import requests 
import pytest 

URL = 'https://api.pokemonbattle.ru'
TOKEN = '5df6ea41c667350a35280389f5372e54'
TRAINER_ID = 4132
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN} 

def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
   
def test_trainer_name():
    response_get = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Костя'