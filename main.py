import os
from pygame.draw import circle
from pyray import *

# from raylib.colors import RAYsWHITE, LIGHTGRAY, BLACK, WHITE, VIOLET, RED, BLUE, GREEN
WHITE = (255,255,255,255)
VEL = 5
from genie.cast.actor import Actor
from genie.services import RaylibScreenService
from genie.services import RaylibKeyboardService, raylib_keys as keys
from genie.services import RaylibMouseService, raylib_mouse as mouse

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
    while not screen_service.is_quit():
        
        # Input phase
        # Keyboard
        if (keyboard_service.is_key_down(keys.LEFT)):
            large_astroid.set_vx(-VEL)
        if (keyboard_service.is_key_down(keys.RIGHT)):
            large_astroid.set_vx(VEL)
        if (keyboard_service.is_key_down(keys.UP)):
            large_astroid.set_vy(-VEL)
        if (keyboard_service.is_key_down(keys.DOWN)):
            large_astroid.set_vy(VEL)
        
        if (keyboard_service.is_key_down(keys.LEFT) and keyboard_service.is_key_down(keys.RIGHT)):
            large_astroid.set_vx(0)
        
        if (keyboard_service.is_key_down(keys.SPACE)):
            screen_service.draw_circle((20,20), 10, width = 2)
        
        if (keyboard_service.is_key_up(keys.LEFT) and keyboard_service.is_key_up(keys.RIGHT)):
            large_astroid.set_vx(0)
        if (keyboard_service.is_key_up(keys.UP) and keyboard_service.is_key_up(keys.DOWN)):
            large_astroid.set_vy(0)
        
        # Mouse:
        if (mouse_service.is_button_pressed(mouse.LEFT)):
            print("LEFT mouse down!")
        if (mouse_service.is_button_down(mouse.RIGHT)):
            print("RIGHT mouse down!")
        if (mouse_service.is_button_down(mouse.MIDDLE)):
            print("MIDDLE mouse down!")
        if (mouse_service.is_button_pressed(mouse.BACK)):
            print("BACK scroll!")
        if (mouse_service.is_button_pressed(mouse.FORWARD)):
            print("FORWARD scroll!")
        
        if (mouse_service.has_mouse_moved()):
            mouse_coor = mouse_service.get_current_coordinates()
            large_astroid.set_position(mouse_coor[0], mouse_coor[1])

        mouse_wheel_move = mouse_service.get_mouse_wheel_move()
        if mouse_wheel_move != 0.0:
            print(mouse_wheel_move)
        # print(mouse_service.get_current_coordinates())
        # print(mouse_service.has_mouse_moved())

        # Update


        # Output phase
        screen_service.begin_drawing()
        screen_service.fill_screen(WHITE)
        screen_service.draw_actors(cast)

        # center = large_astroid.get_position()
        # path = large_astroid.get_path()
        # if path in texture_caches.keys():
        #     texture = texture_caches[path]
        # else:
        #     texture = load_texture(path)
        #     texture_caches[path] = texture
        
        # frame_width = large_astroid.get_width()
        # frame_height = large_astroid.get_height()

        # draw_texture_pro(texture,
        #                 Rectangle(0,0,texture.width,texture.height),
        #                 Rectangle(center[0], center[1], frame_width, frame_height),
        #                 Vector2(frame_width/2, frame_height/2),
        #                 large_astroid.get_rotation(),
        #                 WHITE)
        
        # screen_service.draw_circle((400,300), 400, RED)
        # screen_service.draw_rectangle((400,300), 100, 100, VIOLET, 10)
        # screen_service.draw_actors(cast)
        
        screen_service.update_screen()

        large_astroid.move_with_vel()
        # pos_x +=1
        # pos_y +=1
        large_astroid.rotate()

    screen_service.close_window()

if __name__ == "__main__":
    main()