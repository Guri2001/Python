#!/usr/bin/env python
# coding: utf-8

# # Introduction
"""
Opening your comic book store, the Sorcery Society, has been a lifelong dream come true. 
You quickly diversified your shop offerings to include miniatures, plush toys, collectible card games, 
and board games. Eventually, the store became more a games store with a selection of this week's newest comic books and a small offering of graphic novel paperbacks.
Completing your transformation means offering space for local tabletop gamers. 
They love to play their favorite RPG, "Abruptly Goblins!" and will happily pay you per chair to secure the space to do it. Unfortunately, 
planning the game night has fallen to you. 
If you pick the wrong night, not enough people will come and the game night will be cancelled. 
You decide it's best that you automate the game night selector to get the most people through the door. 
First you need to create a list of people who will be attending the game night.
"""


gamers = []

def add_gamer(gamer, gamers_list):
    if(("name" in gamer.keys())and ("availability" in gamer.keys())):
        gamers_list.append(gamer)


kimberly = {"name": "Kimberly", "availability":["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly,gamers)




add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


def build_daily_frequency_table():
    return {"Monday":0, 
            "Tuesday":0,
            "Wednesday":0,
            "Thursday":0,
            "Friday":0,
            "Saturday":0,
            "Sunday": 0
           }
count_availability = build_daily_frequency_table()


def calculate_availability(gamers_list,available_frequency):
    for each_val in gamers_list:
        for day in each_val["availability"]:
            if(day in available_frequency):
                available_frequency[day] +=1
    return available_frequency
#         for i in range(len(day.get("availability"))):
#             if(day["availability"][i] in available_frequency):
#                 available_frequency[day["availability"][i]] += 1
    return available_frequency


calculate_availability(gamers,count_availability)
print(count_availability)

def find_best_night(availability_table):
    highest_value = 0
    for value in availability_table:
        if(availability_table[value] > highest_value):
            highest_value = availability_table[value]
            day = value
    return day


game_night = find_best_night(count_availability)
print(game_night)


def available_on_night(gamers_list, day):
    available_people = [each_person["name"] for each_person in gamers_list if day in each_person["availability"]]

    return available_people

attending_game_night = available_on_night(gamers,game_night)
print(attending_game_night)


form_email = """
Dear {name},

The {game} can be played on the {day_of_week} come to have a blast!

Abruptly Goblins!

"""


def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name = gamer, day_of_week = day, game = game))
send_email(attending_game_night, game_night, "Abruptly Goblins")


unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer["availability"]]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)
print(second_night)


available_second_game_night = available_on_night(gamers,second_night)
send_email(available_second_game_night,second_night,"Abruptly Goblines")
