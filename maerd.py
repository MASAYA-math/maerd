import pyxel as px


class App:
    def __init__(self):
        px.init(256, 256)
        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pass


App()
