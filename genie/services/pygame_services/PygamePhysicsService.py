import pygame
from genie.cast.actor import Actor

class PygamePhysicsService:
    def __init__(self):
        if not pygame.get_init():
            pygame.init()

    def _get_rectangle(self, actor: Actor):
        return pygame.Rect(actor.get_top_left()[0], actor.get_top_left()[1], actor.get_width(), actor.get_height())

    def rotate_actors(self, actors : list):
        for actor in actors:
            actor.rotate()

    def move_actors(self, actors : list):
        for actor in actors:
            actor.move_with_vel()

    def check_collision(self, actor1 : Actor, actor2 : Actor):
        """
            - create pygame.Shape
            - call colliderect
        """
        return self._get_rectangle(actor1) \
                .colliderect(
                self._get_rectangle(actor2)
                )
    
    def check_collision_list(self, target: Actor, actors: list):
        """
            return the first actor in the actors list that collides with target
            If target doesn't collide with any of the actors, return -1
        """
        for actor in actors:
            if self._get_rectangle(target).colliderect(self._get_rectangle(actor)):
                return actor
        return -1
    
    def check_collision_all(self, target: Actor, actors: list):
        """
            return True if target collides with all of the actors
                    False if there's 1 actor that doesn't collide with target
        """
        for actor in actors:
            if not self._get_rectangle(target).colliderect(self._get_rectangle(actor)):
                return False
        return True

    def is_above(self, actor1 : Actor, actor2 : Actor):
        """
            Return true if actor1 is above actor2, and false otherwise
        """
        return actor1.get_top_left()[1] < actor2.get_top_left()[1]

    def is_below(self, actor1 : Actor, actor2 : Actor):
        """
            Return true if actor1 is below actor2, false otherwise
        """
        return actor1.get_bottom_left()[1] > actor2.get_bottom_left()[1]

    def is_left_of(self, actor1 : Actor, actor2 : Actor):
        """
            Return true if actor1 is on the left of actor2, false otherwise
        """
        return actor1.get_top_left()[0] < actor2.get_top_left()[0]

    def is_right_of(self, actor1 : Actor, actor2 : Actor):
        """
            Return true if actor1 is on the right of actor2, false otherwise
        """
        return actor1.get_top_right()[0] > actor2.get_top_right()[0]