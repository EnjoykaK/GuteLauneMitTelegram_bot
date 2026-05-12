print("Bot started")
from telegram import Update
from telegram._utils.types import ReplyMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from dotenv import load_dotenv
import os
load_dotenv()
import random

TOKEN = os.getenv("TOKEN")

async def button(update: Update, context:ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Witz", callback_data="joke")],
        [InlineKeyboardButton("Kompliment", callback_data="compliment")],
        [InlineKeyboardButton("Motivation", callback_data="motivation")]
    ]
    if query.data == "joke":
        jokes = ["Warun kann ein Fahrrad nicht umfallen? Da es zwei Räder hat! :)",
        "Was ist orange und läuft durch den Wald? Eine Wanderine! :)",
        "Warum können Geister so schlecht lügen? Wiel sie durchschaut werden! :)"
        ]
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("Witz", callback_data="joke")],
            [InlineKeyboardButton("Kompliment", callback_data="compliment")],
            [InlineKeyboardButton("Motivation", callback_data="motivation")]
        ])
        await query.message.reply_text(random.choice(jokes), reply_markup=reply_markup)

    elif query.data == "compliment":
        compliments = ["Du bist wie eine Sonnenschein! ;)", 
                       "Du bist großartig! ;)",
                       "Du bist ein seht guter Mensch! Weiss es! ;)"
                       ]
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("Witz", callback_data="joke")],
            [InlineKeyboardButton("Kompliment", callback_data="compliment")],
            [InlineKeyboardButton("Motivation", callback_data="motivation")]
        ])
        await query.message.reply_text(random.choice(compliments), reply_markup=reply_markup)

    elif query.data == "motivation":
        motivations = ["Du schaffst das!", 
                       "Gib nicht auf, du bist stärker als du denkst!", 
                       "Jeder Tag ist eine neue Chance, um deine Ziele zu erreichen! Schritt für schritt kommst du voran!"
                       ]
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("Witz", callback_data="joke")],
            [InlineKeyboardButton("Kompliment", callback_data="compliment")],
            [InlineKeyboardButton("Motivation", callback_data="motivation")]
        ])
        await query.message.reply_text(random.choice(motivations), reply_markup=reply_markup)

async def start(update: Update, context: ContextTypes. DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Witz", callback_data="joke")],
        [InlineKeyboardButton("Kompliment", callback_data="compliment")],
        [InlineKeyboardButton("Motivation", callback_data="motivation")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
            "Hallo! Ich bin dein Bot für Gute Laune! :)\n\n"
            "Nütze die Befehle /joke, um einen Witz zu bekommen\n"
            "Nütze den Befehl /compliment, um sich sicherer zu fühlen\n"
            "Nütze den Befehl /motivation, um motiviert zu sein\n",
            reply_markup=reply_markup
        )

async def joke (update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = [
        "Warun kann ein Fahrrad nicht umfallen? Da es zwei Räder hat! :)",
        "Was ist orange und läuft durch den Wald? Eine Wanderine! :)",
        "Warum können Geister so schlecht lügen? Wiel sie durchschaut werden! :)",
    ]
    await update.message.reply_text(random.choice(jokes))

async def compliment (update: Update, context: ContextTypes.DEFAULT_TYPE):
    compliments = [
        "Du bist wie eine Sonnenschein! ;)",
        "Du bist großartig! ;)",
        "Du bist ein seht guter Mensch! Weiss es! ;)"
    ]
    await update.message.reply_text(random.choice(compliments))

async def motivation (update: Update, context: ContextTypes.DEFAULT_TYPE):
    motivations = [
        "Du schaffst das!",
        "Gib nicht auf, du bist stärker als du denkst!",
        "Jeder Tag ist eine neue Chance, um deine Ziele zu erreichen! Schritt für schritt kommst du voran!"
    ]
    await update.message.reply_text(random.choice(motivations))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("joke", joke))
app.add_handler(CommandHandler("compliment", compliment))
app.add_handler(CommandHandler("motivation", motivation))
app.add_handler(CommandHandler("help", help))
app.add_handler(CallbackQueryHandler(button))
print("Bot läuft")
import asyncio
asyncio.run(app.run_polling())




