# Функция translate обращается к бесплатному API для перевода текста на требуемый язык. В качестве аргументов функция
# принимает текст для перевода и язык, на который требуется перевести текст. Язык текста определяется автоматически.
# Качество перевода страдает, однако наличие бесплатного API позволяет автоматизировать перевод большого количества
# разрозненных текстов на различных языках для того, чтобы сформировать общее представление о содержании данных текстов.

import requests


def translate(txt, language):
    url = 'https://ftapi.pythonanywhere.com/translate'
    params = {'dl': language, 'text': txt}
    response = requests.get(url, params=params)
    return response.json()['destination-text']


text = ('London is the capital of the United Kingdom of Great Britain and Northern Ireland. Big Ben and Westminster '
        'Abbey are the most famous sights of London.')
language = 'ru'
print(translate(text, language))
