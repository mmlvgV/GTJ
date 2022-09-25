'''Модуль для спама сообщениями в каналах дискорда'''

import random
import asyncio

import discord


class Client(discord.Client):
    '''Основной класс клиента'''

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    # Ивенты

    async def on_connect(self) -> None:
        '''Функция действия при реагировании на подключении бота к дискорду'''
        print('''!! ВАЖНО !! Селф-боты запрещены TOS discord.
         Если Вы получите блокировку аккаунта - создатель программы не будет ответственным за это''')
        print('Подождите несколько секунд пока бот не запустится')

    async def on_ready(self) -> None:
        '''Функция действия при реагировании на готовность бота к использованию'''

        try:
            open('spam.txt', 'r', encoding='utf-8').close()
        except FileNotFoundError:
            print('''Создайте файл spam.txt (в папке с программой) и запишите туда текст,
             который будет отправлятся при спаме (не больше 2000 символов) 
             и перезапустите программу''')

            return

        while True:
            form = input('>')

            if str(form).startswith('spam'):
                arguments = str(form).split()

                try:
                    channel = await self.fetch_channel(arguments[1])
                except IndexError:
                    print('''Неправильно указаны аргументы.
                     Пример использования: spam ID''')
                except discord.Forbidden:
                    print('''Не удалось получить объект канала.
                     Возможно пользователя нет на сервере''')
                finally:
                    pass

                with open('spam.txt', 'r', encoding='utf-8') as _file:
                    _data = str(_file.read())

                print('Чтобы прекратить спам выключите программу')

                QUANTITY = 0

                while True:
                    try:
                        await channel.send(_data)

                        QUANTITY += 1
                    except discord.Forbidden:
                        print('''Не удалось получить объект канала.
                        Возможно пользователя нет на сервере''')
                    finally:
                        pass
                    
                    print(f'Отправлено {QUANTITY} сообщений')

                    await asyncio.sleep(random.uniform(0.1, 1))


if __name__ == '__main__':
    client = Client()

    client.run(input('Токен: '), bot=False)
