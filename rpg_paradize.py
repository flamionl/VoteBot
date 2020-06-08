import requests
import time
import credentials
import random


user = credentials.user
password = credentials.password

def rpg_paradize_vote(user,password) :
    #Connecting your account to the server
    request = requests.post("https://www.icarya.fr/manager/auth", data={'pseudo':user,'mdp':password})
    ci_session = request.headers['Set-Cookie'].strip('ci_session=')
    cookies_icarya = {'ci_session' : ci_session}

    time.sleep(1)
    #Sending the vote request to icarya vote page
    request = requests.get("https://www.icarya.fr/Voter/clique", cookies = cookies_icarya)

    #Sending a request to rpg paradize in order to get the SERVERID104284 && PHPSESSID
    request = requests.get("http://www.rpg-paradize.com/?page=vote&vote=43891")

    #Getting the SERVERID104    284
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
    print(request.text)

while True :
    rpg_paradize_vote(user,password)
    print('cooldown 3h')
    #3h cool down
    time.sleep(10800)
    











