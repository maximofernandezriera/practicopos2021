from collections import deque


# If the github user name contains a $ in its last position, marks it a python developer
def is_python_developer(name):
    return name[-1] == '$'


graph_following_users = {}
graph_following_users["maximofdezriera"] = ["dfleta", "classicoman2", "jbarcelo"]
graph_following_users["classicoman2"] = ["miquelcabot$", "jaumerp"]
graph_following_users["dfleta"] = ["jaumerp"]
graph_following_users["jbarcelo"] = ["jaumeol$", "albertosoto$"]
graph_following_users["miquelcabot$"] = []
graph_following_users["jaumerp"] = []
graph_following_users["jaumeol$"] = []
graph_following_users["albertosoto$"] = []


def search(name):
    search_queue = deque()
    search_queue += graph_following_users[name]
    # This is how you keep track of which user you've searched before
    searched = set()
    # Check if some user is a python developer
    checker = False
    while search_queue:
        github_user = search_queue.popleft()
        # Only search this user if you haven't already searched them
        nobreak = True
        # Using a boolean in order to avoid infinite loops
        if github_user not in searched and nobreak:
            if is_python_developer(github_user) and nobreak:
                print(github_user + " is a python developer!")
                checker = True
                nobreak = False
            else:
                search_queue += graph_following_users[github_user]
                # Marks this person as searched
                searched.add(github_user)
    if not checker:
        print('No python developers found in your github following users')
    return checker


search("maximofdezriera")

#Big notation and algorithmic complexity.
#Breadth-first search takes O(number of people + number of edges)
#It’s more commonly written as O(V+E) (V for number of vertices, E for number of edges).