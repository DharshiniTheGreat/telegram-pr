from telegram.ext import Updater, MessageHandler,Filters


from Adafruit_IO import Client
import os 

aio = Client('Priya_Dharshini',os.getenv('Priya_Dharshini'))


def demo1(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://image.shutterstock.com/image-vector/ok-hand-lettering-handmade-calligraphy-260nw-669965602.jpg'
  bot.message.reply_text('I am fine')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo2(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://www.energy.gov/sites/default/files/styles/full_article_width/public/turn_off_lights_19916160.jpg'
  bot.message.reply_text('LIGHT is turned ON')
  aio.send('light', 1)
  data1 = aio.receive('light')
  print(f'Received value: {data1.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo3(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://cdn5.vectorstock.com/i/1000x1000/70/44/3d-realistic-off-light-bulb-icon-closeup-vector-27407044.jpg'
  bot.message.reply_text('LIGHT is turned OFF')
  aio.send('light', 0)
  data1 = aio.receive('light')
  print(f'Received value: {data1.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo4(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://image.shutterstock.com/image-vector/electrical-fan-working-vector-cartoon-260nw-138334766.jpg'
  bot.message.reply_text('FAN is turned ON')
  aio.send('fan', 1)
  data2 = aio.receive('fan')
  print(f'Received value: {data2.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo5(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://thumbs.dreamstime.com/z/electric-table-fan-icon-outline-style-isolated-white-background-82471191.jpg'
  bot.message.reply_text('FAN is turned OFF')
  aio.send('fan', 0)
  data2 = aio.receive('fan')
  print(f'Received value: {data2.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def main(bot,update):
  a = bot.message.text.lower()
  print(a)
 
  if a == "how are you?":
    demo1(bot,update)
  elif a =="light on" or a=="turn on light":
    demo2(bot,update)
  elif a =="light off" or a=="turn off light":
    demo3(bot,update)
  elif a =="switch on the fan" or a=="turn on fan":
    demo4(bot,update)
  elif a =="switch of the fan" or a=="turn off fan":
    demo5(bot,update)
  else:
    bot.message.reply_text('Invalid Text')
BOT_TOKEN = os.getenv('BOT_TOKEN')
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
