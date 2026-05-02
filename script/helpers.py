import os
import pygame

BASE_IMG_PATH = 'data/images/'
BASE_MAP_PATH = 'data/maps/'

def load_image(relative_path:str):
    return pygame.image.load(BASE_IMG_PATH+relative_path).convert()

def load_images(relative_folder_path:str):
    files = sorted(os.listdir(BASE_IMG_PATH+relative_folder_path))
    images = {}
    for filename in files:
        images[filename] = load_image(relative_folder_path + filename)
    return images

def load_all_assets():
    return {
            'player': (load_image('player.png')),
            'decor': load_images('tiles/decor/'),
            'large_decor': load_images('tiles/large_decor/'),
            'grass': load_images('tiles/grass/'),
            'stone': load_images('tiles/stone/'),
            'spawners': load_images('tiles/spawners/'),
            'clouds': load_images('clouds/'),
            
        }
def load_tilemap_assets():
    return {
            'decor': load_images('tiles/decor/'),
            'large_decor': load_images('tiles/large_decor/'),
            'grass': load_images('tiles/grass/'),
            'stone': load_images('tiles/stone/'),
            #;'spawners': load_images('tiles/spawners/'),
        }

def load_map(filename:str):
        with open(BASE_MAP_PATH + filename, 'r') as mapfile:
            pass
            #print(mapfile.readlines())
            