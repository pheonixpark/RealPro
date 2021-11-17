
from pico2d import *
import game_framework
import theWorld
import title_state

from mario import Mario
from wall import Wall
from gumba import Gumba
from coin import Coin
from back1 import Back1
from turtleman import Turtleman
name = "MainState"

mario1=None
wall=None
Ungm=[]

gumbas=[]
coins=[]
def collide(a, b):
    left_a, bottom_a, right_a, top_a= a.get_bb()
    left_b, bottom_b, right_b, top_b=b.get_bb()
    if left_a>right_b:return False
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False

    return True

def gameover(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False
    if left_a>right_b:return False
    if right_a<left_b:return False

    return True


def enter():
    global mario1
    mario1 = Mario()
    theWorld.add_object(mario1,1)


    global back1
    back1=Back1()
    theWorld.add_object(back1,0)

    global wall
    wall = Wall()
    theWorld.add_object(wall, 0)
    global gumbas
    #gumbas=Gumba()
    gumbas = [Gumba() for i in range(5)]
    theWorld.add_objects(gumbas,1)

    global coins
    coins=[Coin() for i in range(10)]
    theWorld.add_objects(coins,1)

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
            mario1.handle_event(event)

def update():
    for game_object in theWorld.all_objects():
        game_object.update()
    for coin in coins:
        if collide(mario1,coin):
            coins.remove(coin)
            theWorld.remove_object(coin)
    if collide(wall,mario1):
        mario1.stop()
    for gumba in gumbas:
        if gameover(gumba,mario1):
            theWorld.remove_object(mario1)





def draw():
    clear_canvas()
    for game_object in theWorld.all_objects():
        game_object.draw()
    update_canvas()
