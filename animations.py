import pyxel as px
from engine import engine


class Animation0(engine.Animation):
    def __init__(self):
        super().__init__()
        self.is_playing = True

    def update(self):
        super().update()
        if self.is_playing:
            self.tick_count += 1
        if self.tick_count >= 60:
            self.is_playing = False
            self.tick_count = 0

    def draw(self):
        super().draw()
        if self.is_playing:
            px.cls(0)
            if self.tick_count < 12:
                px.text(0, 0, "M", 8)
            elif self.tick_count < 24:
                px.text(0, 0, "MA", 8)
            elif self.tick_count < 36:
                px.text(0, 0, "MAE", 8)
            elif self.tick_count < 48:
                px.text(0, 0, "MAER", 8)
            else:
                px.text(0, 0, "MAERD", 8)


class Animation1(engine.Animation):
    def __init__(self):
        super().__init__()
        self.is_playing = False

    def update(self):
        super().update()
        if self.is_playing:
            self.tick_count += 1
        if self.tick_count >= 30:
            self.is_playing = False
            self.tick_count = 0

    def draw(self):
        super().draw()
        if self.is_playing:
            px.cls(0)
            px.text(118, 128, "MAERD", self.tick_count % 16)
