import pyxel as px


class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def player_update(self):
        if px.btn(px.KEY_D):
            player.x += 1
        if px.btn(px.KEY_A):
            player.x += -1
        if px.btn(px.KEY_W):
            player.y += -1
        if px.btn(px.KEY_S):
            player.y += 1


player = Player(112, 128)


class App:
    def __init__(self):
        px.init(256, 256, caption="MAERD")
        px.load("resource.pyxres")
        px.run(self.update, self.draw)

    def update(self):
        player.player_update()

    def draw(self):
        px.cls(0)
        px.bltm(0, 0, 0, 0, 0, 32, 32)
        px.blt(player.x, player.y, 0, 0, 48, 16, 16, 0)
        px.blt(player.x + 16, player.y, 0, 0, 64, 16, 16, 0)


App()
