from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


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

        user.update(data)
        datastore_client.put(user)

    return "User successfully registered"
