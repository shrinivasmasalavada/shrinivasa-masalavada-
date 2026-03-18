import requests

def get_github_user(username):
    # User API endpoint
    url = f"https://api.github.com/users/{username}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        print(f"--- {username} Profile Details ---")
        print(f"Hesar: {user_data.get('name')}")
        print(f"Bio: {user_data.get('bio')}")
        print(f"Public Repos: {user_data.get('public_repos')}")
        print(f"Followers: {user_data.get('followers')}")
    else:
        print("Kshami-si, aa user mahithi sigalilla.")

# Udaharanege: 'torvalds' (Linux creator)
get_github_user('torvalds')
