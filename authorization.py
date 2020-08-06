from api_keys import token, group_id
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType



mass = []
def log():
    
    vk_session = vk_api.VkApi(token = token)
    session_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    mass.append(vk_session)
    mass.append(session_api)
    mass.append(longpoll)
    return mass
