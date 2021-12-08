import server

from pico2d import *


class Map1:
    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = 800 * 3
        self.h = 600 * 3

        self.tiles = [[load_image('badak%d%d.png' % (x, y)) for x in range(4)] for y in range (2)]

    def draw(self):

        self.window_left = clamp(0,int(server.mario1.x) - self.canvas_width // 2,self.w - self.canvas_width)
        self.window_bottom = clamp(0,int(server.mario1.y) - self.canvas_height // 2,self.h - self.canvas_height)

        tile_left = self.window_left // 800
        tile_right = min((self.window_left + self.canvas_width) // 800 + 1, 4)
        left_offset = self.window_left % 800

        tile_bottom = self.window_bottom // 600
        tile_top = min((self.window_bottom + self.canvas_height) // 600 + 1, 2)
        bottom_offset = self.window_bottom % 600

        for ty in range(tile_bottom, tile_top):
            for tx in range(tile_left, tile_right):
                self.tiles[ty][tx].draw_to_origin(-left_offset + (tx - tile_left) * 800,-bottom_offset + (ty - tile_bottom) * 600)
        pass

    def update(self):
        pass

    def handle_event(self):
        pass
