import telegram
from new import *

token = open('./telegram_token', 'r').read()

from telegram import Update 
from telegram.ext import ApplicationBuilder, CommandHandler 

# 메시지 처리기 = 핸들러
async def hello(update: Update, context) -> None: 
    await update.message.reply_text(
        f'Hello {update.effective_user.first_name}') 
async def bye(update: Update, context) -> None: 
    print(update.message.text.split())
    await update.message.reply_text(
        f'Bye {update.effective_user.first_name}') 

import requests
async def hi(update: Update,content) -> None:
    await update.message.reply_text('Hi. I am notefolio.')
    notefolio_url = 'https://theme.zdassets.com/theme_assets/10821475/fb618bc2b36b5aec0a54e2da42602a2f0b5928d0.png'
    r = requests.get(notefolio_url)
    await update.message.reply_photo(r.content)

async def design(update: Update, context) -> None:
    print(update.message.chat_id) # 채팅방 ID 
    a = datas_a()
    for i in a:
        await update.message.reply_text(i) 
    
print('---- 텔레그램 봇 실행 ----')


app = ApplicationBuilder().token(token).build() 

# 핸들러 등록
app.add_handler(CommandHandler("hello", hello)) # /hello
app.add_handler(CommandHandler("bye", bye)) # /bye
app.add_handler(CommandHandler("design", design)) # /crawl
app.add_handler(CommandHandler("hi", hi)) 

app.run_polling()
