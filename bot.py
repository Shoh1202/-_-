@bot.message_handler(content_types=['text',])
def gate_rate(message: telebot.types.Message):
    try:
        base, quote, amount = message.text.split()
    except ValueError:
        bot.send_message(message.chat.id, "Неправильный формат сообщения."
                                          "Введите данные в формате: USD RUB 10")

        return

    try:
        result =result = Converter.get_price(base, quote, amount)
    except APIException as e:
        bot.send_message(message.chat.id,f"Ошибка: {e}")

    bot.send_message(message.chat.id,result)
bot.infinity_polling()
