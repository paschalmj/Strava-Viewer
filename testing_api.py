import requests #for working with APIs
import urllib3 #for warnings that come up when making HTTPS requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #disable a warning

#this is the url prefix for the auth token request
auth_url = 'https://www.strava.com/oauth/token'

#this is the information that gets fed into the POST request
#we use it to get a refreshed authorization token each time we need it
payload = {
    'client_id': '84840',
    'client_secret': '976dae9212ea8a1a62a74ee617201a80343d57ee',
    'refresh_token': 'd7f2f034ac095f29cfb63b72e7ba4d416c0688f4',
    'grant_type': 'refresh_token',
    'f': 'json'
}

#request the access token using the known refresh token above
print('Requesting Token...\n')
res = requests.post(auth_url, data=payload, verify=False)

#save the access token
access_token = res.json()['access_token']
print(f'Token Received: {access_token} \n')

#use access token to get activities data
activities_url = 'https://www.strava.com/api/v3/athlete/activities'
header = {'Authorization' : 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activities_url, headers=header, params=param, verify=False).json()
print('Dataset Received\n')

#print(my_dataset[0])
