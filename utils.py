def get_opener():

    import urllib

    # create a password manager
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    # If we knew the realm, we could use it instead of None.
    top_level_url = "http://localhost:5820/"
    password_mgr.add_password(None, top_level_url, 'admin', 'admin')

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib.request.build_opener(handler)

    return opener
