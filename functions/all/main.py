import json


def users_handler(request):
    user1 = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "JohnDoe@gmail.com",
        "age": 30,
        "city": "New York",
    }
    user2 = {
        "first_name": "Saba",
        "last_name": "Pochkhua",
        "email": "Saba.Pochkhua@gmail.com",
        "age": 22,
        "city": "Tbilisi",
    }
    user3 = {
        "first_name": "Nika",
        "last_name": "Losaberidze",
        "email": "NikaLosa@gmail.com",
        "age": 22,
        "city": "Tbilisi",
    }

    users = [user1, user2, user3]

    # convert into JSON:
    return json.dumps(users)
