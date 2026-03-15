import telebot
from telebot import types

TOKEN = '7453003416:AAHKzo1KFgTf0f6SSDDkivf7BwgkBjaNK-0' # သင့် Token ကို အမှန်ထည့်ပါ
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_msg(message):
    markup = types.InlineKeyboardMarkup()
    # ခလုတ် (၃) ခု တည်ဆောက်ခြင်း
    btn1 = types.InlineKeyboardButton("ပရိုမိုးရှင်းများ", callback_data='promo')
    btn2 = types.InlineKeyboardButton("ဆက်သွယ်ရန်", callback_data='contact')
    btn3 = types.InlineKeyboardButton("အကောင့်ဖွင့်ရန်", callback_data='account')
    
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    
    bot.send_message(message.chat.id, "ကြိုဆိုပါတယ်! အောက်ပါတို့မှ တစ်ခုကို ရွေးချယ်ပါ:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'promo':
        bot.answer_callback_query(call.id, "ပရိုမိုးရှင်းများကို ကြည့်ရှုနေသည်...")
        bot.send_message(call.message.chat.id, "လက်ရှိပရိုမိုးရှင်းမှာ 30000 အခမဲဖြစ်ပါသည်။")
        
    elif call.data == 'contact':
        bot.answer_callback_query(call.id, "ဆက်သွယ်ရန် အချက်အလက်များ...")
        bot.send_message(call.message.chat.id, "ကျွန်တော်တို့ကို ဆက်သွယ်ရန် @mdl97online_bot ကိုနှိပ်ပါ")
        
    elif call.data == 'account':
        bot.answer_callback_query(call.id, "အကောင့်ဖွင့်ရန် ပုံနှင့်စာ...")
        # 'myphoto.jpg' ဖိုင်ကို Folder ထဲမှာ သေချာထည့်ထားပါ
        try:
            with open('myphoto.jpg', 'rb') as photo_file:
                bot.send_photo(call.message.chat.id, photo_file, 
                               caption="အကောင့်ဖွင့်ရန် လိုအပ်သော အချက်အလက်များ - \nဂိမ်းလင့် -  https://mdl98.com/ \nအထက်ပါလင့်ကိုနှိပ်ပြီးအကောင့်ဖွင့်ပါ\nအဆင်မပြေတာရှိရင်ပြန်လည်မေးမြန်းပေးပါနော်အကို")
        except FileNotFoundError:
            bot.send_message(call.message.chat.id, "အမှား - 'myphoto.jpg' ဖိုင်ကို ရှာမတွေ့ပါ။")

bot.infinity_polling()