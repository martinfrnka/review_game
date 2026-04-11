import os
import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(relative_path:str):
    return pygame.image.load(BASE_IMG_PATH+relative_path).convert()

def load_images(relative_folder_path:str):
    files = sorted(os.listdir(BASE_IMG_PATH+relative_folder_path))
    images = {}
    for filename in files:
        images[filename] = load_image(relative_folder_path + filename)
    return images