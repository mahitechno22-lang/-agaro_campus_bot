from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN =8233984540:AAEyAOwtYnDkPeFpnYnjuRSj3gG30SqAts0

# MAIN MENU
main_menu = [
    ["1️⃣ ስለ አጋሮ ካምፖስ"],
    ["2️⃣ የመጀመሪያ ዲግሪ", "3️⃣ ሁለተኛ ዲግሪ"],
    ["4️⃣ እኛን ለማግኘት"]
]

# SUB MENUS
ug_menu = [
    ["📘 ትምህርቶች", "💰 ክፍያ"],
    ["🔙 Back"]
]

pg_menu = [
    ["📗 ትምህርቶች", "💰 ክፍያ"],
    ["🔙 Back"]
]

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["state"] = "main"
    await update.message.reply_text(
        "እንኳን ወደ አጋሮ ካምፖስ ቦት በደህና መጡ!",
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )

# MESSAGE HANDLER
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    state = context.user_data.get("state")

    # MAIN MENU
    if text == "1️⃣ ስለ አጋሮ ካምፖስ":
        await update.message.reply_text(
            "አጋሮ ካምፖስ በከፍተኛ ደረጃ ትምህርት የሚሰጥ ተቋም ነው።"
        )

    elif text == "2️⃣ የመጀመሪያ ዲግሪ":
        context.user_data["state"] = "ug"
        await update.message.reply_text(
            "የመጀመሪያ ዲግሪ Menu",
            reply_markup=ReplyKeyboardMarkup(ug_menu, resize_keyboard=True)
        )

    elif text == "3️⃣ ሁለተኛ ዲግሪ":
        context.user_data["state"] = "pg"
        await update.message.reply_text(
            "ሁለተኛ ዲግሪ Menu",
            reply_markup=ReplyKeyboardMarkup(pg_menu, resize_keyboard=True)
        )

    elif text == "4️⃣ እኛን ለማግኘት":
        await update.message.reply_text(
            "📞 0911XXXXXX\n"
            "📮 PO Box: 12345\n"
            "📧 Email: agaro@gmail.com"
        )

    # UG SUB MENU
    elif state == "ug":
        if text == "📘 ትምህርቶች