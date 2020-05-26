import requests
import time
import credentials
import random

user = credentials.user
password = credentials.password

def creeper(user,password) :
    #Connecting your account to the server
    request = requests.post("https://www.icarya.fr/manager/auth", data={'pseudo':user,'mdp':password})
    ci_session = request.headers['Set-Cookie'].strip('ci_session=')
    cookies_icarya = {'ci_session' : ci_session}

    time.sleep(1)
    #Sending the vote request to icarya vote page
    request = requests.get("https://www.icarya.fr/Voter/clique", cookies = cookies_icarya)

    #Sending request with cookies to icarya server in order to get the reward
    request = requests.post("https://www.icarya.fr/Voter/vote_add", cookies=cookies_icarya, data={'site_id':'4'})
    print(request.text)

while True :
    creeper(user,password)
    print('Cooldown 3h')
    #3h cool down
    time.sleep(10800)
    #Cool down random
    time.sleep(random.randint(0,300))
