import json


def get_users_original_voices(request):
    orig_voice1 = {
        'name': 'levioza',
        'description': "harry fucking potter",
        'voiceUrl': 'll.url',
        'userId': 14
    }
    orig_voice2 = {
        'name': 'misha wadi',
        'description': "when misha is going",
        'voiceUrl': 'lll.url',
        'userId': 14
    }

    orig_voices = [orig_voice1, orig_voice2]

    # convert into JSON:
    return json.dumps(orig_voices)
