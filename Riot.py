import requests,random,time
import os
try:
    import requests 

except:
    os.system ("pip install requests ")
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
os.system("clear")
import requests
import os, sys, webbrowser,pyfiglet


os.system("clear")
#webbrowser.open("https://t.me/YassaTeam")

print ("\033[1;31m-"*60)
print("\033[1;33m")
yassa = pyfiglet.figlet_format('    Yassa Team')
print (yassa)
print ("\033[1;31m-"*60)
print("")
print ("        \033[1;33m        Welcome To Script Roit ")
print("")
print ("\033[1;31m-"*60)
print("")
print('\033[1;30m='*60)
print('\033[1;33m Dev: \033[1;32mhttps://t.me/YassaHany')
print('\033[1;30m='*60)
print('\033[1;33m Dev Channel: \033[1;32mhttps://t.me/YassaTeam')
print('\033[1;30m='*60)
code=input ("\033[1;32m Enter Your Code : \033[1;34m")
print('\033[1;30m='*60)
print("\033[1;32m")
cookies = {
    'Language': 'en-us',
    'PHPSESSID': '1ba2a9e3ece1456777acea6f8521a00f',
}

headers = {
    'authority': 'm.riotblockchain.live',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer null',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'Language=en-us; PHPSESSID=1ba2a9e3ece1456777acea6f8521a00f',
    'language': 'en',
    'origin': 'https://m.riotblockchain.live',
    'referer': 'https://m.riotblockchain.live/ar/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 3; SM-M526BR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}



cookies3 = {
    'Language': 'en-us',
    'PHPSESSID': '1ba2a9e3ece1456777acea6f8521a00f',
}






cookies2 = {
    'Language': 'en-us',
    'PHPSESSID': '1ba2a9e3ece1456777acea6f8521a00f',
}



json_data2 = {
    'id': 13,
    'coupon_id': '',
}



# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"id":13,"coupon_id":""}'
#response = requests.post('https://m.riotblockchain.live/v1/order/create', cookies=cookies, headers=headers, data=data)

for x in range(999999):
    
    n=random.randint(0000000,99999999)
    n3=("qwertyuiopasdfghjklzxcvbnm")
    n2=random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)
    n3=random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)+random.choice(n3)
    json_data = {
    'username': f'{n3}',
    'mobile': f'12{n}',
    'email': f'{n2}@gmail.com',
    'password': 'Yassa123',
    'sms': '000000',
    'verify': f'{code}',
    'prefix': '20',
    'type': 1,
    }
    response = requests.post('https://m.riotblockchain.live/v1/login/register', cookies=cookies, headers=headers, json=json_data)
    print(response.text)
    co = (response.json()['msg'])
    if co=="Restricted Registration":
        print()
        print("غير ال IP عشان يشتغل")
    
    print()
    json_data3 = {
    'username': f'{n3}',
    'password': 'Yassa123',
    }
    response3 = requests.post('https://m.riotblockchain.live/v1/login/index', cookies=cookies3, headers=headers, json=json_data3)
    print(response3.text)
    
    print()
    token= (response3.json()["data"])
    headers2 = {
    'authority': 'm.riotblockchain.live',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {token}',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'Language=en-us; PHPSESSID=1ba2a9e3ece1456777acea6f8521a00f',
    'language': 'en',
    'origin': 'https://m.riotblockchain.live',
    'referer': 'https://m.riotblockchain.live/ar/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-M526BR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    }
    time.sleep(2)
    response2 = requests.post('https://m.riotblockchain.live/v1/order/create', cookies=cookies2, headers=headers2, json=json_data2)
    print(response2.text)
    print()
    print("غير ال IP عشان يشتغل")
    print()
    print("سوف انتظرك لتغير ال ip مده 20 ثانيه")
    n=0
    for x in range(20):
        n=n+1
        time.sleep(1)
        print(f"Time.Sleep {n}")
        
    
