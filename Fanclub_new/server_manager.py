from server import Server
# Получаем из config.py наш api-token
from config import vk_api_token


server1 = Server(vk_api_token, 186777464, "server1")
# vk_api_token - API токен, который мы ранее создали
# 172998024 - id сообщества-бота
# "server1" - имя сервера

#server1.test()
server1.start()