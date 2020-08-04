from profile import _profile
import vk_api
import vk
from api_keys import access_token

session = vk.Session(access_token = access_token)
version = '5.89'

vk_api = vk.API(session, v = version)


# Основной класс бота
class VkBot:
    # Инициализация
    def __init__(self, user_id):
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name(user_id)
        self._COMMANDS = ["привет", "биба"]

    def _get_user_name(self, user_id):
        user_obj = vk_api.users.get(user_id = user_id)
        user_name = user_obj[0]['first_name']

        return user_name

    def new_message(self, message):
        # Привет
        if message.lower() == self._COMMANDS[0]:
            return f"ЭэээээШКерреееееее"

        # Размер бибы
        if message.lower() == self._COMMANDS[1]:
            #_profile.dick_size(self)
            size = _profile.dick_size_calculate(self)
            return f"Твоя биба {size}см)))))"

        else:
            return "Ты тупой?"