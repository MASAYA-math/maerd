import pyxel as px
from engine import engine


class CustomEventBlock(engine.EventBlock):
    def update_event_handler(self, player):
        super().update_event_handler()

    def draw_event_handler(self, player):
        super().draw_event_handler()


class EventBlock0(CustomEventBlock, engine.CollisionBlock):
    def update_event_handler(self, player):
        super().update_event_handler(player)
        if px.btn(px.KEY_ENTER):
            player.map_number = 1


events = [EventBlock0]
