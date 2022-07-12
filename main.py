# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.longpoll import VkLongPoll, VkEventType
#vk_session = vk_api.VkApi('+79955932780', 'SI5BGmOhGf94')

# try:
#     vk_session.auth(token_only=True)
# except vk_api.AuthError as error_msg:
#     print(error_msg)
#
# current_vk_api = vk_session.get_api()

""" VkApi.method позволяет выполнять запросы к API. В этом примере
    используется метод wall.get (https://vk.com/dev/wall.get) с параметром
    count = 1, т.е. мы получаем один последний пост со стены текущего
    пользователя.
"""
# response = current_vk_api.wall.get(count=1)  # Используем метод wall.get
# if response['items']:
#     print(response['items'][0])
#
# current_vk_api.

token = r"c81e432f4ac6c2cb2ebfbb5abc651eb136cac03bacbea955241c64e6494f01c3c94c20f59daceca3a9b18"
# session = vk_api.VkApi(token=token)
# session.auth(token_only=True)
session = vk_api.VkApi('+79955932780', 'SI5BGmOhGf94')
session.auth()
vk = session.get_api()
# print(session.method("account.getInfo"))
# print(session.method("account.getProfileInfo"))
# print(session.method("account.getCounters"))
# print(session.method("friends.getSuggestions", {
#     "count": 1000
# }))
#birth_day = '22', birth_month = '1'
new_users = vk.users.search(q = '', count=1000, city = '2', sex=1, hometown='Красноярск', fields='bdate, city, home_town')
# print(new_users)
# longpoll = VkLongPoll(session)
index = 1
all_index = 1
for user in new_users['items']:
    try:
        # print(all_index)
        city = user['city']
        user_id = user['id']
        first_name = user['first_name']
        last_name = user['last_name']
        home_town = user['home_town']

        # print(city)
        # print(user_id)

        if city['title'] == 'Санкт-Петербург':# and home_town == 'Красноярск':
            # print(user)
            user_info = vk.users.get(user_id=user_id, fields='relation, universities, music, has_mobile, contacts, status, common_count, last_seen, maiden_name, online, lists, nickname, is_closed, deactivated, counters, friend_status, is_favorite, is_friend, photo_400_orig')
            relation = user_info[0]['relation']
            last_seen = user_info[0]['last_seen']
            university = user_info[0]['universities']
            university_names = ''
            for u in university:
                university_names += u['name'] + " "
            bdate = user['bdate']
            birth_year = datetime.datetime.strptime(bdate,'%d.%m.%Y')
            years_old = 2022 - birth_year.year
            date_time_last_seen =  datetime.datetime.fromtimestamp(last_seen['time'])
            time_difference = datetime.datetime.now() - date_time_last_seen
            time_difference_days = time_difference.days
            # print(time_difference.days)
            if (relation == 0 or relation == 1 or relation == 6) and (time_difference_days <= 7) and (years_old >= 18 and years_old <= 45) : # and( str(university_names).find('СибГАУ') != -1)
                url = {'url': r'https://vk.com/id'+str(user_id)}
                # print(index, first_name, last_name, relation, years_old, time_difference_days, url)
                # print(user_info)
                try:
                    print(index, first_name, last_name, relation, years_old, time_difference_days, url, university_names)
                    print(user_info)
                    # groups = session.method("users.getSubscriptions", {
                    #     "user_id": user_id
                    #
                    # })['groups']
                    #
                    # for group_id in groups['items']:
                    #     group_info = session.method("groups.getById", {
                    #         "group_id": group_id
                    #     })
                    #     name = group_info[0]['name']
                    #     if str(name).lower().find('ддт') != -1:
                    #         print(group_info)

                except :
                    pass
                index += 1
        all_index += 1
    except:
        pass

def send_message(user_id, message):
    session.method("messages.send", {
        "user_id": user_id,
        "message": message,
        "random_id": 0
    })

# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#         text = event.text.lower()
#         user_id = event.user_id
#
#         if text == 'start':
#             send_message(user_id, "Hello!")

