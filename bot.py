import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from keep_alive import keep_alive
import time

# ដាក់ Token របស់អ្នកនៅទីនេះ ឬប្រើ Environment Variable
API_TOKEN = '8933232129:AAH3bZPylnAug8uIe2G9nFlXQN9ysbtiLC0'
bot = telebot.TeleBot(API_TOKEN)

# មុខងារបង្ហាញម៉ឺនុយគោល (រូបភាព និង Inline Keyboard)
def send_main_menu(chat_id):
    photo_url = "https://i.ibb.co/1Z010101/sal-diamond.jpg" # អ្នកអាចប្តូរជា Link รูปภาพរបស់អ្នក ឬប្រើ send_photo ធម្មតា
    
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🔥 Free Fire", callback_data="game_ff"),
        InlineKeyboardButton("💎 Mobile Legends", callback_data="game_ml"),
        InlineKeyboardButton("⚔️ Honor of Kings", callback_data="game_hok"),
        InlineKeyboardButton("⭐ Telegram Premium", callback_data="tg_premium"),
        InlineKeyboardButton("📦 ការទិញទំនិញរបស់ខ្ញុំ", callback_data="my_orders"),
        InlineKeyboardButton("💬 ជំនួយ / Contact Support", callback_data="support")
    )
    
    caption_text = (
        "🎮 **ਸ్వاگతంមកកាន់ SAL DIAMOND TOP UP!**\n\n"
        "⚡ រហ័ស • សុវត្ថិភាព • តម្លៃសមរម្យ\n\n"
        "👇 សូមជ្រើសរើសសេវាកម្មខាងក្រោម៖"
    )
    
    try:
        # ផ្ញើរូបភាព និង Inline Menu ដូចក្នុងរូបភាពរបស់អ្នក
        bot.send_message(chat_id, caption_text, parse_mode="Markdown", reply_markup=markup)
    except Exception as e:
        print(f"Error sending menu: {e}")

# ពេលអ្នកប្រើប្រាស់ចុច /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    send_main_menu(message.chat.id)

# គ្រប់គ្រងការចុចប៊ូតុង Inline Menu
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "game_ml":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "💎 អ្នកបានជ្រើសរើស **Mobile Legends**\nសូមបញ្ជូន Player ID និង Zone ID មក៖", parse_mode="Markdown")
    elif call.data == "game_ff":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🔥 អ្នកបានជ្រើសរើស **Free Fire**\nសូមបញ្ជូន Player ID មក៖", parse_mode="Markdown")
    elif call.data == "support":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📞 រាល់បញ្ហាសូមទាក់ទងមកកាន់ Admin: @YourAdminUsername")
    else:
        bot.answer_callback_query(call.id, "មុខងារនេះកំពុងអភិវឌ្ឍ!")

# ចាប់ផ្តើម Server និង Auto-reconnect Polling
keep_alive()

while True:
    try:
        print("Bot កំពុងចាប់ផ្តើមដំណើរការ...")
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"Connection Error: {e}")
        time.sleep(5)
```[cite: 9]
