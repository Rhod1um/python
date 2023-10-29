import requests  #siger requests ikke kan blive resolved selvom den godt kan

print('Hello world')

req = requests.get('https://clbokea.github.io/exam/assignment_2.html')

print(req.text)