
from pico2d import *
import game_framework
import theWorld

from Mario import mario
from wall import Wall

name = "MainState"

mario=None
wall=None

def collide(a, b):
    left_a, bottom_a, right_a, top_a= a.get_bb()
    left_b, bottom_b, right_b, top_b=b.get_bb()
    if left_a>right_b:return False
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False

    return True

def enter():
    global Mario
    Mario = Mario()
    theWorld.add_object(Mario,1)

    global wall
    wall=Wall()
    theWorld.add_object(wall,0)

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
                game_framework.quit()
        else:
            Mario.handle_event(event)

def update():
    for game_object in theWorld.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in theWorld.all_objects():
        game_object.draw()
    update_canvas()
