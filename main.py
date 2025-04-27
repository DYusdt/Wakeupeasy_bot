import telebot

bot = telebot.TeleBot('7697075490:AAFhAiwUQiVKYaRNh36daSJWgJBZ-9O-_t0')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне время, во сколько ты ложишься спать (например: 23:00).")

@bot.message_handler(func=lambda message: True)
def calculate_sleep_cycles(message):
    try:
        import datetime

        sleep_time = message.text.strip()
        sleep_hour, sleep_minute = map(int, sleep_time.split(':'))
        sleep_datetime = datetime.datetime.now().replace(hour=sleep_hour, minute=sleep_minute, second=0, microsecond=0)

        cycle_minutes = 90
        recommendations = []

        for cycles in range(3, 7):
            wake_up_time = sleep_datetime + datetime.timedelta(minutes=cycle_minutes * cycles)
            recommendations.append(wake_up_time.strftime("%H:%M"))

        bot.reply_to(
            message,
            "Лучшие времена для пробуждения:\n" + "\n".join(recommendations)
        )
    except Exception as e:
        bot.reply_to(message, "Произошла ошибка. Пожалуйста, отправь время в формате ЧЧ:ММ.")

bot.infinity_polling()
