import pyxel as px
from engine import engine


class Animation1(engine.Animation):
    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
        if self.is_playing:
            self.tick_count += 1
        if self.tick_count >= 60:
            self.is_playing = False

    def draw(self):
        super().draw()
        if self.is_playing:
            px.cls(0)
            px.text(118, 128, "MAERD", self.tick_count % 16)
