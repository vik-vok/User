def user_update(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and "userId" in request_json:
        user_id = str(request_json["userId"]) + "/json"
    elif request_args and "userId" in request_args:
        user_id = str(request_args["userId"]) + "/args"
    else:
        user_id = "UserId"

    # take object from json
    # update user, if it's own account
    return user_id
