import json
from google.cloud import datastore

client = datastore.Client("speech-similarity")


def user_delete(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and "userId" in request_json:
        user_id = request_json["userId"]
    elif request_args and "userId" in request_args:
        user_id = int(request_args["userId"])
    else:
        # return error api response
        return ""

    # check authentification and autorization

    key = client.key("User", user_id)
    client.delete(key)
    # delete user, check logged in or not, their account or not
    return json.dumps({})
