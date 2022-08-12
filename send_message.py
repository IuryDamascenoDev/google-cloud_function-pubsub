import requests
import json


def send_message_to_readings_topic():
    url = 'https://us-central1-simple-spark-project.cloudfunctions.net/\
        my_cloud_function'
    data = {
        'id': '0001',
        'name': 'iury',
        'age': 19
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(f'r = {r}')


if __name__ == '__main__':
    send_message_to_readings_topic()
