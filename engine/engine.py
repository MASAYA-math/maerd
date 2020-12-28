class Block:
    pass


class EmptyBlock(Block):
    pass


class CollisionBlock(Block):
    pass


class EventBlock(CollisionBlock):
    pass


def make_map_instance(source, events):
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
