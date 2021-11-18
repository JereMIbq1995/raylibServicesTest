from genie.services import RaylibKeyboardService
from genie.services import RaylibScreenService
from genie.services import keys
from genie.cast.actor import Actor
from genie.services.raylib_services.RaylibAudioService import RaylibAudioService
from genie.services.raylib_services.RaylibPhysicsService import RaylibPhysicsService
WHITE = (255, 255, 255, 255)
VEL = 5

def main():
    screen_width = 800
    screen_height = 600

    screen_service = RaylibScreenService((screen_width, screen_height), "Astroid")
    keyboard_service = RaylibKeyboardService()
    physics_service = RaylibPhysicsService()
    audio_service = RaylibAudioService()

    large_astroid = Actor("assets/astroids/astroid_large.png", 175, 175, 200, 200, rotation_vel = 1)
    cast = []
    cast.append(large_astroid)

    screen_service.set_fps(60)

    while not keyboard_service.is_quit():
        # Input

        if keyboard_service.is_key_down(keys.LEFT):
            large_astroid.set_vx(-VEL)
        if keyboard_service.is_key_down(keys.RIGHT):
            large_astroid.set_vx(VEL)
        if keyboard_service.is_key_down(keys.UP):
            large_astroid.set_vy(-VEL)
        if keyboard_service.is_key_down(keys.DOWN):
            large_astroid.set_vy(VEL)

        if not (keyboard_service.is_key_down(keys.LEFT) or keyboard_service.is_key_down(keys.RIGHT)):
            large_astroid.set_vx(0)
        if not (keyboard_service.is_key_down(keys.UP) or keyboard_service.is_key_down(keys.DOWN)):
            large_astroid.set_vy(0)
        
        if keyboard_service.is_key_pressed(keys.SPACE):
            audio_service.play_sound("assets/sound/bullet_shot.wav")
        

        # Update
        physics_service.move_actors(cast)
        physics_service.rotate_actors(cast)

        # Output
        screen_service.begin_drawing()
        screen_service.fill_screen(WHITE)
        screen_service.draw_actors(cast)
        screen_service.update_screen()

    

if __name__ == "__main__":
    main()