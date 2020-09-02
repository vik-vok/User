import json
from google.cloud import datastore

datastore_client = datastore.Client("speech-similarity")


def user_original_voices(request):
    # 1. Get User ID from request
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and "userId" in request_json:
        userId = request_json["userId"]
    elif request_args and "userId" in request_args:
        userId = request_args["userId"]
    else:
        return (json.dumps({"error": "Missing parameter: userId"}), 422, {})

    # 2. Fetch All Original Voices
    query = datastore_client.query(kind="OriginalVoice")
    query.add_filter("userId", "=", userId)
    results = list(query.fetch())

    # 3. Fetch ID's
    query.keys_only()
    keys = list(query.fetch())
    for i in range(len(results)):
        results[i]["originalVoiceId"] = keys[i].id

    # 4. return JSON data
    return json.dumps(results, indent=4, sort_keys=True, default=str)
