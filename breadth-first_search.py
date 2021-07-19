from collections import deque

# If the github user name contains a $ in its last position, marks it a python developer
def is_python_developer(name):
    return name[-1] == '$'

# Suppose that using GitHub's API we consult the list of friendships for any user
graph_following_users = {}
graph_following_users["maximofdezriera"] = ["jaumerp", "jbarcelo", "dfleta$"]
graph_following_users["jbarcelo"] = ["miquelcabot", "jaumeol"]
graph_following_users["jaumerp"] = ["jaumeol"]
graph_following_users["dfleta"] = ["classicoman2", "michelangelocasablancas"]
graph_following_users["miquelcabot"] = []
graph_following_users["jaumeol"] = []
graph_following_users["classicoman2"] = []
graph_following_users["michelangelocasablancas"] = []

def search(name):
    search_queue = deque()
    search_queue += graph_following_users[name]
    # This is how you keep track of which people you've searched before.
    searched = set()
    while search_queue:
        github_user = search_queue.popleft()
        # Only search this github_user if you haven't already searched them.
        if github_user not in searched:
            if is_python_developer(github_user):
                print(github_user + " is a python developer!")
                return True
            else:
                search_queue += graph_following_users[github_user]
                # Marks this github_user as searched
                searched.add(github_user)
                # Is the search_queue is null, print an error message
                if len(search_queue) == 0:
                    print('No python delevopers found in your github following users')
                
    return False

search("maximofdezriera")