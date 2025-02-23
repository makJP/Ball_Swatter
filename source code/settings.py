import pygame

WINDOW_NAME = "BALL SWATTER"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1440,900

FPS = 90
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
REDS_SIZES = (50,50)
RED_SIZE_RANDOMIZE = (1,2) # for each new red ball, it will multiply the size with an random value beteewn X and Y
GREENS_SIZES = (50, 50)
GREEN_SIZE_RANDOMIZE = (1.2, 1.5)

# drawing
DRAW_HITBOX = False # will draw all the hitbox

# animation
ANIMATION_SPEED = 0.08 # the frame of the balls will change every X sec

# difficulty
GAME_DURATION = 60 # the game will last X sec
REDS_SPAWN_TIME = 1
REDS_MOVE_SPEED = {"min": 1, "max": 5}
GREEN_PENALITY = 1 # will remove X of the score of the player (if he kills a GREEN BALL)

# colors
COLORS = {"title": (255, 255, 255), "score": (255, 255, 255), "timer": (255, 255, 255),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (0, 0, 0)}} # second is the color when the mouse is on the button

# sounds / music
MUSIC_VOLUME = 0.16 # value between 0 and 1
SOUNDS_VOLUME = 1

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
