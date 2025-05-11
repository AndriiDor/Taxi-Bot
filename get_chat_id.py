from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = '8021547206:AAFLTVFmgGb5qOxAMh-CCGha_Kn-udSQ08k'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f'Your chat ID is: {chat_id}')

if __name__ == '__main__':
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
