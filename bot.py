import os
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI()

# Build Telegram async application
application = (
    Application.builder()
    .token(TOKEN)
    .build()
)

# ----- Handlers -----
async def start(update: Update, context):
    await update.message.reply_text("Hello! Async webhook bot is working 🚀")

application.add_handler(CommandHandler("start", start))


# ----- Webhook endpoint -----
@app.post(f"/webhook/{TOKEN}")
async def telegram_webhook(request: Request):
    json_data = await request.json()
    update = Update.de_json(json_data, application.bot)
    await application.process_update(update)
    return {"status": "ok"}


@app.get("/")
async def home():
    return {"status": "running"}
