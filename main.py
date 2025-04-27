
import telebot

TOKEN = '7697075490:AAFhAiwUQiVKYaRNh36daSJWgJBZ-9O-_t0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    import datetime

    text = message.text.lower()
    if "ложусь в" in text:
        try:
            time_text = text.split("ложусь в")[1].strip()
            hour, minute = map(int, time_text.split(":"))
            sleep_start = datetime.datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
            
            cycle_minutes = 90
            recommendations = []
            for cycles in range(3, 7):
                wake_time = sleep_start + datetime.timedelta(minutes=cycles * cycle_minutes)
                recommendations.append(f"{cycles} цикл(ов): {wake_time.strftime('%H:%M')}")

            bot.reply_to(message, "Лучшие времена для пробуждения:")
        
" + "\n".join(recommendations))
        except Exception as e:
            bot.reply_to(message, "Не могу разобрать время. Напиши, например: 'Я ложусь в 23:40'")
    else:
        bot.reply_to(message, "Напиши, во сколько ты ложишься спать, например: 'Я ложусь в 23:40'")

bot.polling()
