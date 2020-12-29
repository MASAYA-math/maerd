

class Block:
    pass


class EmptyBlock(Block):
    pass


class CollisionBlock(Block):
    pass


class EventBlock(Block):
    def update_event_handler(self, app):
        pass

    def draw_event_handler(self):
        pass


class Map:
    def __init__(self, app, map_data_source, events):
        self.app = app
        self.map_data = self.make_map_instance(map_data_source, events)

    def update(self):
        self.on_collision_list = self.is_on_collision(
            self.app.player, self.map_data)
        for elm in self.on_collision_list:
            if isinstance(elm[2], EventBlock):
                elm[2].update_event_handler(self.app)

    def draw(self):
        for elm in self.on_collision_list:
            if isinstance(elm[2], EventBlock):
                elm[2].draw_event_handler()

    def make_map_instance(self, source, events):
        map_data_instance = []
        for i in range(0, len(source)):
            map_data_instance.append([])
            for j in range(0, len(source[i])):
                if source[i][j] == 0:
                    map_data_instance[i].append(EmptyBlock())
                elif source[i][j] == 1:
                    map_data_instance[i].append(CollisionBlock())
                else:
                    map_data_instance[i].append(events[source[i][j] - 2]())
        return map_data_instance

    def is_on_collision(self, player, map_data) -> list:
        on_collision_list = []
        for i in range(0, len(map_data)):
            for j in range(0, len(map_data[i])):
                if abs(player.x - j*16) <= 16 and\
                        abs(player.y - i*16) <= 16:
                    on_collision_list.append((i, j, map_data[i][j], True))
        return on_collision_list


class Animation:
    def update(self):
        pass

    def draw(self):
        pass
