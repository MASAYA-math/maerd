import pyxel as px
from engine import engine
import map0
import map1


class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.map_number = 0

    def update(self, collision_list):
        self.collision_list = collision_list
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
        px.blt(112, 128, 0, 0, 48, 16, 16, 0)

    def handle_collision(self, collision_list) -> dict:
        forbidden_direction = {"A": False, "D": False, "W": False, "S": False}
        for elm in collision_list:
            if isinstance(elm[2], engine.CollisionBlock):
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
        self.maps = [map0.Map0(self), map1.Map1(self)]
        self.map_player_in_number = 0
        self.map_player_in = self.maps[self.map_player_in_number]
        px.run(self.update, self.draw)

    def update(self):
        self.map_player_in.update()
        self.player.update(self.map_player_in.on_collision_list)

    def draw(self):
        px.cls(0)
        self.map_player_in.draw()
        self.player.draw()
        px.blt(self.player.x + 16, self.player.y, 0, 0, 64, 16, 16, 0)


App()
