import pyxel as px
from engine import engine


class CustomEventBlock(engine.EventBlock):
    pass


class EventBlock0(CustomEventBlock, engine.CollisionBlock):
    def update_event_handler(self, app):
        super().update_event_handler(app)
        if px.btn(px.KEY_ENTER):
            app.map_player_in_number = 1
            app.map_player_in = app.maps[app.map_player_in_number]
            app.map_player_in.update(app.player)


events = [EventBlock0]
