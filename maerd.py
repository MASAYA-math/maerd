import pyxel as px


class Block:
    def __init__(self, x, y):
        self.x, self.y = x, y


block = Block(24, 0)

col_blocks = [block]


class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def update(self):
        forbidden_direction = is_col_flagged(self)
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


def is_col_flagged(player: Player) -> dict:
    forbidden_direction = {"A": False, "D": False, "W": False, "S": False}
    for i in range(0, len(col_blocks)):
        if (abs(player.x - col_blocks[i].x) <= 16 and
                abs(player.y - col_blocks[i].y) <= 16):
            if player.x - col_blocks[i].x + 16 >= 16 and\
                    abs(player.y - col_blocks[i].y) != 16:
                forbidden_direction["A"] = True
            if player.x - col_blocks[i].x + -16 < -16 and\
                    abs(player.y - col_blocks[i].y) != 16:
                forbidden_direction["D"] = True
            if player.y - col_blocks[i].y + 16 >= 16 and\
                    abs(player.x - col_blocks[i].x) != 16:
                forbidden_direction["W"] = True
            if player.y - col_blocks[i].y + -16 < -16 and\
                    abs(player.x - col_blocks[i].x) != 16:
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
        px.run(self.update, self.draw)

    def update(self):
        self.player.update()

    def draw(self):
        px.cls(0)
        if self.map == 0:
            px.bltm(0, 0, 0, 0, 0, 32, 32)
            self.player.draw()
            px.blt(self.player.x + 16, self.player.y, 0, 0, 64, 16, 16, 0)
        elif self.map == 1:
            self.player.draw()


App()
