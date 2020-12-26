import pyxel as px


class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def update(self):
        if px.btn(px.KEY_D):
            self.x += 1
        if px.btn(px.KEY_A):
            self.x += -1
        if px.btn(px.KEY_W):
            self.y += -1
        if px.btn(px.KEY_S):
            self.y += 1

    def draw(self):
        px.blt(self.x, self.y, 0, 0, 48, 16, 16, 0)


class App:
    def __init__(self):
        px.init(256, 256, caption="MAERD")
        px.load("assets/resource.pyxres")
        self.map = 0
        self.player = Player(112, 128)
        px.run(self.update, self.draw)

    def update(self):
        self.player.update()
        if self.player.y < 16:
            self.map = 1
            self.player.x = 112
            self.player.y = 128

    def draw(self):
        px.cls(0)
        if self.map == 0:
            px.bltm(0, 0, 0, 0, 0, 32, 32)
            self.player.draw()
            px.blt(self.player.x + 16, self.player.y, 0, 0, 64, 16, 16, 0)
        elif self.map == 1:
            self.player.draw()


App()
