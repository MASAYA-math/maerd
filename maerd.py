import pyxel as px
from engine import engine
import map0
import map1
import animations
import player


class App:
    def __init__(self):
        px.init(256, 256, caption="MAERD")
        px.load("assets/resource.pyxres")
        self.player = player.Player(112, 128)
        self.maps = [map0.Map0(self), map1.Map1(self)]
        self.map_player_in_number = 0
        self.map_player_in = self.maps[self.map_player_in_number]
        self.animations = [animations.Animation1()]
        px.run(self.update, self.draw)

    def update(self):
        self.map_player_in.update()
        self.player.update(self.map_player_in.on_collision_list)
        for elm in self.animations:
            elm.update()

    def draw(self):
        px.cls(0)
        self.map_player_in.draw()
        self.player.draw()
        for elm in self.animations:
            elm.draw()
        px.blt(self.player.x + 16, self.player.y, 0, 0, 64, 16, 16, 0)


App()
