class Actor:
    """
        A thing that participates in an animation. Anything that either MOVES, can be DRAWN
        on the screen, or BOTH is an actor.
        For the purpose of collision checking, all actors are represented with the shape of a RECTANGLE.
        
        Attributes:
            _x : the x coordinate of the center of the rectangle
            _y : the y coordinate of the position
            _vx : the horizontal velocity
            _vy : the vertical velocity
            _height : 
    """
    def __init__(self, path : str,
                    width : int,
                    height : int,

                    x : float = 0, 
                    y : float = 0,
                    
                    vx : float = 0,
                    vy : float = 0,

                    rotation : float = 0,
                    rotation_vel : float = 0):
        """
            Initialize the actor using the image and
            a scaling factor, or width and height
        """

        self._path = path

        self._width = width
        self._height = height

        self._x = x
        self._y = y

        self._vx = vx
        self._vy = vy

        self._rotation = rotation
        self._rotation_vel = rotation_vel
        
    # Path
    def get_path(self):
        return self._path
    
    def set_path(self, path):
        self._path = path
    
    # Getters and setters for width and height
    def get_width(self):
        return self._width
    
    def set_width(self, width):
        self._width = width
    
    def get_height(self):
        return self._height
    
    def set_height(self, height):
        self._height = height

    def scale(self, scale):
        self._width *= scale
        self._height *= scale
    
    # Getters and setters for x and y
    def get_x(self):
        return self._x
    
    def set_x(self, x):
        self._x = x
    
    def get_y(self):
        return self._y
    
    def set_y(self, y):
        self._y = y
    
    # Getters and setters for position
    def get_position(self):
        return (self._x, self._y)
    
    def set_position(self, x, y):
        self._x = x
        self._y = y
    
    # Getters for top-left corner of the rectangle
    def get_top_left(self):
        return (self._x - self._width / 2, self._y - self._height / 2)
    
    def get_top_right(self):
        return (self._x + self._width / 2, self._y - self._height / 2)

    def get_bottom_left(self):
        return (self._x - self._width / 2, self._y + self._height / 2)
    
    def get_bottom_right(self):
        return (self._x + self._width / 2, self._y + self._height / 2)

    # Getters and setters for velocity
    def get_vx(self):
        return self._vx
    
    def set_vx(self, vx):
        self._vx = vx
    
    def get_vy(self):
        return self._vy
    
    def set_vy(self, vy):
        self._vy = vy
    
    # Getters and setters for rotation and rotation velocity
    def get_rotation(self):
        return self._rotation
    
    def set_rotation(self, rotation):
        self._rotation = rotation

    def get_rotation_vel(self):
        return self._rotation_vel
    
    def set_rotation_vel(self, rotation_vel):
        self._rotation_vel = rotation_vel

    # Move functions
    def move_with_vel(self):
        """
            Simply add vx and vy onto x and y respectively
        """
        self._x += self._vx
        self._y += self._vy
    
    def rotate(self):
        self._rotation += self._rotation_vel