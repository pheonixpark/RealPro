from pico2d import *

class Back1:
    def __init__(self):
        self.image = load_image('back1.png')

    def update(self):
        pass

    def get_bb(self):
        return 0,0,0,0

    def draw(self):
        self.image.draw(800,450)
        draw_rectangle(*self.get_bb())