from pico2d import *

class Wall:
    def __init__(self):
        self.image = load_image('wall.png')

    def update(self):
        pass

    def get_bb(self):
        return 0,0,1600-1,50

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        draw_rectangle(*self.get_bb())



