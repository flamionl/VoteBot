import requests
import time

#Getting password and user
user = str(input("Quel est votre nom d'utilisateur ?: "))
passwd = str(input("Quel est votre mot de passe ? : "))

def rpg_paradize_vote(user,passwd) :
    #Connecting your account to the server
    request = requests.post("https://www.icarya.fr/manager/auth", data={'pseudo':user,'mdp':passwd})
    ci_session = request.headers['Set-Cookie'].strip('ci_session=')
    cookies_icarya = {'ci_session' : ci_session}

    time.sleep(1)
    #Sending the vote request to icarya vote page
    request = requests.get("https://www.icarya.fr/Voter/clique", cookies = cookies_icarya)

    #Sending a request to rpg paradize in order to get the SERVERID104284 && PHPSESSID
    request = requests.get("http://www.rpg-paradize.com/?page=vote&vote=43891")

    #Getting the SERVERID104284
    SERVERID104284 = request.headers['Set-Cookie'].split(";")[0].split("=")[1]

    #Getting the PHPSESSID
    PHPSESSID = request.headers['Set-Cookie'].split(';')[2].split(',')[1].split('=')[1]
    cookies_rpgparadize = {'SERVERID104284': SERVERID104284, 'PHPSESSID':PHPSESSID, 'adscount':'1', 'parasubmitvote1':'vote'}

    #Sending request with cookies to script_rpg
    request = requests.get('http://www.rpg-paradize.com/script_rpg_v1.js', cookies=cookies_rpgparadize)

    #Sending request with cookies to script_account
    request = requests.get('http://www.rpg-paradize.com/script_account_js.php', cookies=cookies_rpgparadize)

    #Sending request with cookies to ads.js
    request = requests.get('http://www.rpg-paradize.com/ads.js', cookies=cookies_rpgparadize)

    #Sending request with cookies to icarya server in order to get the reward
    request = requests.post("https://www.icarya.fr/Voter/vote_add", cookies=cookies_icarya, data={'site_id':'2'})

while True :
    rpg_paradize_vote(user,passwd)

    











