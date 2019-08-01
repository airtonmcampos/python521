
import requests 

DOMAIN_URL = 'https://gen-net.herokuapp.com/api/users/{}'

user_id = input('digite seu id: ')
name = input('digite seu nome: ')
email = input('digite seu email: ')
password = input('digite sua senha: ')

payload = { 
	'name': name,
	'email': email, 
	'password': password
}

response = requests.put(DOMAIN_URL.format(user_id), payload)

if response.status_code ==200:
	print('Usuario atualizado com sucesso')
else:
	print('Erro ao atualizar o usuario')


