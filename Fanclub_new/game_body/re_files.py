import shelve
import inspect, os.path
filename = inspect.getframeinfo(inspect.currentframe()).filename
path_pr = os.path.dirname(os.path.abspath(filename))
#print(path_pr)
shelvefile = shelve.open(path_pr)
shelvefile['player_list']=[]

shelvefile['money']={}
shelvefile['equip']={}
shelvefile['inventories']={}

#shelvefile[user_id] = {}