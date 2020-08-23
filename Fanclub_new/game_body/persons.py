import inspect, os.path

import shelve
import inspect, os.path

class person_create:

    def __init__(self, user_id, vk_api, class_player, peer_id):
        global path_pr
        #сохранение участника
        filename = inspect.getframeinfo(inspect.currentframe()).filename
        path_pr = os.path.dirname(os.path.abspath(filename))

        shelvefile = shelve.open(path_pr)

        

        plater_list = shelvefile['player_list']
        class_player= class_player.split()[1]
        self.data_save(shelvefile, user_id, class_player)
        if user_id in plater_list:
            message='[id{}|{}]'.format(user_id, user_id) + ' сменил роль на '+class_player
            vk_api.messages.send(peer_id=peer_id, message=message , random_id =0)
        else:
            plater_list.append(user_id)
            shelvefile['player_list']=plater_list
            shelvefile.close()
            self.data_save(shelvefile, user_id, class_player)
            #self.class_createclass_player)
    
    def attack(self):
        pass #сделать атаку, оборону и другие функции
    '''
    def class_create(self, class_player):
        if class_player.lower()== 'дд':
            self.hp =30
            self.damage = 100
        if class_player.lower() =='танк':
            self.hp=120
            self.damage=2
        if class_player.lower()=='хилер':
            self.hp =35
            self.damage=4
            self.healing=50
    '''

    def data_save(self, shelvefile, user_id, class_player):
        
        save_list = {'class_player':class_player}
        print(save_list)
        shelvefile[str(user_id)] = save_list
    
    def data_show(self, user_id):
        shelvefile = shelve.open(path_pr)
        save_list=shelvefile[str(user_id)]
        print(save_list)

       


        
    
    def show_player_list(self):
        shelvefile = shelve.open(path_pr)
        plater_list = shelvefile['player_list']
        print(plater_list)
        shelvefile.close()

    def player_check(self, user_id):
        shelvefile = shelve.open(path_pr)
        plater_list = shelvefile['player_list']
        if user_id in plater_list:
            message='не пустить'
        else:
            message='пустить'
        return(message)
    
class Boss:

    def __init__(self):
        self.name = 'boss'#1.придумать стилистику
        self.hp = 10#2.+- от количества игроков (plater_list = shelvefile['player_list'])4
        self.damage = 10#3.+- ...

    def attack(self):
        pass #сделать атаку, оборону и другие функции
    

