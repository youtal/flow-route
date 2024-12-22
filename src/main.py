from map_process import *
from src.utils.fetch_data import fetch_all_room_info
from utils import *


def main():
    map_str = get_room_info('W12N15', 'shard0')
    print(map_str)
    cost_map = init_map(map_str)
    for j in range(50):
        for i in range(50):
            print(f'{cost_map[j][i]["cost"]:3}', end=' ')
        print()
    cost_grid = bfs_fill(cost_map, 21, 31)
    for row in cost_grid:
        print(row)
    dir_grid = config_direction_idx(cost_grid)
    for row in dir_grid:
        print(row)
    generate_image_from_dir(dir_grid, 'output/result.png', 21, 31)


if __name__ == '__main__':
    test()
