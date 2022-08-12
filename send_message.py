import requests
import json


def send_message_to_readings_topic():
    url = 'FUNCTION_URL'
    data = {
        'key_1': 'value_1',
        'key_2': 'value_2',
        'key_3': 'value_3'
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(f'r = {r}')


if __name__ == '__main__':
    send_message_to_readings_topic()
