import sqlite3
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = "89296BKDfUHJWpmFBKDfUHJWpmFEnRVuJeoWNdcfvCpnGsfUHJWpmFEnRVuJeoWNdcfvCpnGs"
ADMIN_ID = 8305261625

# Database তৈরি
conn = sqlite3.connect("jbx.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    full_name TEXT,
    payment_method TEXT,
    payment_number TEXT
)
""")

conn.commit()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["💳 Payment Setting"],
        ["📥 Submit File"],
        ["📞 Support ID"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    text = """
⚡ JBX SMART RECEIVER ⚡

স্বাগতম JBX ID RECEIVER BOT-এ।

📌 ফাইল সাবমিট করার আগে Payment Setting সম্পূর্ণ করুন।
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )


async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Support: @Jbx_id_receiver"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("support", support))

    print("Bot Running...")

    app.run_polling()


if __name__ == "__main__":
    main()
