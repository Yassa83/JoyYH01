import os
try:
    import requests
except:
    os.system('pip install requests')
try:
    import pyfiglet
except:
    os.system('pip install pyfiglet')
import requests,time
import pyfiglet,webbrowser

class main():
    def __init__(self,number, password):
        self.number=number
        self.password=password
        headers ={'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 6 Pro MIUI/V10.3.6.0.PEKMIXM)',
                  'Host': 'services.orange.eg',
                  'Accept-Encoding': 'gzip'}
        
        url = 'https://services.orange.eg/SignIn.svc/SignInUser'
        data = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (number,password)
        response = requests.post(url, headers=headers, data=data)
        global userID            
        userID = response.json()['SignInUserResult']['UserData']['UserID']
        if userID:
            print(" \033[1;33m               Successfully logged in")
            print("\033[1;33m")
            print('\033[1;31m='*60)
            print("\033[1;33m")
       
            
    def token(self,number,password):
       
        url2 = 'https://services.orange.eg/BucketsService.svc/SubscribeToBuckets'

        headers2 ={'Content-type': 'application/json',
                  'Accept': 'application/json',
                  'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 6 Pro MIUI/V10.3.6.0.PEKMIXM)',
                  'Host': 'services.orange.eg',
                  'Accept-Encoding': 'gzip'}
        
        data2 = '{"begindate":"","bucketID":"2198 ","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dial":"%s","lang":"ar","renewDuration":"","renewEndDate":"","userID":"%s","isEasyLogin":false,"password":"%s"}' % (number,userID,password)
        r=requests.post(url2,data=data2,headers=headers2)
      

    def delta(self,number , password):
            
        url3 = 'https://services.orange.eg/BucketsService.svc/UnSubscribeToBuckets'
               
        headers3 ={'Content-type': 'application/json',
                   'Accept': 'application/json',
                    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 6 Pro MIUI/V10.3.6.0.PEKMIXM)',
                    'Host': 'services.orange.eg',
                    'Accept-Encoding': 'gzip'}

        data3='{"bucketID":"2198","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dial":"%s","lang":"ar","isEasyLogin":false,"password":"%s"}'% (number,password)

                
        req=requests.post(url3,data=data3,headers=headers3)
       # print(req.content)
        

    ######################
    
    def india(self,number , password):
            
        url4 = 'https://services.orange.eg/BucketsService.svc/UnSubscribeToBuckets'
               
        headers4 ={'Content-type': 'application/json',
                   'Accept': 'application/json',
                    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 6 Pro MIUI/V10.3.6.0.PEKMIXM)',
                    'Host': 'services.orange.eg',
                    'Accept-Encoding': 'gzip'}

        data4='{"bucketID":"4017","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dial":"%s","lang":"ar","isEasyLogin":false,"password":"%s"}'% (number,password)
                
        req=requests.post(url4,data=data4,headers=headers4)

print('\033[1;31m='*60)      
print("\033[1;33m")
yassa = pyfiglet.figlet_format('    Yassa Team')
print (yassa)

print('\033[1;31m='*60)
print("\033[1;33m")


print ("\033[1;33m Dev Channel: https://t.me/YassaTeam ")
webbrowser.open("https://t.me/YassaTeam")
print("\033[1;33m")
print (" Dev: https://t.me/YassaHany")
print("\033[1;33m")
print('\033[1;31m='*60)
print("\033[1;33m")
print ("\033[1;33m       Welcome To Script Orange&YourLuck By YassaTeam")
print("\033[1;33m")
print('\033[1;31m='*60)
print("\033[1;33m")
number=input(" Enter Your Phone Number: ")
print("\033[1;33m")
password= input(" Enter Your Pass: ")
print("\033[1;33m")
print('\033[1;31m='*60)
print("\033[1;33m")
fox=main(number,password)
print(" if you want renue press (1)\n to delet (2)\n to do delet and and renuu (3)"+"\n" +" get offer extra(4)")
print("\033[1;33m")
delta= input((" Enter Your Choice: "))
print("\033[1;33m")
print('\033[1;31m='*60)
print("\033[1;33m")
if delta =="1":
    x=fox.token(number,password)  
    print(" Done Aded The Bucket")
elif  delta =="2":
    x=fox.delta(number,password)

    print(" Done Removeed your Bucket")

elif  delta =="4":
    x=fox.india(number,password)
    print(" Done Aded The Offer")

else:
    x=fox.delta(number,password)
    time.sleep(10)
    
    x=fox.token(number,password)
    print(" Done remove  Old Bucket And Giv You New Bucket ")
    
print("\033[1;33m")
print('\033[1;31m='*60)
print("\033[1;33m")