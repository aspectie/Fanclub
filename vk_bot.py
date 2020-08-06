from profile import _profile
import vk_api
import vk
from api_keys import token
from defs.profile_photo_cr import profile_create
import authorization
from vk_api.upload import VkUpload


#import authorization

session = vk.Session(access_token = token)
version = '5.89'

vk_api = vk.API(session, v = version)

vk_session=authorization.log()[0]
#vk_sesion = vk_api.VkApi(token = token)


# Основной класс бота


class VkBot:
    # Инициализация

    def __init__(self, user_id):
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name(user_id)
        self._COMMANDS = ["привет", "биба", "профиль"]

    def _get_user_name(self, user_id):
        user_obj = vk_api.users.get(user_id = user_id)
        user_name = user_obj[0]['first_name']

        return user_name

    #вызывать эту функцию в функции new_message(), когда необходимо отправить картинку
    
    def picture_send(username1, userid1):
       
        file_path = profile_create(username1)
        upload = VkUpload(vk_session)
                                        
        photo = upload.photo_messages(file_path)
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']

        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
            
        vk_session.method('messages.send', {'user_id':  userid1, 'message': 'бе', 'random_id' : 0, 'attachment':attachment})



    def new_message(self, message):
        # Привет
        if message.lower() == self._COMMANDS[0]:
            return f"ЭэээээШКерреееееее"

        # Размер бибы
        if message.lower() == self._COMMANDS[1]:
            #_profile.dick_size(self)
            size = _profile.dick_size_calculate(self)
            return f"Твоя биба {size}см)))))"
        if message.lower() == self._COMMANDS[2]:
            VkBot.picture_send(self._USERNAME, self._USER_ID)
            x='ы'
            return x
    
        else:
            return "Ты тупой?"
     