import json
from google.cloud import datastore

datastore_client = datastore.Client("speech-similarity")


def user_get_all(request):

    query = datastore_client.query(kind="User")
    results = list(query.fetch())

    query.keys_only()
    keys = list(query.fetch())

    for i in range(len(results)):
        results[i]["id"] = keys[i].id

    return json.dumps(results)
