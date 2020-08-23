import json
from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


def user_get_all(request):
    query = datastore_client.query(kind='User')
    return json.dump(list(query.fetch()))
