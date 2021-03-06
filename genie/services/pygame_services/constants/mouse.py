import pygame
from genie.services.constants.mouse import *

mouse_map = {
    LEFT : 0,      # index for Left mouse
    MIDDLE : 1,    # index for Middle mouse
    RIGHT : 2,     # index for Right mouse

    # If mouse has more than 3 buttons:
    # (there are only 2 more since Pygame only support 5)
    EXTRA1 : 3,
    EXTRA2 : 4
}