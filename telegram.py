import facedetecter, telebot, requests

API_TOKEN = "BOT-TOKEN"
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True, content_types=['photo'])
def echo(msg):
    file_info = bot.get_file(msg.photo[len(msg.photo)-1].file_id)
    response = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path))
    
    with open("photo.png", "wb") as file:
        file.write(response.content)
        file.close()
    
    file = facedetecter.search_objects("photo.png")
    
    bot.send_photo(msg.chat.id, file, reply_to_message_id=msg.message_id)

if __name__ == "__main__":
    bot.infinity_polling()