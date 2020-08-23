import re
import requests
from bs4 import BeautifulSoup

def first_check():
    mass=[]
    url ='https://www.google.com/search?q=%D1%81%D1%82%D0%BE%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD&rlz=1C1SQJL_ruRU909RU909&oq=%D1%81%D1%82%D0%BE%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD&aqs=chrome..69i57j0l6j69i61.671j0j9&sourceid=chrome&ie=UTF-8' 
    #url ='https://vk.com/pospat_4isto'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    page = requests.get(url, headers = headers)
    #print(page.text)
    #print(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')

    convert = soup.findAll('span', {'class':'DFlfde', 'class':'SwHCTb'})
    #print(convert[0].text)
    bit_cost = str(convert[0].text).split()

    Nbit_cost = ''
    for i in bit_cost:
        mass.append(i)


    for i in mass:
        if i == ' ':
            continue
        if i ==',':
            i='.'
        Nbit_cost+=i
    return(Nbit_cost)
    