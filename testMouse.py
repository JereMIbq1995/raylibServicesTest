import os
from pygame.draw import circle
from pyray import *

from raylib.colors import RAYWHITE, LIGHTGRAY, BLACK, WHITE, VIOLET, RED, BLUE, GREEN
WHITE = (255,255,255,255)
VEL = 5
from genie.cast.actor import Actor
from genie.services import RaylibScreenService
from genie.services import RaylibKeyboardService, keys
from genie.services import RaylibMouseService, mouse

def main():
    screen_width = 800
    screen_height = 600

    screen_service = RaylibScreenService((screen_width, screen_height), "Astroid")
    keyboard_service = RaylibKeyboardService()
    mouse_service = RaylibMouseService()

    large_astroid = Actor("assets/astroids/astroid_large.png", 175, 175, 400, 300, rotation_vel = 1)
    cast = []
    cast.append(large_astroid)

    # texture = load_texture("assets/astroids/astroid_large.png")
    # frame_width = large_astroid.get_width()
    # frame_height = large_astroid.get_height()

    screen_service.set_fps(60)
    circle = { 'x' : 400, 'y' : 300, 'radius': 100 }
    while not screen_service.is_quit():
        
        # Input phase
        # Keyboard

        if (mouse_service.is_button_pressed(mouse.LEFT)):
            print("LEFT mouse pressed!")
        if (mouse_service.is_button_down(mouse.RIGHT)):
            print("RIGHT mouse down!")
        if (mouse_service.is_button_down(mouse.MIDDLE)):
            print("MIDDLE mouse down!")
        if (mouse_service.is_button_pressed(mouse.BACK)):
            print("BACK pressed!")
        if (mouse_service.is_button_pressed(mouse.FORWARD)):
            print("FORWARD pressed!")
        
        # if (mouse_service.has_mouse_moved()):
        mouse_coor = mouse_service.get_current_coordinates()
        large_astroid.set_position(mouse_coor[0], mouse_coor[1])
        
        mouse_wheel_move = mouse_service.get_mouse_wheel_move()

        if mouse_wheel_move != 0.0:
            print(mouse_wheel_move)
        
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