from FindingFriendsUser import FindingFriendsUser

lib = {}

def get(id):
    if id not in lib:
        lib[id] = FindingFriendsUser('asdf', id)
    return lib[id]