from requests import get, utils
response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

user = input('Введите код валюты: ')

def currency_rates(currency):
    currency_in_content = content[content.find(currency):content.find(currency)+3]
    if currency == currency_in_content:
        currency_str = content[content.find(currency)+40:content.find(currency)+90]
        value_str = ''
        for i in currency_str:
            if i.isdigit():
                value_str = value_str + i
        print(f'{currency} по курсу ЦБРФ -  {float(value_str) / 10000} руб.')
    else:
        print('Введите верный код валюты.')

currency_rates(user.upper())