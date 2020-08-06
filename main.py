import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot
import authorization

# Авторизация
authorization.log()


vk_session=authorization.log()[0]
session_api=authorization.log()[1]
longpoll=authorization.log()[2]

def write_msg(user_id, message):
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, 'random_id' : 0})

# Основной цикл
def main():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            print('Новое сообщение:')
            print(f'От пользователя: {event.user_id}    ', end='')

            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))

            print(' Сообщение:', event.text)

if __name__ == '__main__':
    main()
