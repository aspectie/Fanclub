import inspect, os.path
import pprint
import shelve

class person:
    
    def __init__(self, name, id_person):
        
        self.path = self.get_path()
        self.id_person=id_person

        
        if self.reg_check(name,  self.id_person, self.path)==False:
            self.name=name
            self.hp=10
            self.save_data(self.path)
        else:
            self.data_get(self.path)


        
       
    def reg_check(self, name, id_person, path):
        #self.id_person=id_person #уникальный вк id пользователя 
        
        shelveFile = shelve.open(path)#открываем базу данных
        list_member=shelveFile['list']#загружаем список со всеми id пользователей, которые уже зарегестрировались
        return(self.id_person in list_member)
    
    def data_get(self, path):
        shelveFile = shelve.open(path)
        self.name = shelveFile[str(self.id_person)+' name']
        self.hp = shelveFile[str(self.id_person)+' hp']

    

    def save_data(self,path):
        
       
        shelveFile = shelve.open(path)
        shelveFile[str(self.id_person)+' name'] = self.name
        shelveFile[str(self.id_person)+' hp'] = self.hp
        shelveFile.close()

    
    def show(self):
        print(self.name)

    def get_path(self):
        
        filename = inspect.getframeinfo(inspect.currentframe()).filename
        path_equip = os.path.dirname(os.path.abspath(filename))
        
        path=path_equip +'\safe_folder'
        return(path)


class Boss:
    def __init__(self, hp, attack_power):
        self.hp = hp
        self.attack_power = attack_power



            
    


danya = person('daniil', id_person=12349501811111 )
danya.show()

glep = person('gleb', id_person=22213213213213)
glep.show()

vika= person('vikka', id_person=2221321332713213)
vika.show()
 
dab=person('dab', id_person=222132132173213)
dab.show()