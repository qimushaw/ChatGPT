
from transformers import pipeline

# Replace YOUR_BOT_TOKEN with the token provided by BotFather
updater = Updater(token='5955950302:AAFL_RVjydcb1t3IoZTWKJog8aO9ZndxfBE', use_context=True)

# Define a function to generate responses using GPT
def generate_response(text):
    # Load the GPT-2 model with default settings
    generator = pipeline('text-generation', model='gpt2')

    # Generate a response to the input text
    response = generator(text, max_length=50)[0]['generated_text']

    return response

# Define a function to handle incoming messages
def handle_message(update, context):
    text = update.message.text
    response = generate_response(text)
    update.message.reply_text(response)

# Create a message handler and register it with the updater
message_handler = MessageHandler(Filters.text, handle_message)
updater.dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()

