import requests
import random
import time
import json
from bs4 import BeautifulSoup as bs
import graphql

name = 'qwertyuiopasdfghjklzxcvbnm1234567890'
username = ''
roop = int(input('몇 번 돌리실건지? : '))

for i in range(roop):
  username = ''

  for a in range(12): 
    num = random.randrange(1,len(name))
    username = username + name[num]
    password = username + '*'

  print('\n-\n')
    
  with requests.Session() as ent:
    print(f"아이디 : {username}\n비밀번호 : {password}")

    soup = bs(ent.get("https://playentry.org").text, "html.parser")
    csrf = soup.select_one('meta[name=csrf-token]')['content']
    headers = {'CSRF-Token': csrf, "Content-Type": "application/json"}

    ent.post('https://playentry.org/graphql',     
    headers = headers, json={'query':graphql.query, 'variables':{"type":"user","word":username}})

    ent.get("https://playentry.org/signup/1")
    ent.get("https://playentry.org/signup/2")
    ent.get("https://playentry.org/signup/3")
    
    req = ent.post("https://playentry.org/graphql", headers=headers, json={'query':graphql.create, 'variables':{"username":username,"passwordConfirm":password,"password":password,"role":"member","grade":"1","gender":"male","nickname":username,"email":"","mobileKey":""}})

print('\n-\n생성 완료')
