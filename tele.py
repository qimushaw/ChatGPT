import logging
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the command handler function
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm a bot. Type /help to see my commands.")

# Define the message handler function
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Set up the bot
updater = Updater(token='5955950302:AAFL_RVjydcb1t3IoZTWKJog8aO9ZndxfBE', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Add command handler
dispatcher.add_handler(CommandHandler('start', start))

# Add message handler
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start the bot
updater.start_polling()
