import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from keep_alive import keep_alive

# ដាក់ Token ដែលទទួលបានពី @BotFather នៅទីនេះ
API_TOKEN = '8933232129:AAH3bZPylnAug8uIe2G9nFlXQN9ysbtiLC0'
bot = telebot.TeleBot(API_TOKEN)

# រក្សាទុកទិន្នន័យអ្នកប្រើប្រាស់បណ្ដោះអាសន្ន (សម្រាប់ការសាកល្បង)
user_balances = {}
user_orders = {}

# ១. បង្កើតប៊ូតុងម៉ឺនុយខាងក្រោម (Reply Keyboard) ដូចក្នុងរូបភាព
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("🎮 បញ្ចូលទឹកប្រាក់ហ្គេម"), KeyboardButton("🔥 កញ្ចប់ពេញនិយម"),
        KeyboardButton("📦 ប្រវត្តិ និងពិនិត្យការបញ្ជាទិញ"),
        KeyboardButton("💳 បញ្ចូលទឹកប្រាក់"), KeyboardButton("💰 គណនីរបស់ខ្ញុំ"),
        KeyboardButton("🖼️ តារាងតម្លៃកញ្ចប់ហ្គេម"),
        KeyboardButton("🎁 បញ្ចូលកូដរង្វាន់"), KeyboardButton("🤝 ណែនាំមិត្តភក្តិ"),
        KeyboardButton("📖 របៀបប្រើប្រាស់"), KeyboardButton("🌐 ប្តូរភាសា"),
        KeyboardButton("📞 ទាក់ទងអ្នកគ្រប់គ្រង")
    )
    return markup

# ២. បង្កើតប៊ូតុងជ្រើសរើសកញ្ចប់ពេជ្រ (Inline Keyboard)
def mlbb_packages():
    markup = InlineKeyboardMarkup(row_width=1)
    packages = [
        ("💎 ទទួលបាន 12 ពេជ្រ — តម្លៃ $0.34", "buy_12_0.34"),
        ("💎 ទទួលបាន 14 ពេជ្រ — តម្លៃ $0.36", "buy_14_0.36"),
        ("💎 ទទួលបាន 10+1 ពេជ្រ — តម្លៃ $0.37", "buy_11_0.37"),
        ("💎 ទទួលបាន 19 ពេជ្រ — តម្លៃ $0.53", "buy_19_0.53"),
        ("💎 ទទួលបាន 20+2 ពេជ្រ — តម្លៃ $0.74", "buy_22_0.74")
    ]
    for text, callback in packages:
        markup.add(InlineKeyboardButton(text, callback_data=callback))
    return markup

# ពេលអ្នកប្រើប្រាស់ចុច /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id not in user_balances:
        user_balances[user_id] = 0.00
    
    welcome_text = (
        f"សួស្តី **{message.from_user.first_name}**! 👋\n"
        "ស្វាគមន៍មកកាន់ប្រព័ន្ធបញ្ចូលទឹកប្រាក់ហ្គេមស្វ័យប្រវត្តិ។\n"
        "សូមជ្រើសរើសម៉ឺនុយខាងក្រោមដើម្បីបន្ត៖"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=main_menu())

