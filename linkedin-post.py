import requests

# get person id with access token
access_token = "YOUR_ACCESS_TOKEN"
url = "https://api.linkedin.com/v2/me"
header = {
    'Authorization' : f'Bearer {access_token}'
}
response = requests.get(url=url, headers=header)
person_id = response.json()['id']

# text to share
text = input('Text: ')
to_url = input('Url to redirect: ')
url_title = input('Url Title: ')
# share post
url = "https://api.linkedin.com/v2/shares"
headers = {
    'Authorization' : f'Bearer {access_token}',
    'Content-Type' : 'application/json'
}
payload = {
    
    "content": {
        "contentEntities": [
            {
                "entityLocation": to_url,
                
            }
        ],
        "title": url_title,
    },
    'owner': f'urn:li:person:{person_id}',
    'text': {
        'text': text
    }
}

response = requests.post(url=url, headers=headers, json = payload)

print(response.json())