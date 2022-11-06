import requests,telebot,shutil
from pytube import YouTube
from pytube import exceptions
from pytube import Playlist



bot =telebot.TeleBot("5368093121:AAFBzV9eTOS8Zu-7odxe_P6VeQcXjfMkItw")
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,("طريقه التحميل سهله غير كلمه url برابط الفيديو اللي عايز تحمله سواء كنت عايز تحمله فيديو عادي او اغنيه \n\n/mp3 url لو عايز تنزل اغنيه\n/mp4 url لو عايز تنزل فيديو \n\nلو عايز تحمل قائمه تشغيل كامله بدوسه واحده فمش هتعرف تحملها من البوت لكن هتعرف تحملها من اسكربت البايثون بتاعنا 😀 ابعت /py عشان ابعتلك الاسكربت والشرح \n\nالمطور: @YassaHany\nقناة المطور: @YassaTeam\n"))

@bot.message_handler(commands=["py"])
def start(message):
    bot.send_message(message.chat.id,("https://t.me/YassaTeam/5513"))

@bot.message_handler(commands=["mp3"])
def start(message):
    url=(message.text)
    url=url.split()[1:]
    url=" ".join(map(str,url))
    #print(url)
    #url="https://youtu.be/Cmpk8NKhegI"
    try:
            yt = YouTube(url)
    except exceptions.ExtractError:
        bot.send_message(message.chat.id,("الرابط غلط او انت مكتبتش رابط اصلا.. اكتبه صح وبطل فزلكه 🙄"))
    except exceptions.VideoUnavailable:
        bot.send_message(message.chat.id,("الفيديو دا غير متاح او اتحذف يحب يعني مش هعرف احملهولك جرب غيرو كدا 🥲"))
    except exceptions.VideoPrivate:
            bot.send_message(message.chat.id,("الفيديو دا برايفت يحب يعني مش هعرف احملهولك جرب غيرو كدا 🥲"))
    except exceptions.VideoRegionBlocked:
              bot.send_message(message.chat.id,("الفيديو دا اتعمله بلوك من يوتيوب يحب يعني مش هعرف احملهولك جرب غيرو كدا🥲"))
              
    else:
        bot.send_message(message.chat.id,("تمام يحب بيتم تحميل اللي طلبته حاليا..انتظر 🤍"))
        chc = yt.streams.get_audio_only().download()
        nam = chc.splitlines()[0].replace(".mp4", "")
        nam = nam.splitlines()[0].replace(".webm", "")
        nam=shutil.move(chc,""+nam+".mp3")
        print(nam)
        bot.send_document(message.chat.id,open(nam,"rb"))
        bot.send_message(message.chat.id,("حملتهولك اهو اي خدعه ابسط اعم 🌚🤍\n ومتنساش تشترك ف قناتي ماشي 🌚👍 \n @YassaTeam "))
    
@bot.message_handler(commands=["mp4"])
def start(message):
    url=(message.text)
    url=url.split()[1:]
    url=" ".join(map(str,url))
    print(url)
    #url="https://youtu.be/Cmpk8NKhegI"
    #yt = YouTube(url)
    try:
            yt = YouTube(url)
    except exceptions.ExtractError:
        bot.send_message(message.chat.id,("الرابط غلط او انت مكتبتش رابط اصلا.. اكتبه صح وبطل فزلكه 🙄"))
    except exceptions.VideoUnavailable:
        bot.send_message(message.chat.id,("الفيديو دا غير متاح او اتحذف يحب يعني مش هعرف احملهولك جرب غيرو كدا 🥲"))
    except exceptions.VideoPrivate:
            bot.send_message(message.chat.id,("الفيديو دا برايفت يحب يعني مش هعرف احملهولك جرب غيرو كدا 🥲"))
    except exceptions.VideoRegionBlocked:
              bot.send_message(message.chat.id,("الفيديو دا اتعمله بلوك من يوتيوب يحب يعني مش هعرف احملهولك جرب غيرو كدا🥲"))
              
    else:
            bot.send_message(message.chat.id,("تمام يحب بيتم تحميل اللي طلبته حاليا..انتظر 🤍"))
            chc = yt.streams.get_highest_resolution().download()
            nam=shutil.move(chc,chc)
            print(nam)
            bot.send_document(message.chat.id,open(nam,"rb"))
            bot.send_message(message.chat.id,("حملتهولك اهو اي خدعه ابسط اعم 🌚🤍\n ومتنساش تشترك ف قناتي ماشي 🌚👍 \n @YassaTeam "))
    
bot.polling()