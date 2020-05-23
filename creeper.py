import requests
import time

user = str(input("Quel est votre nom d'utilisateur ?: "))
passwd = str(input("Quel est votre mot de passe ? : "))

def creeper(user,password) :
    #Connecting your account to the server
    request = requests.post("https://www.icarya.fr/manager/auth", data={'pseudo':user,'mdp':passwd})
    ci_session = request.headers['Set-Cookie'].strip('ci_session=')
    cookies_icarya = {'ci_session' : ci_session}

    time.sleep(1)
    #Sending the vote request to icarya vote page
    request = requests.get("https://www.icarya.fr/Voter/clique", cookies = cookies_icarya)

    #Sending request with cookies to icarya server in order to get the reward
    request = requests.post("https://www.icarya.fr/Voter/vote_add", cookies=cookies_icarya, data={'site_id':'4'})
    print(request.text)

while True :
    creeper(user,passwd)
    print('Cooldown 3h')
    #3h cool down
    time.sleep(10800)

    #0 to 15 min cool down
    time.sleep(random.randint(0,900))