import json
from google.cloud import datastore
from google.cloud import logging

# DataStore
datastore_client = datastore.Client("speech-similarity")


def user_register(request):
    request_json = request.get_json(silent=True)

    with datastore_client.transaction():
        # Key = Firestore.uid

        complete_key = datastore_client.key("User", request_json["id"])
        user = datastore.Entity(key=complete_key)

        data = {
            "username": request_json.get("username"),
            "email": request_json.get("email"),
            "photoUrl": request_json.get("photoUrl"),
            "emailVerified": request_json.get("emailVerified"),
        }

        user.update(data)
        datastore_client.put(user)
    return json.dumps(user)
