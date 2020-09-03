import json
from google.cloud import datastore

datastore_client = datastore.Client("speech-similarity")


def user_get_all(request):
    query = datastore_client.query(kind="User")
    results = list(query.fetch())


    for i in range(len(results)):
        results[i]["userId"] = results[i].key.id_or_name

    return json.dumps(results, indent=4, sort_keys=True, default=str)
