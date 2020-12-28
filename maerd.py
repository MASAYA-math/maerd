import pyxel as px
from engine import engine
import map0


def convert_coordinates():
    pass


def is_on_collision(player, map_data) -> list:
    on_collision_list = []
    for i in range(0, len(map_data)):
        for j in range(0, len(map_data[i])):
            if isinstance(map_data[i][j], engine.CollisionBlock) and\
                    abs(player.x - j*16) <= 16 and abs(player.y - i*16) <= 16:
                on_collision_list.append((i, j, map_data[i][j], True))
    return on_collision_list


class Map:
    pass


class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.map_number = 0

    def update(self, map_data):
        self.collision_list = is_on_collision(self, map_data)
        for elm in self.collision_list:
            if isinstance(elm[2], engine.EventBlock):
                elm[2].update_event_handler(self)
        forbidden_direction = self.handle_collision(self.collision_list)
        if px.btn(px.KEY_D) and not forbidden_direction["D"]:
            self.x += 1
        if px.btn(px.KEY_A) and not forbidden_direction["A"]:
            self.x += -1
        if px.btn(px.KEY_W) and not forbidden_direction["W"]:
            self.y += -1
        if px.btn(px.KEY_S) and not forbidden_direction["S"]:
            self.y += 1

    def draw(self):
        for elm in self.collision_list:
            if isinstance(elm[2], engine.EventBlock):
                elm[2].draw_event_handler(self)
        px.blt(self.x, self.y, 0, 0, 48, 16, 16, 0)

    def handle_collision(self, collision_list) -> dict:
        forbidden_direction = {"A": False, "D": False, "W": False, "S": False}
        for elm in collision_list:
            if self.x - elm[1]*16 + 16 >= 16 and\
                    abs(self.y - elm[0]*16) != 16:
                forbidden_direction["A"] = True
            if self.x - elm[1]*16 + -16 < -16 and\
                    abs(self.y - elm[0]*16) != 16:
                forbidden_direction["D"] = True
            if self.y - elm[0]*16 + 16 >= 16 and\
                    abs(self.x - elm[1]*16) != 16:
                forbidden_direction["W"] = True
            if self.y - elm[0]*16 + -16 < -16 and\
                    abs(self.x - elm[1]*16) != 16:
                forbidden_direction["S"] = True
        return forbidden_direction


class App:
    def __init__(self):
        px.init(256, 256, caption="MAERD")
        px.load("assets/resource.pyxres")
        self.player = Player(112, 128)
        self.map0 = map0.Map()
        px.run(self.update, self.draw)

    def update(self):
        self.player.update(self.map0.map_data)

    def draw(self):
        px.cls(0)
        if self.player.map_number == 0:
            px.bltm(0, 0, 0, 0, 0, 32, 32)
            self.player.draw()
            px.blt(self.player.x + 16, self.player.y, 0, 0, 64, 16, 16, 0)
        else:
            px.text(64, 64, "NEXT STAGE", 8)


App()
