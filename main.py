from telegram.ext import Updater, MessageHandler, Filters

# Define a function to handle incoming messages
def handle_message(update, context):
    message = update.message.text
    # Your code to process the message goes here
    # Example code to send a reply message
    update.message.reply_text('Thanks for your message!')

def main():
    # Set up the Telegram bot
    updater = Updater('5955950302:AAFL_RVjydcb1t3IoZTWKJog8aO9ZndxfBE', use_context=True)
    dispatcher = updater.dispatcher
    # Set up a message handler to handle incoming messages
    message_handler = MessageHandler(Filters.text, handle_message)
    dispatcher.add_handler(message_handler)
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
