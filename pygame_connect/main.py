import sys
from typing import List, Dict, Tuple, Union, Optional, Any, NoReturn

import pygame

from constant import Constant, ColorEnum
from config import Config

constant = Constant()
config = Config()

def main():
    # pygame setup
    pygame.init()
    # screen = pygame.display.set_mode(config.screen_size)
    # clock = pygame.time.Clock()

    screen = pygame.display.set_mode(config.screen_size)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(pygame.font.get_default_font(), config.default_font_size)
    ball = pygame.image.load("intro_ball.gif")
    ball_rect = ball.get_rect()

    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(config.background_color)

        # RENDER YOUR GAME HERE
        game_name = font.render(constant.name, True, ColorEnum.white)
    
        w, h = config.screen_size

        ball_rect = ball_rect.move(config.ball_speed)
        if ball_rect.left < 0 or ball_rect.right > w:
            config.ball_speed[0] = -config.ball_speed[0]
        if ball_rect.top < 0 or ball_rect.bottom > h:
            config.ball_speed[1] = -config.ball_speed[1]
        
        screen.fill(ColorEnum.black)
        screen.blit(game_name, (w/2, h/2))
        screen.blit(ball, ball_rect)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(config.limit_fps)  # limits FPS to 60

    pygame.quit()

if __name__ == '__main__':
    main()
