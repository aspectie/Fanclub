import shelve
import inspect, os.path
import random

filename = inspect.getframeinfo(inspect.currentframe()).filename
path_pr     = os.path.dirname(os.path.abspath(filename))

shelveFile = shelve.open(path_pr + '\\differentValues')
shelveFile['value']=random.randint(200, 90000)