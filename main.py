import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot
import Enter_values


# API-ключ

token = Enter_values.token
group_id=Enter_values.group_id
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