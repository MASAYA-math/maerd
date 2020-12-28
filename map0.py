from engine import main


map_data_source = [
    [0, 1, 0]
]

map_data_instance = main.make_map_instance(map_data_source)


print(map_data_instance)


class Map:
    def __init__(self):
        self.map_data = map_data_instance
