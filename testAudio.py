import os
from pygame.draw import circle
from pyray import *

from raylib.colors import RAYWHITE, LIGHTGRAY, BLACK, WHITE, VIOLET, RED, BLUE, GREEN
WHITE = (255,255,255,255)
VEL = 5
from genie.cast.actor import Actor
from genie.services import RaylibScreenService
from genie.services import RaylibKeyboardService, raylib_keys as keys
from genie.services import RaylibAudioService

def main():
    screen_width = 800
    screen_height = 600

    screen_service = RaylibScreenService((screen_width, screen_height), "Astroid")
    keyboard_service = RaylibKeyboardService()
    audio_service = RaylibAudioService()

    large_astroid = Actor("assets/astroids/astroid_large.png", 175, 175, 400, 300, rotation_vel = 1)
    cast = []
    cast.append(large_astroid)

    screen_service.set_fps(60)
    circle = { 'x' : 400, 'y' : 300, 'radius': 100 }
    while not screen_service.is_quit():
        
        # Input phase
        if (keyboard_service.is_key_down(keys.SPACE)):
            screen_service.draw_circle((200,200), 50, RED)

        if (keyboard_service.is_key_pressed(keys.SPACE)):
            audio_service.play_sound("assets/sound/bullet_shot.wav", 0.5)

        # Update
        large_astroid.move_with_vel()
        large_astroid.rotate()

        # Output phase
        screen_service.begin_drawing()
        screen_service.fill_screen(WHITE)
        screen_service.draw_actors(cast)
        screen_service.update_screen()



    screen_service.close_window()

if __name__ == "__main__":
    main()