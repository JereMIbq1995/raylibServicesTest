import os
from pyray import *
from raylib.colors import RAYWHITE, LIGHTGRAY, BLACK, WHITE, VIOLET, RED, BLUE, GREEN

def main():
    screen_width = 800
    screen_height = 600

    init_window(screen_width, screen_height, "raylib test")
    image = load_image("assets/astroids/astroid_large.png")
    image_resize(image, 100, 100)
    texture = load_texture_from_image(image)
    
    pos_x = 400
    pos_y = 300
    rotation = 0
    set_target_fps(60)

    while not window_should_close():

        begin_drawing()
        clear_background(VIOLET)
        
        # draw_texture(texture, 100, 100, WHITE)
        # draw_texture_ex(texture, Vector2(100,100), rotation, 1, WHITE)
        
        draw_texture_pro(texture, Rectangle(0,0, texture.width, texture.height), Rectangle(pos_x,pos_y, texture.width*2, texture.height*4), Vector2(texture.width, 2*texture.height), rotation, WHITE)
        # draw_texture_tiled(texture, Rectangle(0,0, texture.width, texture.height), Rectangle(pos_x,pos_y, texture.width*3, texture.height*3), Vector2(0,0), rotation, 1, WHITE)

        draw_circle(pos_x,pos_y, 5, RED)
        draw_text("Congrats! You created your first window!", 190, 200, 20, GREEN)
        end_drawing()

        # pos_x +=1
        # pos_y +=1
        rotation += 1

    close_window()

if __name__ == "__main__":
    main()