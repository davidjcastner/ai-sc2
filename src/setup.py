import os
import random
import shutil

MAP_SRC_DIR = './maps'
MAP_DST_DIR = 'C:\\Program Files (x86)\\StarCraft II\\Maps'


def setup() -> None:
    copy_maps()


def copy_maps() -> None:
    '''only copy the maps if it does not exist in the StarCraft II directory'''
    for map_file in os.listdir(MAP_SRC_DIR):
        if map_file.endswith('.SC2Map'):
            if not os.path.isfile(os.path.join(MAP_DST_DIR, map_file)):
                shutil.copy(os.path.join(MAP_SRC_DIR, map_file), os.path.join(MAP_DST_DIR, map_file))


def is_valid_map(map_name: str) -> bool:
    return os.path.isfile(os.path.join(MAP_DST_DIR, map_name + '.SC2Map'))


def get_random_map() -> str:
    maps = [map_name for map_name in os.listdir(MAP_SRC_DIR) if map_name.endswith('.SC2Map')]
    return random.choice(maps).replace('.SC2Map', '')
