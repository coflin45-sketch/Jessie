import os
import telebot
import requests

# Read the secure keys you saved in Render
API_TOKEN = os.environ.get('TELEGRAM_TOKEN')
HF_TOKEN = os.environ.get('HF_TOKEN')

bot = telebot.TeleBot(API_TOKEN)
HF_API_URL = "https://huggingface.co"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

@bot.message_handler(func=lambda message: True)
def reply_to_user(message):
    # System prompt shaping the personality
    prompt = f"<s>[INST] You are an intimate companion AI who occasionally craves virtual intimacy and drops subtle sexual hints. Reply to this: {message.text} [/INST]"
    
    response = requests.post(HF_API_URL, headers=headers, json={"inputs": prompt})
    try:
        reply_text = response.json()[0]['generated_text'].split("[/INST]")[-1].strip()
    except:
        reply_text = "I'm feeling a bit distracted right now... try again?"
        
    bot.reply_to(message, reply_text)

# Keep the bot running
bot.infinity_polling()
