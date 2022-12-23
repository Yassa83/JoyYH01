import requests,random,time


code = input ("Enter Your Code: ")
cookies = {
    'lang': 'ar',
    'waf_sc': '5889647726',
    'googleplugin': 'm5W7Smb5TeDT6MmF',
    'PHPSESSID': 'q2agl2rsc5q4v4idppeoa08g98',
}

headers = {
    'authority': 'lanzajet.vip',
    'accept': '*/*',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'lang=ar; waf_sc=5889647726; googleplugin=m5W7Smb5TeDT6MmF; PHPSESSID=q2agl2rsc5q4v4idppeoa08g98',
    'origin': 'https://lanzajet.vip',
    'referer': 'https://lanzajet.vip/register?invite_code=285864',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-M526BR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}



for x in range(9):
    r=random.randint(11111111,99999999)
    r2=random.randint(11111111,99999999)
    data = {
    'username': r2,
    'password': 'Yassa123',
    'invite_code': code,
    'phone': f'012{r}',
    }
    response = requests.post('https://lanzajet.vip/register', cookies=cookies, headers=headers, data=data).json()
    print(response)
    print('='*60)
    print("Change IP....")
    print('\033[1;30m='*60)
    time.sleep(10)