#!/usr/bin/python3
"subscribers count"

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()
        
        if response.status_code != 200:
            return 0
        else:
            return data['data']['subscribers']
    
    except Exception as e:
        print(f"Error: {e}")
        return 0

