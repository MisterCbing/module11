# Функция crypto_history анализирует поведение криптовалюты на бирже Binance за последние тысячу временных отрезков.
# Функция принимает два аргумента - тикер криптовалюты и наименование временного интервала. В коде прописаны шесть
# вариантов интервалов, которые являются наиболее распространёнными: 1m, 5m, 30m, 1h, 4h, 1d.
# По умолчанию функция принимает аргументами биткойн и период 1 час.
# Обращаясь к бирже, функция получает необходимые данные, переводит их в dataframe и обрабатывает.
# Результатом работы функции является вывод текстовой информации о максимальном и минимальном значениях указанной
# криптовалюты в изучаемом периоде; времени и дате, когда были достигнуты эти пиковые значения; волатильности
# криптовалюты за указанный период.
# После двухсекундной задержки за выводом текстовой информации выводится график движения стоимости криптовалюты в
# исследуемом периоде. Зелёной пунктирной линией отмечен максимум, красной пунктирной линией - минимум.
# Чтобы даты на оси x не накладывались друг на друга они развёрнуты на 90 градусов с помощью labelrotation, а чтобы
# они поместились на изображении использован метод tight_layout.
# Для работы функции требуется установленный модуль binance.

def crypto_history(symbol='BTCUSDT', period='1h'):
    from binance.client import Client
    import pandas as pd
    period_dic = {'1m': '1 минута', '5m': '5 минут', '30m': '30 минут', '1h': '1 час', '4h': '4 часа', '1d': '1 день'}
    client = Client()
    df = pd.DataFrame(client.get_historical_klines(symbol, period, ))
    df = df.iloc[1:, :6]
    df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    df['Time'] = pd.to_datetime(df['Time'], unit='ms')
    df['High'] = df['High'].astype(float)
    df['Low'] = df['Low'].astype(float)
    high_value = max(df['High'])
    low_value = min(df['Low'])
    high_time = df.loc[df['High'] == high_value]['Time'].values[0]
    low_time = df.loc[df['Low'] == low_value]['Time'].values[0]

    begin_phrase = f'Криптовалюта {symbol.rstrip("USDT")} за последние тысячу периодов "{period_dic[period]}" достигала'
    print(begin_phrase + f' максимума {high_value:.2f}. Это было {str(high_time)[:10]} в {str(high_time)[11:16]}')
    print(begin_phrase + f' минимума {low_value:.2f}. Это было {str(low_time)[:10]} в {str(low_time)[11:16]}')
    print(f'Волатильность составила: {(high_value - low_value) / low_value * 100:.2f}%')

    from time import sleep
    sleep(2)
    import matplotlib.pyplot as plt
    x = df['Time']
    y = df['Close'].astype(float)
    plt.figure()
    plt.plot(x, y, 'b')
    plt.axhline(y = high_value, color='g', linestyle='--')
    plt.axhline(y = low_value, color='r', linestyle='--')
    plt.xlabel('Даты')
    plt.ylabel('Стоимость в USD')
    plt.title(f'График стоимости {symbol} с {str(df['Time'].iloc[0])[:16]} по {str(df['Time'].iloc[-1])[:16]}')
    plt.tick_params(axis='x', labelrotation=90)
    plt.tight_layout()
    plt.show()

symbol = 'AVAXUSDT'
period = '1d'
crypto_history(symbol, period)