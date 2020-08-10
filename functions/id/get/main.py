def user_handler(request):

    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_args and 'userId' in request_args:
        user_id = request_args['userId']
    else:
        user_id = 'UserId'

    # this function retrieves user information, with its id

    return user_id
