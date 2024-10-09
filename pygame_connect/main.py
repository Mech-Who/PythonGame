import sys
from typing import List, Dict, Tuple, Union, Optional, Any, NoReturn

import pygame

from constant import Constant, ColorEnum
from config import Config

constant = Constant()
config = Config()

def init_all_objects():
    objects = {
        'screen': pygame.display.set_mode(config.screen_size),
        'clock': pygame.time.Clock(),
        'font': pygame.font.SysFont(pygame.font.get_default_font(), config.default_font_size),
        'ball': pygame.image.load("intro_ball.gif"),
    }
    objects['ball_rect'] = objects['ball'].get_rect()
    return objects

def frame_logic(objects: Dict):
    objects['game_name'] = objects['font'].render(constant.name, True, ColorEnum.white)
    
    w, h = config.screen_size

    objects['ball_rect'] = objects['ball_rect'].move(config.ball_speed)
    if objects['ball_rect'].left < 0 or objects['ball_rect'].right > w:
        config.ball_speed[0] = -config.ball_speed[0]
    if objects['ball_rect'].top < 0 or objects['ball_rect'].bottom > h:
        config.ball_speed[1] = -config.ball_speed[1]
    
    objects['screen'].fill(ColorEnum.black)
    objects['screen'].blit(objects['game_name'], (w/2, h/2))
    objects['screen'].blit(objects['ball'], objects['ball_rect'])

def main():
    # pygame setup
    pygame.init()
    # screen = pygame.display.set_mode(config.screen_size)
    # clock = pygame.time.Clock()

    objects = init_all_objects()

    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        objects['screen'].fill(config.background_color)

        # RENDER YOUR GAME HERE
        frame_logic(objects)

        # flip() the display to put your work on screen
        pygame.display.flip()

        objects['clock'].tick(config.limit_fps)  # limits FPS to 60

    pygame.quit()

if __name__ == '__main__':
    main()
