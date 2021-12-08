
from pico2d import *
import json
import game_framework
import theWorld
import title_state

from mario import Mario
from wall import Wall
from gumba import Gumba
from coin import Coin
from back1 import Back1
from brick import Brick
from turtleman import Turtleman
from backg import Map1 as Background
name = "MainState"

import server

def collide(a, b):
    left_a, bottom_a, right_a, top_a= a.get_bb()
    left_b, bottom_b, right_b, top_b=b.get_bb()
    if left_a>right_b:return False
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False

    return True



def enter():
    server.mario1 = Mario()
    theWorld.add_object(server.mario1,1)

    server.wall = Wall()
    theWorld.add_object(server.wall, 0)


    #gumbas=Gumba()
    gumbas = [Gumba() for i in range(5)]
    theWorld.add_objects(gumbas, 1)


    server.background=Background()
    theWorld.add_object(server.background,0)

    """with open('coin_data.json.py') as f:
        coin_data_list=json.load(f)
    for data in coin_data_list:
        server.coins=Coin(data['no'],data['x'],data['y'])
        theWorld.add_object(server.coins,1)"""



    """global Ungm
    Ungm=[Turtleman() for i in range(3)]
    theWorld.add_objects(Ungm,1)"""

def exit():
    theWorld.clear()

def pause():
    pass


def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
        else:
            server.mario1.handle_event(event)

def update():
    for game_object in theWorld.all_objects():
        game_object.update()
    for coin in server.coins:
        if collide(server.mario1,coin):
            server.coins.remove(coin)
            theWorld.remove_object(coin)


    if collide(server.wall,server.mario1):
        server.mario1.stop()




def draw():
    clear_canvas()
    for game_object in theWorld.all_objects():
        game_object.draw()
    update_canvas()
