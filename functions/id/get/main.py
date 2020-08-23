import json
from google.cloud import datastore
import google.cloud.exceptions

client = datastore.Client('speech-similarity')


def user_get(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    return json.dumps([request_args, request_json])
    # if request_json and 'userId' in request_json:
    #     user_id = request_json['userId']
    # elif request_args and 'userId' in request_args:
    #     user_id = int(request_args['userId'])
    # else:
    #     # return error apiresponse
    #     return ""

    # key = client.key('User', user_id)
    # user = client.get(key)

