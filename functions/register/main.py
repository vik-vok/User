import json
from google.cloud import datastore
from google.cloud import logging

# DataStore
datastore_client = datastore.Client('speech-similarity')

# Logging
logging_client = logging.Client()
logger = logging_client.logger('User Registration')

def user_register(request):
    request_json = request.get_json(silent=True)

    with datastore_client.transaction():
        # Key = Firestore.uid

        complete_key = datastore_client.key('User', request_json['id'])
        user = datastore.Entity(key=complete_key)

        data = {
            "username": request_json["username"],
            "email": request_json["email"],
            "photoUrl": request_json["photoUrl"],
            "emailVerified": request_json["emailVerified"],
        }

        logger.log_text(data)
    return json.dumps(request_json)
        # user.update(data)
        # datastore_client.put(user)

