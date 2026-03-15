import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# သင့် Token ကို လုံခြုံအောင်ထားပါ (အွန်လိုင်းပေါ် မတင်ပါနဲ့)
TOKEN = "7453003416:AAHKzo1KFgTf0f6SSDDkivf7BwgkBjaNK-0"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🎁 အခမဲ့ဘောနပ်စ်", "🔥 ငွေသွင်းနည်း"],
        ["📞 ဆက်သွယ်ရန်", "🌐 ဝဘ်ဆိုဒ်"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("မင်္ဂလာပါ! အောက်ပါ Menu များမှ ရွေးချယ်နိုင်ပါတယ် -", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "🎁 အခမဲ့ဘောနပ်စ်":
        # ပုံနှင့်စာတွဲ၍ ပြန်ပေးခြင်း
        await update.message.reply_photo(
            photo=open('bonus.jpg', 'rb'), # သင့် Folder ထဲက ပုံနာမည်ဖြစ်ရပါမယ်
            caption="🎉 Fc Free Spin  ဘောနပ်စ် ရရှိထားပါတယ်။"
        )
        
    elif text == "🔥 ငွေသွင်းနည်း":
        await update.message.reply_photo(
            photo=open('depphoto.jpg', 'rb'), 
            caption="🔥 ပုံမှာပြထားသည့်အတိုင်းငွေသွင်းနည်း"
        )
        
    elif text == "📞 ဆက်သွယ်ရန်":
        await update.message.reply_text("အကူအညီအတွက် @mdl97online_bot သို့ ဆက်သွယ်ပါ။")
        
    elif text == "🌐 ဝဘ်ဆိုဒ်":
        await update.message.reply_text("ကျွန်ုပ်တို့၏ ဝဘ်ဆိုဒ် - https://97mdl.vip")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()