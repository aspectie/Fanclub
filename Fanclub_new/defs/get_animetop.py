import requests
#from bs4 import BeautifulSoup
import re

def anime_top():
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'})

    url = "https://animego.org/anime?sort=r.rating&direction=desc"
    html_c = requests.get(url, headers)

    #забираем названия
    search_name_method = re.compile(r'<div class="h5 font-weight-normal mb-1"><a href="https.+">(.+)</a></div>')
    anime_names = search_name_method.findall(html_c.text)
   

    #забираем рейтинг
    search_star_method = re.compile(r'class="p-rate-flag__text">(\d,\d)')
    anime_stars = search_star_method.findall(html_c.text)
    

    search_year_method = re.compile(r'>(\d\d\d\d)</a>')
    anime_year = search_year_method.findall(html_c.text)
    print(anime_year)

    message='Аниме топ по мнению AnimeGO\n'
    for i in range(10):
        
        message+=str(i+1)+'.'+anime_names[i]+' '+str(anime_stars[i])+'⭐\n'+'год:'+anime_year[i]+'\n'

    return(message)