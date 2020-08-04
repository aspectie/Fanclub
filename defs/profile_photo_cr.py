from PIL import Image, ImageDraw, ImageFont
import requests
import sys
import sys
import shelve
import random
import os
mass = []
shelveFile = shelve.open(r'C:\Users\danii\Desktop\Vk_Bot\VKbot_env\defs\differentValues')
shelveFile['value']+=1
x = shelveFile['value']

string = 'https://www.thiswaifudoesnotexist.net/example-'+str(x)+'.jpg'
print(string)




url = string
 

resp = requests.get(url, stream=True).raw



img = Image.open(resp)

t_d = ImageDraw.Draw(img)



for foldername, subfoldernames, filenames in os.walk(r'C:\Users\danii\Desktop\Vk_Bot\VKbot_env\defs\differentValues\fonts'):
 
    for filename in filenames:
        mass.append(filename)
        
    

random.shuffle(mass)
print(mass)

font = 'C:/Users/danii/Desktop/Vk_Bot/VKbot_env/defs/differentValues/fonts/' + mass[0]
#C:\Users\danii\Desktop\Vk_Bot\VKbot_env\defs\differentValues\fonts
#font = ImageFont.truetype("arial.ttf", size=80)
text = 'future_Username'


font = ImageFont.truetype(font,  size=100)

 
t_d.text((200, 880), text, font=font, fill=(15,150,56,220))

img.show()
img.save('C:/Users/danii/Desktop/Vk_Bot/VKbot_env/defs/differentValues/Profile'+str(x)+'.jpg')
