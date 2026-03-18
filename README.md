import requests

def get_repo_info(owner, repo_name):
    # GitHub Public API URL
    url = f"https://api.github.com/repos/{owner}/{repo_name}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Repository Name: {data['name']}")
        print(f"Description: {data['description']}")
        print(f"Stars: {data['stargazers_count']}")
        print(f"Language: {data['language']}")
    else:
        print("Kshami-si, repository mahithi sigalilla.")

# Udaharanege: Google na 'jax' repository
get_repo_info('google', 'jax')
