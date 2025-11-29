@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.reply_to(message, "Инструкция по работе с ботом: Бот может помочь вам узнать курс любой валюты. "
                          "Отправтье сообщения в виде : <имя валюты, цену которой он хочет узнать> <имя валюты, "
                          "в которой надо узнать цену первой валюты> <количество первой валюты>.Пример: USD RUB 2")
class APIException(Exception):
    pass
@bot.message_handler(commands=["values"])
def values_handler(message):
    bot.reply_to(message,"Доступные валюты: USD,EUR,RUB")


class Converter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise APIException("Количество должно быть числом!")
        if base == quote:
            raise APIException("Нельзя вводить одинаковые валюты!")
        response = requests.get(f"https://v6.exchangerate-api.com/v6/{KEY}/pair/{base}/{quote}")
        data = response.json()
        rate = data.get("conversion_rate")
        result = rate * amount
        return f'Стоисомть {amount} {base} в {quote} равна {result}'
