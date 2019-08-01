import requests 

DOMAIN_URL = 'https://gen-net.herokuapp.com/api/users/{}'

payload = { 
'name': input('Digite Seu Nome: '),
'email': input('Digite seu Email: '),
'password': input('Digite sua Senha: ')
}

res = requests.post(DOMAIN_URL, payload)

if res.status_code == 200:
	user_id = res.json().get( 'id' )
	print('Usuario {} cadastrado com sucesso'.format(user_id))
else:
	print ('Email Já Cadastrado')
