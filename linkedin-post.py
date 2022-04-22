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
text = input('Text:')

# share post
url = "https://api.linkedin.com/v2/shares"
headers = {
    'Authorization' : f'Bearer {access_token}',
    'Content-Type' : 'application/json'
}
payload = {
    'owner': f'urn:li:person:{person_id}',
    'text': {
        'text': text
    }
}

response = requests.post(url=url, headers=headers, json = payload)

print(response.json())