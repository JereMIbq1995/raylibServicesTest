from pyray import *
from raylib.colors import *

from genie.cast.actor import Actor

class RaylibScreenService:
    """
        - add methods to the interface
            i.e. ScreenService.DrawImages(Actors)
            (this is in core)
        - create the trait Image
            i.e. image
        - Implement the methods in concrete class
            i.e. PygameScreenService
            A. Loop Through Actors
            If has Image trait:
                convert image data to what pygame needs
                use pygame to draw
    """
    def __init__(self, window_size, title : str = ""):
        # if not pyray.is_window_ready():
        #     print("window initialized!")
        init_window(window_size[0], window_size[1], title)
        self._textures_cache = {}
    
    def initialize(self):
        pass
    
    def set_fps(self, fps : int = 60):
        set_target_fps(fps)

    def _load_texture(self, actor : Actor):
        """
            Takes in an actor that has 2 traits: Body and Image
                and load the image of that Actor into the cache
        """
        image_path = actor.get_path()
        # print("2")
        texture = load_texture(image_path)
        
        # put image in cache so we don't have to load again
        if (image_path not in self._textures_cache.keys()):
            self._textures_cache[image_path] = texture

        return texture

    def load_textures(self, actors : list):
        """
            load all the images into a dictionary cache
        """
        for actor in actors:
            self._load_texture(actor)

    def fill_screen(self, color = WHITE):
        """
            Fill the screen with a certain color
        """
        clear_background(color)

    def begin_drawing(self):
        """
            What to call before drawing anything in a frame
        """
        begin_drawing()

    def update_screen(self):
        """
            Actually putting whatever was drawn on to the screen
        """
        end_drawing()

    def close_window(self):
        close_window()

    def is_quit(self):
        return window_should_close()

    # def get_text_image(self):
    #     font = pygame.font.SysFont(font, font_size)
    #     text_image = font.render(text, antialias, color)

    def draw_text(self, text : str, font : str = None, font_size : int = 24, 
                    color : tuple = (0, 0, 0), position : tuple = (0, 0),
                    antialias : bool = True, position_center : bool = False):
        """
            Draw the input text (str).
            Inputs:
                - text: The text you want to draw
                - font: The font you want to use (try to find out what's
                        available on your system first)
                - font_size: default is 24
                - color: An RGB tuple. (0,0,0) is BLACK, and (255,255,255) is WHITE
                        You can also pass a 4 entries tuple. the 4th entry determines opacity
                - position: A tuple in the form of (x, y)
                - antialias: Boolean. Default is True
                - position_center: A boolean that tells whether the position given should be
                                    the center of the text image or the top-left corner.
                        + True: treats the position as the center of the text image
                        + False: treats the position as the top-left corner of the text image

        """
        pass

    def draw_rectangle(self, center : tuple, width : int, height: int, color : tuple = (0, 0, 0), 
                        border_width : int = 0, roundness : float = 0):
        """
            Draw a rectangle.

            Input:
                - center: An (x, y) tuple indicating the center of the rectangle
                - width: the width of the rectangle
                - height: the height of the rectangle
                - color: An RGB tuple. (0,0,0) is BLACK, and (255,255,255) is WHITE
                        You can also pass a 4 entries tuple. the 4th entry determines opacity
                - border_width: how many pixels you want the border to be
                
                - border_radius, border_..._radius: use these parameters if you want your rectangle
                                     to have rounded corners.
                                        + values < 1 means squared corners
                                        + values >= 1 means rounded corners. Increase this
                                            to increase the roundness
        """
        topleft_x, topleft_y = center[0] - width/2, center[1] - height/2
    
        if border_width == 0:
            draw_rectangle_rounded(Rectangle(topleft_x, topleft_y, width, height), roundness, 60, color)
        elif border_width > 0:
            draw_rectangle_rounded_lines(Rectangle(topleft_x, topleft_y, width, height), roundness, 60, border_width, color)

    
    def draw_circle(self, center, radius, color : tuple = (0, 0, 0), width : int = 0,
                    draw_top_right : bool = False, draw_top_left : bool = False, draw_bottom_left : bool = False, 
                    draw_bottom_right : bool = False):
        """
            Draw a circle.

            Input:
                - center: A tuple represents center of the circle (x, y)
                - radius: Well...
                - color: RGB tuple (0,0,0) is BLACK, (255,255,255) is WHITE.
                        Can also use 4th entry to specify opacity
                - width: How bold you want the border of the circle to be

                - draw_top_..., draw_bottom_...: Boolean. Use these parameters if want to draw
                    only parts of the circle (top left, top right, bottom left, bottom right)
        """
        if width == 0:
            draw_circle(center[0], center[1], radius, color)
        elif width > 0:
            equiv_rec = Rectangle(center[0] - radius, center[1] - radius, 2*radius, 2*radius)
            draw_rectangle_rounded_lines(equiv_rec, 1, 60, width, color)
    
    def draw_actor(self, actor: Actor):
        center = actor.get_position()
        path = actor.get_path()
        try:
            # Load image from cache or from file
            texture = self._textures_cache[path] if path in self._textures_cache.keys() else self._load_texture(actor)
            
            frame_width = actor.get_width()
            frame_height = actor.get_height()
            # print(actor.get_rotation())
            draw_texture_pro(texture,
                            Rectangle(0,0,texture.width,texture.height),
                            Rectangle(center[0], center[1], frame_width, frame_height),
                            Vector2(frame_width/2, frame_height/2),
                            actor.get_rotation(),
                            WHITE)

            # This line of code when un-commented shows the hit box of the actor
            # draw_rectangle_lines(int(actor.get_top_left()[0]), int(actor.get_top_left()[1]), int(actor.get_width()), int(actor.get_height()),BLACK)
        except:
            print("Something went wrong in RaylibScreenService.draw_actor()! Most likely path not found!")

    def draw_actors(self, actors : list, lerp : float = 0):
        """
            Draw all the actors in the "actors" list in order:
                    First thing in the list gets drawn first.

            actors: actors that need to be drawn
            lerp: linear interpolation
        """
        for actor in actors:
            self.draw_actor(actor)
        
    def release(self):
        pass