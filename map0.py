from engine import main

map_data_source = [
    [0, 1, 0]
]

map_data_instance = []
for i in range(0, len(map_data_source)):
    map_data_instance.append([])
    for j in range(0, len(map_data_source[i])):
        if map_data_source[i][j] == 0:
            map_data_instance[i].append(main.EmptyBlock())
        elif map_data_source[i][j] == 1:
            map_data_instance[i].append(main.CollisionBlock())
        elif map_data_source[i][j] == 2:
            map_data_instance[i].append(main.EventBlock())

print(map_data_instance)
