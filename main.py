from base64 import encode
import os
import json
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
PROJECT_ID = os.getenv('YOUR_PROJECT_ID')


def my_cloud_function(request):
    data = request.data

    if data is None:
        print('request.data is empty')
        return ('request.data is empty', 400) # Requests error 400: 'Bad request'

    print(f'request data: {data}')

    data_json = json.loads(data)
    print(f'json = {data_json}')

    value_1 = data_json['key1']
    value_2 = data_json['key2']
    value_3 = data_json['key3']

    print(f'key_1 = {value_1}')
    print(f'key_2 = {value_2}')
    print(f'key_3 = {value_3}')

    ################################################################
    # moving data to pubsub

    topic_path = 'YOUR_TOPIC_NAME'

    message_json = json.dumps({
        'data': {'message': 'readings!'},
        'readings': {
            'key_1': value_1,
            'key_2': value_2,
            'key_3': value_3
        }
    })
    message_bytes = message_json.encode('utf-8')

    try:
        publish_future = publisher.publish(topic_path, data=message_bytes)
        publish_future.result()
    except Exception as e:
        print(e)
        return (e, 500)

    return ('Message received and published to Pubsub', 200)
