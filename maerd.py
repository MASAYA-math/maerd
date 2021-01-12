from engine import engine
import map0
import map1
import animations
import player

TITLE = "MAERD"
RESOURCE_FILE = "../assets/resource.pyxres"
PLAYER = player.Player(112, 128)
MAPS = [map0.Map0, map1.Map1]
ANIMATIONS = [animations.Animation0(), animations.Animation1()]


engine.App(TITLE, RESOURCE_FILE, PLAYER, MAPS, ANIMATIONS)
