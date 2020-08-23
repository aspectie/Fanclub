import shelve
import inspect, os.path
from equip_list import *
filename = inspect.getframeinfo(inspect.currentframe()).filename
path_pr = os.path.dirname(os.path.abspath(filename))

shelvefile = shelve.open(path_pr)
#shelvefile['equip']={}
equip_inv = shelvefile['equip']
all_inv = shelvefile['inventories']
   
item_id='1'
Head=''
Chest=''
Weapon=''
Legs=''
Feet=''
item_type = weap_list[item_id]['type']

equip_inv[1]=equip_inv.get(1, {'Head':'','Chest':'','weapon':'','Legs':'','Feet':''}) 

equip_inv[1][weap_list[item_id]['type']]=weap_list[item_id]['name']
shelvefile['equip'] = equip_inv
print(equip_inv[1])
message = 'Head:'+equip_inv[1][+ '', 'Chest': '', 'weapon': 'вилка', 'Legs': '', 'Feet': ''

