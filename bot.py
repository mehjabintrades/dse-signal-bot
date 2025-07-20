import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

sample_signals = [
    {"stock": "BATBC", "action": "BUY", "price": "585", "target": "659"},
    {"stock": "WALTONHIL", "action": "BUY", "price": "427.7", "target": "520"},
    {"stock": "AAMRA", "action": "AVERAGE", "price": "17.27", "target": "23"},
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📈 Show Today’s Trade Signals", callback_data='signals')]]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Welcome to Mehjabin DSE Bot!", reply_markup=markup)

async def show_signals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    message = "📊 *Today's Trade Signals:*\n\n"
    for signal in sample_signals:
        message += (
            f"➡️ {signal['action']} | 🏢 {signal['stock']} | 💵 {signal['price']} 🎯 Target: {signal['target']}\n"
        )
    await query.edit_message_text(text=message, parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(show_signals, pattern="signals"))
    app.run_polling()

if __name__ == "__main__":
    main()
