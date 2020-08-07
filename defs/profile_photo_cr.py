from PIL import Image, ImageDraw, ImageFont
import requests
import sys

import shelve
import random
import os
import inspect, os.path




def profile_create(userName):
    

    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path_pr     = os.path.dirname(os.path.abspath(filename))
    


    shelveFile = shelve.open(path_pr + '\\differentValues')
    
    print

    
    shelveFile['value']+=1

    x = shelveFile['value']

    string = 'https://www.thiswaifudoesnotexist.net/example-'+str(x)+'.jpg'
    #print(string)




    url = string
    

    resp = requests.get(url, stream=True).raw



    img = Image.open(resp)

    t_d = ImageDraw.Draw(img)


    fonts_mass = []
    for foldername, subfoldernames, filenames in os.walk(path_pr + '\\differentValues\\fonts'):
    
        for filename in filenames:
            fonts_mass.append(filename)
            
        

    random.shuffle(fonts_mass)
    #print(fonts_mass)
    print('нынешний os.getcwd():'+os.getcwd())
    font = path_pr + '\\differentValues\\fonts\\' + fonts_mass[0]
    print(font)
    text = userName
    #print('\n'+font)

    font = ImageFont.truetype(font,  size=100)
    t_d.text((200, 880), text, font=font, fill=(15,150,56,220))
    save_line = path_pr + '\\differentValues\\profPictures\\' +str(x)+ '.jpg'
    img.save(save_line)

    return(save_line)