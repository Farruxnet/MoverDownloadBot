################################
####### Farrux Elomonov  #######
####### www.farruxnet.uz #######
################################
import telebot
import urllib.request
################################TOKEN################################
bot = telebot.TeleBot('1009671060:AAHpaCPs4d9Un9NO75jiFxPq78SYiXIMIlQ')

################################START################################
@bot.message_handler(commands=['start'])
def Start(message):
    u_m = telebot.types.ReplyKeyboardMarkup(True, True)
    u_m.row('Yuklash')
    bot.send_message(message.from_user.id, 'Mover.uz dan video yuklashni boshlash uchun Yuklash tugmasini bosing!', reply_markup=u_m)

#####################################################################
@bot.message_handler(content_types=['text', '/Yuklash'])
def Yukla(message):
    def Yuk():
        bot.send_message(message.from_user.id, 'Video manzilini yuboring!')
        bot.register_next_step_handler(message, SendLink)
    if message.text == 'Yuklash':
        Yuk()
    else:
        Yuk()
#######################################################################
def SendLink(message):
    silka = 'https://v.mover.uz/'
    link = str(message.text[23:].split('/')[0])+'_m.mp4'
    vid = urllib.request.urlopen(silka+link).read()
    bot.reply_to(message, 'Yuklanmoqda...\n')
    # bot.send_chat_action(message.from_user.id, 'upload_document')
    # bot.send_document(message.from_user.id, vid)
    bot.send_video(message.from_user.id, vid)

bot.polling(none_stop=True)














