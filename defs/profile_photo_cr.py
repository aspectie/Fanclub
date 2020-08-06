from PIL import Image, ImageDraw, ImageFont
import requests
import sys

import shelve
import random
import os




def profile_create(userName):
    shelveFile = shelve.open(os.getcwd() + '\\Desktop\\Fanclub\\defs\\differentValues')
    shelveFile['value']+=1
    x = shelveFile['value']

    string = 'https://www.thiswaifudoesnotexist.net/example-'+str(x)+'.jpg'
    #print(string)




    url = string
    

    resp = requests.get(url, stream=True).raw



    img = Image.open(resp)

    t_d = ImageDraw.Draw(img)


    fonts_mass = []
    for foldername, subfoldernames, filenames in os.walk(os.getcwd() + '\\Desktop\\Fanclub\\defs\\differentValues\\fonts'):
    
        for filename in filenames:
            fonts_mass.append(filename)
            
        

    random.shuffle(fonts_mass)
    #print(fonts_mass)

    font = os.getcwd() + '\\Desktop\\Fanclub\\defs\\differentValues\\fonts\\' + fonts_mass[0]
    
    text = userName
    #print('\n'+font)

    font = ImageFont.truetype(font,  size=100)
    t_d.text((200, 880), text, font=font, fill=(15,150,56,220))
    save_line = os.getcwd() + '\\Desktop\\Fanclub\\defs\\differentValues\\profPictures\\' +str(x)+ '.jpg'
    img.save(save_line)

    return(save_line)