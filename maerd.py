import pyxel as px


class App:
    def __init__(self):
        px.init(256, 256, caption="MAERD")
        px.load("resource.pyxres")
        self.x = 112
        self.y = 128
        px.run(self.update, self.draw)

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
        px.cls(0)
        px.bltm(0, 0, 0, 0, 0, 32, 32)
        px.blt(self.x, self.y, 0, 0, 48, 16, 16, 0)
        px.blt(self.x + 16, self.y, 0, 0, 64, 16, 16, 0)


App()
