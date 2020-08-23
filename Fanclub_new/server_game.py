import vk_api.vk_api
#from rp_messages import RP

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType




class Server_game:

    def __init__(self, api_token, group_id, server_name: str="Empty"):
        self.pers_num=0
        # Даем серверу имя
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)
        
        # Для использования Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id)
        
        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()
        


    def start(self):
        while True:
            for event in self.long_poll.listen():   # Слушаем сервер
                
            # Пришло новое сообщение
                if event.type == VkBotEventType.MESSAGE_NEW:
                    
                    print(event)
                    #profiles = self.vk_api.users.get(user_id=event.object.message['from_id'], fields = "bdate, city, sex, country, nickname, followers_count, occupation, activities, home_town")
                    #print(profiles)
                    #print('---------------')
                    #print(self.get_user_sex(event.object.message['from_id']))
                    #print('---------------')
                    #print(gifts.get(user_id = event.object.message['from_id'], count=10, offset=2))
                    #print(event.object.message['from_id'])
                    ######print(event)
                    #self.send_msg(event.object.message['from_id'], "отправляю это сообщение с помощью бота ДАБДАБ СЮЮЮДАААА ЛУУТ")
                    
                    #print(event)
                    print("Username: " + self.get_user_name(event.object.message['from_id']) +' '+str(event.object.message['from_id']))
                    #event.object.message['']
                    #print("From: " + self.get_user_city(event.object.message['from_id']))
                    print("Text: " +event.object.message['text'])
                    if 'лука' in event.object.message['text'].lower():
                        #Server.send_message(event.object.message['peer_id'], "картошка пидарас")
                        attachment=0
                        self.vk_api.messages.send(peer_id=event.object.message['peer_id'], message="картошка пидарас это второй чат" , random_id =0, attachment= attachment)
                    #######print("Type: ", end="")
                    #######if event.object.message['id']> 0:
                    ########    print("private message")
                    ########else:
                    ########    print("group message")
                    print(" --- ")
                    #print(event.group_id)
                    #namegrmes= 'ы'
                    
                    #if event.message['text'].lower() == 'кто такой лукашенко?':
                    #    self.send_message(event.object.message['peer_id'], "картошка пидарас")
                    #if 'лука' in event.message['text'].lower():
                    #    self.send_message(event.object.message['peer_id'], "картошка пидарас")
                    #self.send_message(event.object.message['from_id'], namegrmes)
                    #send_massage(vk)
                    #self.send_message(event.object.message['peer_id'], "картошка пидарас")
                    #vk_api.messages.getChat(chat_id='169', message = "картошка пидарас", random_id =0)
                    #RP.messages_check(self.vk_api, event.message['text'], event.object.message['peer_id'], self.get_user_name(event.object.message['from_id']),
                    #event.object.message['from_id'],  self.get_user_sex(event.object.message['from_id']), event.object.message['id'], self.vk, self.pers_num )
                    #self.vk_api = vk_api, event.message['text']=  text, event.object.message['peer_id'] = peer_id, self.get_user_name(event.object.message['from_id']) = user_name, 
                    #event.object.message['from_id'] = user_id, self.get_user_sex(event.object.message['from_id']) = sex, self.vk = vk_session
                

        
    def send_message(self, peer_id, message):
        self.vk_api.messages.send(peer_id=peer_id, message=message, random_id =0)

    
    #def send_keybord(self, peer_id, message):
    #    self.vk_api.messages.send(peer_id=peer_id, message=message, random_id =0, keyboard = keyboard.json)


    def get_user_name(self, user_id):
        """ Получаем имя пользователя"""
        return self.vk_api.users.get(user_id=user_id)[0]['first_name']

    def get_user_city(self, user_id):
        """ Получаем город пользователя"""
        return self.vk_api.users.get(user_id=user_id, fields="city")[0]["city"]['title']

    def get_user_sex(self, user_id):
        """ Получаем пол пользователя"""
        return self.vk_api.users.get(user_id = user_id, fields = 'sex')[0]['sex']
       
        

    #def test(self):
        # Посылаем сообщение пользователю с указанным ID
        #self.send_msg(123495018, "отправляю это сообщение с помощью бота ДАБДАБ СЮЮЮДАААА ЛУУТ") 