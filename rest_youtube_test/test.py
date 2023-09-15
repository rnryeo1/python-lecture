import requests

url = 'http://127.0.0.1:8000/api/auth'

reponse =requests.post(url,data= {'username' : 'admin', 'password': '123123'})

print(reponse.text)

myToken = reponse.json()
token = myToken['token']
header = {'Authorization' : 'Token ' + token}
response = requests.get('http://127.0.0.1:8000/api/student_list', headers=header)
print(response.text)




