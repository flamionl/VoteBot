import requests
import time


user = str(input("Quel est votre nom d'utilisateur ?: "))
passwd = str(input("Quel est votre mot de passe ? : "))

def list_serveur(user,passwd) :
    #Connecting your account to the server
    request = requests.post("https://www.icarya.fr/manager/auth", data={'pseudo':user,'mdp':passwd})
    ci_session = request.headers['Set-Cookie'].strip('ci_session=')
    cookies_icarya = {'ci_session' : ci_session}

    time.sleep(1)
    #Sending the vote request to icarya vote page
    request = requests.get("https://www.icarya.fr/Voter/clique", cookies = cookies_icarya)

    #Sending request with cookies to icarya server in order to get the reward
    request = requests.post("https://www.icarya.fr/Voter/vote_add", cookies=cookies_icarya, data={'site_id':'3'})
    print(request.text)


while True :
    creeper(user,passwd)

    print('24h cooldown')
    #24 cool down
    time.sleep(86400)

    #0 to 15 min cool down
    time.sleep(random.randint(0,900))