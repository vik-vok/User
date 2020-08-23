from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


def user_register(request):
    request_json = request.get_json(silent=True)

    with datastore_client.transaction():
        # Key = Firestore.uid
        complete_key = datastore_client.key('User', request_json['id'])
        user = datastore.Entity(key=complete_key)

        user.update(request_json)
        datastore_client.put(user)

    return "User successfully registered"
