import os
# from pyray import *
from raylib.colors import RAYWHITE, LIGHTGRAY, BLACK, WHITE, VIOLET, RED, BLUE, GREEN

from genie.cast.actor import Actor
from genie.services import RaylibScreenService

def main():
    screen_width = 800
    screen_height = 600

    screen_service = RaylibScreenService((screen_width, screen_height), "Astroid")
    screen_service.set_fps(60)

    large_astroid = Actor("assets/astroids/astroid_large.png", 175, 175, 400, 300, 1, 1,)
    cast = []
    cast.append(large_astroid)

    # texture = load_texture("assets/astroids/astroid_large.png")
    frame_width = large_astroid.get_width()
    frame_height = large_astroid.get_height()


    while not screen_service.is_quit():

        screen_service.begin_drawing()
        screen_service.fill_screen(WHITE)
        
        screen_service.draw_actor(large_astroid)
        # screen_service.draw_circle((400,300), 400, RED)
        # screen_service.draw_rectangle((400,300), 100, 100, VIOLET, 10)
        # screen_service.draw_actors(cast)
        
        


        # draw_texture_pro(texture,
        #                             Rectangle(0,0,texture.width,texture.height),
        #                             Rectangle(large_astroid.get_x(), large_astroid.get_y(), frame_width, frame_height),
        #                             Vector2(frame_width/2, frame_height/2),
        #                             large_astroid.get_rotation(),
        #                             WHITE)
        
        screen_service.update_screen()

        large_astroid.move_with_vel()
        # pos_x +=1
        # pos_y +=1
        # rotation += 1

    screen_service.close_window()

if __name__ == "__main__":
    main()