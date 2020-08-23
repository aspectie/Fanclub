#from server import Server
from vk_api.upload import VkUpload
from defs.profile_photo_cr import profile_create
from defs.bitcoin_check import first_check
from defs.get_animetop import anime_top
from game_body.persons import *

from config import vk_api_token
from game_body.inventory import * 
import inspect, os.path
import sys#чисто для меня

class RP:

    def messages_check(vk_api, text, peer_id, user_name, user_id, sex, chat_type, vk_session, pers_num):

        def face_member(user_name,user_id, vk_session):
            file_path = profile_create(user_name, user_id)
            upload = VkUpload(vk_session)
                                        
            photo = upload.photo_messages(file_path)
            owner_id = photo[0]['owner_id']
            photo_id = photo[0]['id']
            access_key = photo[0]['access_key']

            attachment = f'photo{owner_id}_{photo_id}_{access_key}'
            return(attachment)

        filename = inspect.getframeinfo(inspect.currentframe()).filename
        path_pr = os.path.dirname(os.path.abspath(filename))

        #if 'лука' in event.message['text'].lower():
        if 'лука' in text.lower():
            #Server.send_message(event.object.message['peer_id'], "картошка пидарас")
            attachment=0
            vk_api.messages.send(peer_id=peer_id, message="картошка пидарас" , random_id =0, attachment= attachment)

        if 'ку' in text.lower() or 'прив' in text.lower() or 'здаров' in text.lower() or 'погна' in text.lower():
            if chat_type> 0:
                vk_api.messages.send(peer_id=peer_id, message='погнали реально', random_id =0, keyboard=open(path_pr+"\keyboards\kb_start.json", "r", encoding="UTF-8").read())

        if 'казино' in text.lower():
            if chat_type> 0:
                global stage, bit_c
                stage=1
                bit_c = first_check()
                attachment=0
                message ='на данный момент стойость биткойна:'+bit_c+'\nподнимется или опустится?'
                vk_api.messages.send(peer_id=peer_id, message=message , random_id =0, attachment= attachment, keyboard=open(path_pr+ "\keyboards\kb_bit.json", "r", encoding="UTF-8").read())

        if 'поднимится' in text.lower() and stage==1:
           
            bit_c_sec = first_check()
            while bit_c_sec==bit_c:
                message='ещё не обновился...'
                vk_api.messages.send(peer_id=peer_id, message=message , random_id =0)
                bit_c_sec = first_check()
            if bit_c>bit_c_sec:
                message='ты проиграл\nбиткоин упал и теперь стоит:'+bit_c_sec
                vk_api.messages.send(peer_id=peer_id, message=message , random_id =0)
            else:
                message='ты победил\nбиткоин поднялся и теперь стоит:'+bit_c_sec
                vk_api.messages.send(peer_id=peer_id, message=message , random_id =0)
            stage=0

        if '!профиль' == text.lower():#отправляет твою ебучку нужно добавить со всеми параметрами и тд
            file_path = profile_create(user_name, user_id)
            upload = VkUpload(vk_session)
                                        
            photo = upload.photo_messages(file_path)
            owner_id = photo[0]['owner_id']
            photo_id = photo[0]['id']
            access_key = photo[0]['access_key']

            attachment = f'photo{owner_id}_{photo_id}_{access_key}'
            message = 'камней:'+money_show(user_id)+'\n'+equiped_items_show(user_id)
            
            vk_api.messages.send(peer_id=peer_id, message=message , random_id =0, attachment= attachment)

        if 'обоссать всех' in text.lower():
            if sex ==2 or sex ==0:
                message='[id{}|{}]'.format(user_id, user_name) + ' обоссал всех'
                vk_api.messages.send(peer_id=peer_id, message=message , random_id =0)
            else:
                message='[id{}|{}]'.format(user_id, user_name) + ' обоссала всех'
                vk_api.messages.send(peer_id=peer_id, message=message , random_id =0)

        if 'аниме топ' in text.lower():
            message=anime_top()
            vk_api.messages.send(peer_id=peer_id, message=message , random_id =0)

        #==================================================
        #messages for game
        if  text.lower()=='собираю пати':
            global raid_stage
            raid_stage=True
            attachment = face_member(user_name,user_id, vk_session)
            message= user_name+' собирает пати на рейд'
            vk_api.messages.send(peer_id=peer_id, message=message , random_id =0, attachment= attachment, keyboard=open(path_pr+ "\keyboards\kb_party_collect.json", "r", encoding="UTF-8").read())
            
        
        if text.lower()=='я дд' or text.lower()=='я танк'or  text.lower()=='я хилер' and raid_stage==True:
            person1=person_create(user_id, vk_api, text, peer_id)
            if person1.player_check(user_id)=='пустить':
                attachment = face_member(user_name,user_id, vk_session)
                message= user_name+' присоединился к рейду'

        if text.lower()=='запускаем подземелье' and raid_stage==True:
            raid_stage==False
            from server_game import Server_game
            from config import vk_api_token


            server_game1 = Server_game(vk_api_token, 186777464, "server_game1")
          
            server_game1.start()



        if '!учавствую' in text.lower():
            #server_sec1 = Server_sec(vk_api_token, 186777464, "server_sec1")
            #server_sec1.start()  второй поток для стадии битвы
            pers_num+=1
            #class_p = text.split()[1]
            #person1=person_create(user_id, vk_api, class_p, peer_id)
            person1=person_create(user_id, vk_api, peer_id)
            person1.show_player_list()
            person1.data_show(user_id)

        #========================================================
        #inventory message
        if  '!надеть' in text.lower() and chat_type > 0:
            message = item_equip(user_id, text.split()[1])
            vk_api.messages.send(peer_id=peer_id, message=message , random_id =0)

        if text.lower() == '!сундук':
            message = inventory_show(user_id)
            vk_api.messages.send(peer_id=peer_id, message=message , random_id =0)
            
            
        if text.lower() == '!инвентарь':
            message = inventory_show(user_id)
            vk_api.messages.send(peer_id=peer_id, message=message , random_id =0)

        if text.lower() == 'открыть кейс' and chat_type > 0:
            global loot, sell_check
            sell_check=True
            loot = case_open(user_id)
            print('луут:'+str(loot))
            message = 'вам выпало:'+ loot[0]
            vk_api.messages.send(peer_id=peer_id, message=message , random_id =0, keyboard=open(path_pr+"\keyboards\kb_sell.json", "r", encoding="UTF-8").read())

            #inventory_upload(user_id)

        if text.lower() == 'продать' and chat_type > 0 and sell_check==True:
            sell_item(user_id, loot[1])
            sell_check=False
            message = 'теперь у тебя:' +str(money_show(user_id))+'🗿 камней'
            vk_api.messages.send(peer_id=peer_id, message=message , random_id =0)

            
        if text.lower() =='!!продать':
            item_id = text.split()[1]
            
            sell_item(user_id, item_id)

        if text.lower() =='!офай!':
            sys.exit()
        
        

            
