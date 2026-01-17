import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛩️ Aviator Demo Bot\n\n"
        "⚠️ Demo signals only\n"
        "Use /signal"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    value = round(random.uniform(1.2, 4.5), 2)
    await update.message.reply_text(
        f"🤖 AI Analysis Complete\n\n"
        f"🎯 Suggested Exit: {value}x\n"
        f"⚠️ Entertainment only"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

app.run_polling()
