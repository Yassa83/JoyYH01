import requests
headers = {'User-Agent': 'okhttp/3.12.1'}
rr= requests.get('http://mobile.vodafone.com.eg/mobile-app/seamlessMsisdn', headers=headers).json()
print(rr)
