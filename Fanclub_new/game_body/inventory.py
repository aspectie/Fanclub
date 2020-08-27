import shelve
import random
from game_body.equip_list import *
import inspect, os.path

def inventory_unload(user_id, item_id):#загрузить доп. items в базу данных
    shelvefile = shelve.open(path_get())
    
    all_inv = shelvefile['inventories']
    all_inv.setdefault(user_id, [])
    all_inv[user_id].append(item_id)
    shelvefile['inventories']=all_inv
    #shelvefile.close()

def sell_item(user_id, item_id):
    shelvefile = shelve.open(path_get())
    money_list = shelvefile['money']
    all_inv = shelvefile['inventories']
    #print(str(all_inv[user_id])+' до удаления')
    
    if weap_list[item_id]['rare']=='common':
        q_money=10
    if weap_list[item_id]['rare']=='legendary':
        q_money=40
    
    all_inv[user_id].remove(item_id)
    #print(str(all_inv[user_id])+' после')
    shelvefile['inventories']=all_inv
    shelvefile['money']=money_add(user_id, q_money, money_list)
    #добавить деняг
    #shelvefile.close()
    
def inventory_show(user_id):
    shelvefile = shelve.open(path_get())
    all_inv = shelvefile['inventories']
    print()
    message_weap=''
    message_hat=''
    message_chest=''
    message_Legs=''
    message_Feet=''
   
    for equip in all_inv[user_id]:
        if weap_list[equip]['type'] == 'weapon':
            message_weap+=weap_list[equip]['name']+'('+equip+')|||'+'⚔'+ weap_list[equip]['damage']+'🛡'+weap_list[equip]['armor']+'💊'+weap_list[equip]['heal_lvl']+'\n'
        if weap_list[equip]['type'] == 'Head':
            message_hat+=weap_list[equip]['name']+'('+equip+')|||'+'⚔'+ weap_list[equip]['damage']+'🛡'+weap_list[equip]['armor']+'💊'+weap_list[equip]['heal_lvl']+'\n'
        if weap_list[equip]['type'] == 'Chest':
            message_chest+=weap_list[equip]['name']+'('+equip+')|||'+'⚔'+ weap_list[equip]['damage']+'🛡'+weap_list[equip]['armor']+'💊'+weap_list[equip]['heal_lvl']+'\n'
        if weap_list[equip]['type'] == 'Legs':
            message_Legs+=weap_list[equip]['name']+'('+equip+')|||'+'⚔'+ weap_list[equip]['damage']+'🛡'+weap_list[equip]['armor']+'💊'+weap_list[equip]['heal_lvl']+'\n'
        if weap_list[equip]['type'] == 'Feet':
            message_Feet+=weap_list[equip]['name']+'('+equip+')|||'+'⚔'+ weap_list[equip]['damage']+'🛡'+weap_list[equip]['armor']+'💊'+weap_list[equip]['heal_lvl']+'\n'


    
        
    fin_message='Твой инвентарь + (id):\n'+'голова:\n'+message_hat+'\n\n'+'нагрудники:\n'+message_chest+'\n\n'+'оружие:\n'+message_weap+'\n\n'+'ноги:\n'+message_Legs+'\n\n'+'ботинки:\n'+message_Feet
    return(fin_message)

def item_equip(user_id, item_id):
    shelvefile = shelve.open(path_get())
    equip_inv = shelvefile['equip']
    all_inv = shelvefile['inventories']
    if item_id in all_inv[user_id]:
        
        
        item_type = weap_list[item_id]['type']

        equip_inv[user_id]=equip_inv.get(user_id, {'Head':'','Chest':'','weapon':'','Legs':'','Feet':''}) 

        equip_inv[user_id][weap_list[item_id]['type']]=weap_list[item_id]['name']
        shelvefile['equip'] = equip_inv
        
        message = 'надетый шмот:'+ '\nголова:'+equip_inv[user_id]['Head']+'\nгрудь'+equip_inv[user_id]['Chest']+'\nоружие:'+equip_inv[user_id]['weapon']+'\nноги:'+equip_inv[user_id]['Legs']+'\nботинки:'+equip_inv[user_id]['Legs']
        


        #equip_inv[user_id]={'Head':Head,'Chest':Chest,'weapon':Weapon,'Legs':Legs,'Feet':Feet}
        
    else:
        message='у тебя такого нет'
    return(message)
def equiped_items_show(user_id):
    shelvefile = shelve.open(path_get())
    equip_inv = shelvefile['equip']
    message = 'надетый шмот:'+ '\nголова:'+equip_inv[user_id]['Head']+'\nгрудь'+equip_inv[user_id]['Chest']+'\nоружие:'+equip_inv[user_id]['weapon']+'\nноги:'+equip_inv[user_id]['Legs']+'\nботинки:'+equip_inv[user_id]['Legs']
    return(message)

def inventory_upload(user_id):#выгружаем id всех предметов в базе данных для нас в консоли
    shelvefile = shelve.open(path_get())
    all_inv = shelvefile['inventories']
    print(all_inv)
    #shelvefile.close()
    print(all_inv[user_id])

def money_add(user_id, q_money, money_list):
    
    #money_list.setdefault(user_id, 10)
    #money_list.get(user_id, 0)
    print(money_list)
    #money_list[user_id]=money_list[user_id]+int(q_money)
    money_list[user_id]=money_list.get(user_id, 0) + int(q_money)#если нет данных о человеке - создаёт их
    
    print('money_list[user_id]:'+str(money_list[user_id]))
    print(type(money_list[user_id]))  
    print(money_list)  
    
    return(money_list)

    #print(money_list[user_id])
    #shelvefile.close()

def money_show(user_id):
    shelvefile = shelve.open(path_get())
    money_list = shelvefile['money'][user_id]
    #shelvefile.close()
    print(money_list)
    return(str(money_list)+'🗿')


def case_open(user_id):
    legendary_rare = 90
    common_rare = 0

    fin_num = random.randint(0, 100)

    mass_keys=weap_list.keys()
    keys_rare=[]
    if fin_num>=legendary_rare:
        for keys in mass_keys:
            if weap_list[keys]['rare']=='legendary':
                keys_rare.append(keys)
        

    elif fin_num >=common_rare and fin_num < legendary_rare:
        for keys in mass_keys:
            if weap_list[keys]['rare']=='common':
                keys_rare.append(keys)

    
    random.shuffle(keys_rare)
    prize =keys_rare[0]
    
    inventory_unload(user_id, prize)
    #print('проверяемый список:'+weap_list[prize]['name'], prize)
    ret_list = [weap_list[prize]['name'], prize]
    
    return(ret_list)

def path_get():
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path_pr = os.path.dirname(os.path.abspath(filename))
    return(path_pr)

