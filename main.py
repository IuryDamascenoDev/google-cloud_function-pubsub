from base64 import encode
import os
import json
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
PROJECT_ID = os.getenv('simple-spark-project')


def my_cloud_function(request):
    data = request.data

    if data is None:
        print('request.data is empty')
        return ('request.data is empty', 400)

    print(f'request data: {data}')

    data_json = json.loads(data)
    print(f'json = {data_json}')

    person_id = data_json['id']
    name = data_json['name']
    age = data_json['age']

    print(f'id = {person_id}')
    print(f'name = {name}')
    print(f'age = {age}')

    ####################################
    # moving data to pubsub

    topic_path = 'projects/simple-spark-project/topics/cdf-integ'

    message_json = json.dumps({
        'data': {'message': 'readings!'},
        'readings': {
            'id': person_id,
            'name': name,
            'age': age
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
