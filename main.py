import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
import os

# Set up OpenAI API key
openai.api_key = os.environ['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']

# Define function to generate response using GPT
def generate_response(text):
    prompt = f"User: {text}\nAI:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=50,
        n=1,
        stop=None,
        timeout=20,
    )
    message = response.choices[0].text.strip()
    return message

# Define function to handle user messages
def handle_message(update, context):
    text = update.message.text
    response = generate_response(text)
    update.message.reply_text(response)

# Define main function to start the bot
def main():
    # Set up Telegram bot and updater
    token = os.environ['6133300401:AAH-K0ljX3mi9wGC3jBOrRLybc2yOn58V5I']
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # Define handlers for commands and messages
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)

    # Add handlers to dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until interrupted
    updater.idle()

# Define function to handle /start command
def start(update, context):
    update.message.reply_text("Hi! I'm a GPT-based chatbot. How can I assist you today?")

if name == 'main':
    main()
