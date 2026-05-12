from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from dotenv import load_dotenv
import os
load_dotenv()
import random
import asyncio

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


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

asyncio.run(app.run_polling())




