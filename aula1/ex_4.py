import requests 

URL = 'https://gen-net.herokuapp.com/api/users/'
res = requests.get(URL)

print(res.status_code)

users = res.json()

email = input ('Digite seu Email: ')

for user in users:
	if user.get('email') == email:
		print(user)