import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot


# API-ключ
token = '5f02dd28cbc30080117ddf19f6b597e62803bd37da5d4839c59f62cc0f2ad961abc9dac18249a37dd5d4d'

# Авторизация
vk_sesion = vk_api.VkApi(token = token)
session_api = vk_sesion.get_api()
longpoll = VkLongPoll(vk_sesion)

def write_msg(user_id, message):
    vk_sesion.method('messages.send', {'user_id': user_id, 'message': message, 'random_id' : 0})

# Основной цикл
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))

            print(' Text: ', event.text)