# គ្រប់គ្រងការចុចប៊ូតុងម៉ឺនុយខាងក្រោម
@bot.message_handler(func=lambda message: True)
def handle_menu(message):
    user_id = message.from_user.id
    text = message.text

    if text == "🎮 បញ្ចូលទឹកប្រាក់ហ្គេម":
        msg = (
            "⚔️ **ហ្គេម៖ Mobile Legends (Global) (ទំព័រ 1/7)**\n"
            "📌 តម្រូវឲ្យមានទាំង៖ **Player ID (user_id)** និង **Zone ID (zone_id)**\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "👇 សូមចុចជ្រើសរើសកញ្ចប់ខាងក្រោមដើម្បីបញ្ចូលទឹកប្រាក់៖"
        )
        bot.send_message(message.chat.id, msg, parse_mode="Markdown", reply_markup=mlbb_packages())

    elif text == "💰 គណនីរបស់ខ្ញុំ":
        bal = user_balances.get(user_id, 0.00)
        bot.send_message(
            message.chat.id,
            f"👤 **ព័ត៌មានគណនី**\n🆔 ID: `{user_id}`\n💵 សមតុល្យទឹកប្រាក់៖ **${bal:.2f}**",
            parse_mode="Markdown"
        )

    elif text == "💳 បញ្ចូលទឹកប្រាក់":
        bot.send_message(
            message.chat.id,
            "🏦 **វិធីសាស្ត្របញ្ចូលទឹកប្រាក់ (KHQR / ABA)**\n"
            "សូមវេរប្រាក់មកកាន់គណនី `000 123 456` រួចផ្ញើវិក្កយបត្រមកកាន់ Admin ដើម្បីបញ្ចូលទឹកប្រាក់។",
            parse_mode="Markdown"
        )

    elif text == "📞 ទាក់ទងអ្នកគ្រប់គ្រង":
        bot.send_message(message.chat.id, "📩 សូមទាក់ទងទៅកាន់៖ @YourAdminUsername")

    else:
        bot.send_message(message.chat.id, "មុខងារនេះកំពុងអភិវឌ្ឍ! សូមជ្រើសរើសម៉ឺនុយផ្សេងទៀត។")

# គ្រប់គ្រងពេលអ្នកប្រើប្រាស់ចុចជ្រើសរើសកញ្ចប់ពេជ្រ
@bot.callback_query_handler(func=lambda call: call.data.startswith("buy_"))
def handle_package_selection(call):
    data = call.data.split("_")
    diamonds = data[1]
    price = float(data[2])
    
    msg = bot.send_message(
        call.message.chat.id,
        f"💎 អ្នកបានជ្រើសរើសកញ្ចប់ **{diamonds} ពេជ្រ** (តម្លៃ **${price}**)\n\n"
        "✍️ សូមវាយបញ្ចូល **Player ID** និង **Zone ID** របស់អ្នក\n"
        "ឧទាហរណ៍៖ `123456789 1234`",
        parse_mode="Markdown"
    )
    bot.register_next_step_handler(msg, process_game_id, diamonds, price)

# ទទួលយក ID ហ្គេមពីអ្នកប្រើប្រាស់
def process_game_id(message, diamonds, price):
    game_info = message.text
    user_id = message.from_user.id
    bal = user_balances.get(user_id, 0.00)

    if bal < price:
        bot.send_message(
            message.chat.id,
            f"❌ **ទឹកប្រាក់ក្នុងគណនីមិនគ្រប់គ្រាន់ទេ!**\n"
            f"តម្លៃកញ្ចប់៖ **${price}** | សមតុល្យរបស់អ្នក៖ **${bal:.2f}**\n"
            "សូមចុចប៊ូតុង **💳 បញ្ចូលទឹកប្រាក់** ជាមុនសិន។",
            parse_mode="Markdown"
        )
    else:
        user_balances[user_id] -= price
        bot.send_message(
            message.chat.id,
            f"✅ **ការបញ្ជាទិញជោគជ័យ!**\n"
            f"🎮 ID ហ្គេម៖ `{game_info}`\n"
            f"💎 កញ្ចប់៖ **{diamonds} ពេជ្រ**\n"
            f"💵 កាត់ទឹកប្រាក់៖ **${price}**\n"
            "ប្រព័ន្ធកំពុងបញ្ជូនពេជ្រទៅក្នុងគណនីរបស់អ្នក...",
            parse_mode="Markdown"
        )

import time

# កូដការពារការដាច់ connection (Auto-reconnect loop)
while True:
    try:
        print("Bot កំពុងចាប់ផ្តើមដំណើរការ polling...")
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"មានបញ្តាបណ្តាញដាច់ (Error): {e}")
        print("កំពុងព្យាយាមតភ្ជាប់ឡើងវិញក្នុងរយៈពេល 5 វិនាទី...")
        time.sleep(5)
