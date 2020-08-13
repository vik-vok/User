import json


def get_users_recorded_voices(request):
    rec_voice1 = {
        'parentId': 12,
        'voiceUrl': 'rr.url',
        'userId': 16
    }
    rec_voice2 = {
        'parentId': 13,
        'voiceUrl': 'rr.url',
        'userId': 16
    }

    rec_voices = [rec_voice1, rec_voice2]

    # convert into JSON:
    return json.dumps(rec_voices)
