def user_register(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    # firebase interaction for authentication
    # register and save in database/firestore user object
    return "User successfully registered"
