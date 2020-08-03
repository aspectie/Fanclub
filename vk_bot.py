import bs4
import requests
from profile import _profile

# Основной класс бота
class VkBot:
    # Инициализация
    def __init__(self, user_id):
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._COMMANDS = ["ПРИВЕТ", "БИБА"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    @staticmethod
    def _clean_all_tag_from_str(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result

    def new_message(self, message):
        # Привет
        if message.upper() == self._COMMANDS[0]:
            return f"ЭэээээШКерреееееее"

        # Размер бибы
        if message.upper() == self._COMMANDS[1]:
            #_profile.dick_size(self)
            size = _profile.dick_size_calculate(self)
            return f"Твоя биба {size}см)))))"

        else:
            return "Ты тупой?"