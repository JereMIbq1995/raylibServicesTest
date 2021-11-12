import os
from pyray import *
# from raylib.colors import RAYsWHITE, LIGHTGRAY, BLACK, WHITE, VIOLET, RED, BLUE, GREEN
WHITE = (255,255,255,255)
from genie.cast.actor import Actor
from genie.services import RaylibScreenService

def main():
    screen_width = 800
    screen_height = 600

    screen_service = RaylibScreenService((screen_width, screen_height), "Astroid")

    large_astroid = Actor("assets/astroids/astroid_large.png", 175, 175, 400, 300, 1, 1, 0, 1)
    cast = []
    cast.append(large_astroid)

    # texture = load_texture("assets/astroids/astroid_large.png")
    # frame_width = large_astroid.get_width()
    # frame_height = large_astroid.get_height()

    texture_caches = {}

    screen_service.set_fps(60)
    while not screen_service.is_quit():

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