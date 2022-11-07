import shutil,random
from pytube import YouTube
from pytube import exceptions
from pytube import Playlist
from shutil import *
from telethon import TelegramClient,events  
from random import randint


client = TelegramClient("bot", 24694743, "f81bb69a0d9ac25aa7d029f2464a56d8")

client.start()
print("Bot Running")

@client.on(events.NewMessage(pattern="^/py"))

async def start(event):
    
    url=(event.text)
    url=url.split()[1:]
    url=" ".join(map(str,url))
    print(url)
    
    await event.reply("https://t.me/YassaTeam/5513")


@client.on(events.NewMessage(pattern="^/mp3"))

async def start(event):
    
    url=(event.text)
    url=url.split()[1:]
    url=" ".join(map(str,url))
    print(url)
    #url="https://youtu.be/Cmpk8NKhegI"
    try:
            yt = YouTube(url)
    except exceptions.ExtractError:
        await event.reply("الرابط غلط او انت مكتبتش رابط اصلا.. اكتبه صح وبطل فزلكه 🙄")
    except exceptions.VideoUnavailable:
        await event.reply("الفيديو دا غير متاح او اتحذف يحب يعني مش هعرف احملهولك جرب غيرو كدا 🥲")
    except exceptions.VideoPrivate:
            await event.reply("الفيديو دا برايفت يحب يعني مش هعرف احملهولك جرب غيرو كدا 🥲")
    except exceptions.VideoRegionBlocked:
              await event.reply("الفيديو دا اتعمله بلوك من يوتيوب يحب يعني مش هعرف احملهولك جرب غيرو كدا🥲")
              
    else:
        ln = 'abcdefghijklmnopqrstuvwxyz1234567890'
        fol=random.choice(ln)+random.choice(ln)+random.choice(ln)+'Yassa'+random.choice(ln)+random.choice(ln)+random.choice(ln)
        print(fol)
        await event.reply("تمام يحب بيتم تحميل الملف الصوتي حاليا..انتظر 🤍")
        chc = yt.streams.get_audio_only().download(fol)
        file = chc.splitlines()[0].replace(".mp4", "")
        file = file.splitlines()[0].replace(".webm", "")
        file=shutil.move(chc,""+file+".mp3")
        print(file)
        try:
            await client.send_file(event.chat.id, file,caption="حملتهولك اهو اي خدعه ابسط اعم 🌚🤍\n ومتنساش تشترك ف قناتي ماشي 🌚👍 \n @YassaTeam")
            
 
        except:
            await event.reply("الملف كبير مش هقدر احمله وابعتهولك")
            print("False")
        else:
            rmtree(fol)
            print("Done")
            
          

@client.on(events.NewMessage(pattern="^/mp4"))

async def start(event):
    
    url=(event.text)
    url=url.split()[1:]
    url=" ".join(map(str,url))
    print(url)
    #url="https://youtu.be/Cmpk8NKhegI"
    try:
            yt = YouTube(url)
    except exceptions.ExtractError:
        await event.reply("الرابط غلط او انت مكتبتش رابط اصلا.. اكتبه صح وبطل فزلكه 🙄")
    except exceptions.VideoUnavailable:
        await event.reply("الفيديو دا غير متاح او اتحذف يحب يعني مش هعرف احملهولك جرب غيرو كدا 🥲")
    except exceptions.VideoPrivate:
            await event.reply("الفيديو دا برايفت يحب يعني مش هعرف احملهولك جرب غيرو كدا 🥲")
    except exceptions.VideoRegionBlocked:
              await event.reply("الفيديو دا اتعمله بلوك من يوتيوب يحب يعني مش هعرف احملهولك جرب غيرو كدا🥲")
              
    else:
        ln = 'abcdefghijklmnopqrstuvwxyz1234567890'
        fol=random.choice(ln)+random.choice(ln)+random.choice(ln)+'Yassa'+random.choice(ln)+random.choice(ln)+random.choice(ln)
        print(fol)
        await event.reply("تمام يحب بيتم تحميل الفيديو حاليا..انتظر 🤍")
        file = yt.streams.get_highest_resolution().download(fol)
        
        print(file)
        try:
            await client.send_file(event.chat.id, file,caption="حملتهولك اهو اي خدعه ابسط اعم 🌚🤍\n ومتنساش تشترك ف قناتي ماشي 🌚👍 \n @YassaTeam")
            
 
        except:
            await event.reply("الملف كبير مش هقدر احمله وابعتهولك")
            print("False")
        else:
            rmtree(fol)
            print("Done")



client.run_until_disconnected()
