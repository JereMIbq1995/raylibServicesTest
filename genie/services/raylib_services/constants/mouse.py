from pyray import *
from genie.services.constants.mouse import *

mouse_map = {
    LEFT : MOUSE_BUTTON_LEFT,      # index for Left mouse
    MIDDLE : MOUSE_BUTTON_MIDDLE,    # index for Middle mouse
    RIGHT : MOUSE_BUTTON_RIGHT,     # index for Right mouse

    # If mouse has more than 3 buttons:
    EXTRA1 : MOUSE_BUTTON_EXTRA,
    
    SIDE : MOUSE_BUTTON_SIDE,
    FORWARD : MOUSE_BUTTON_FORWARD,
    BACK : MOUSE_BUTTON_BACK
}