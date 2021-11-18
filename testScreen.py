import os
from pygame.draw import circle
from pyray import *

from raylib.colors import PINK, RAYWHITE, LIGHTGRAY, BLACK, WHITE, VIOLET, RED, BLUE, GREEN
WHITE = (255,255,255,255)
VEL = 5
from genie.cast.actor import Actor
from genie.services import RaylibScreenService

def test_draw_circle(screen_service, circle):
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, False, False, False, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, False, False, False, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, False, False, True, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, False, False, True, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 50, False, True, False, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, False, True, False, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, False, True, True, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, False, True, True, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, True, False, False, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, True, False, False, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, True, False, True, False)
    screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, True, False, True, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, True, True, False, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, True, True, False, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, True, True, True, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 5, True, True, True, True)

    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, False, False, False, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, False, False, False, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, False, False, True, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, False, False, True, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, False, True, False, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, False, True, False, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, False, True, True, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, False, True, True, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, True, False, False, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, True, False, False, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, True, False, True, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, True, False, True, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, True, True, False, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, True, True, False, True)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, True, True, True, False)
    # screen_service.draw_circle((circle['x'], circle['y']), circle['radius'], BLACK, 0, True, True, True, True)

def main():
    screen_width = 800
    screen_height = 600

    screen_service = RaylibScreenService((screen_width, screen_height), "Astroid")

    large_astroid = Actor("assets/astroids/astroid_large.png", 175, 175, 200, 200, rotation_vel = 1)
    cast = []
    cast.append(large_astroid)

    # texture = load_texture("assets/astroids/astroid_large.png")
    # frame_width = large_astroid.get_width()
    # frame_height = large_astroid.get_height()

    font = load_font("genie/services/raylib_services/Fonts/calibri.ttf")
    text_image = image_text_ex(font, "Hello World!", 72, 0, BLACK)
    texture = load_texture_from_image(text_image)
    text_size = 72

    screen_service.set_fps(60)
    circle = { 'x' : 400, 'y' : 300, 'radius': 100 }
    while not screen_service.is_quit():
        
        # Input phase
        # Keyboard        
        rsf = text_size / 72


        # Output phase
        screen_service.begin_drawing()
        screen_service.fill_screen(WHITE)

        screen_service.draw_text("Hello World!", font_size = 24, color=BLACK, position = (400,300), position_center=True)
        screen_service.draw_rectangle((400,300), 300, 100, PINK, 2, 2)
        test_draw_circle(screen_service, circle)
        screen_service.draw_actors(cast)

        
        # These lines of code test the drawing of different sectors of a circle
        

        screen_service.update_screen()

        large_astroid.move_with_vel()
        large_astroid.rotate()
        # pos_x +=1
        # pos_y +=1
        circle["x"] += 1
        circle["y"] += 1

    screen_service.close_window()

if __name__ == "__main__":
    main()