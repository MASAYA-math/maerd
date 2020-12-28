import pyxel as px
from engine import engine
import map0


def convert_coordinates():
    pass


class Block:
    def __init__(self, x, y):
        self.x, self.y = x, y


block = Block(16, 0)

map_data = [block]


class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def update(self, map_data):
        forbidden_direction = self.is_col_flagged(map_data)
        print(forbidden_direction)
        if px.btn(px.KEY_D) and not forbidden_direction["D"]:
            self.x += 1
        if px.btn(px.KEY_A) and not forbidden_direction["A"]:
            self.x += -1
        if px.btn(px.KEY_W) and not forbidden_direction["W"]:
            self.y += -1
        if px.btn(px.KEY_S) and not forbidden_direction["S"]:
            self.y += 1

    def draw(self):
        px.blt(self.x, self.y, 0, 0, 48, 16, 16, 0)

    def is_col_flagged(self, map_data) -> dict:
        # TODO Change implement of this function to be able to use map_data instead of before data.
        forbidden_direction = {"A": False, "D": False, "W": False, "S": False}
        for i in range(0, len(map_data)):
            if (abs(self.x - map_data[i].x) <= 16 and
                    abs(self.y - map_data[i].y) <= 16):
                if self.x - map_data[i].x + 16 >= 16 and\
                        abs(self.y - map_data[i].y) != 16:
                    forbidden_direction["A"] = True
                if self.x - map_data[i].x + -16 < -16 and\
                        abs(self.y - map_data[i].y) != 16:
                    forbidden_direction["D"] = True
                if self.y - map_data[i].y + 16 >= 16 and\
                        abs(self.x - map_data[i].x) != 16:
                    forbidden_direction["W"] = True
                if self.y - map_data[i].y + -16 < -16 and\
                        abs(self.x - map_data[i].x) != 16:
                    forbidden_direction["S"] = True
                return forbidden_direction
            else:
                return forbidden_direction


class App:
    def __init__(self):
        px.init(256, 256, caption="MAERD")
        px.load("assets/resource.pyxres")
        self.map = 0
        self.player = Player(112, 128)
        self.map0 = map0.Map()
        px.run(self.update, self.draw)

    def update(self):
        self.player.update(self.map0.map_data)

    def draw(self):
        px.cls(0)
        if self.map == 0:
            px.bltm(0, 0, 0, 0, 0, 32, 32)
            self.player.draw()
            px.blt(self.player.x + 16, self.player.y, 0, 0, 64, 16, 16, 0)
        elif self.map == 1:
            self.player.draw()


App()
