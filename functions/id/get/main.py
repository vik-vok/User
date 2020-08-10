import json


def user_handler(request):
    user = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "JohnDoe@gmail.com",
        "age": 30,
        "city": "New York",
    }

    # convert into JSON:
    return json.dumps(user)
