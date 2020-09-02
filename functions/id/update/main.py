import json
from google.cloud import datastore

client = datastore.Client("speech-similarity")


def user_update(request):

    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and "userId" in request_json:
        user_id = request_json["userId"]
    elif request_args and "userId" in request_args:
        user_id = int(request_args["userId"])
    else:
        # return error apiresponse
        return ""

    # check authentification and autorization

    with client.transaction():
        key = client.key("User", user_id)
        user = client.get(key)

        for arg, val in request_json.items():
            if arg != "userId":
                user[arg] = val
        client.put(user)

    return json.dumps({})
