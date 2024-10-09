"""
参考CSDN:
- https://blog.csdn.net/cxhold/article/details/139853348
- https://blog.csdn.net/cxhold/article/details/139859422
"""
import pygame
import sys
from pygame.locals import *
import time
import traceback
import os,random


def main():
    pygame.init()
    game_size = width,height = 700,500
    bg_color = (255,255,255)  #白色底
    game_cols = 6
    game_rows = 6
    imgs_repeat =  game_cols * game_rows / 4
    cell_size = 40
    
    small_imgs = []    #新增
    
    cur_game = []    #游戏, 新增
    tmp_game = []    #临时游戏内容, 新增
    mid_game = []    #中间游戏, 新增

    EMPTYCELL = -1   #新增

    '''
    分割小图标
    '''
    def splitImg():
        llk_base = pygame.image.load("imgs\\llk.png")  #图片加载成功后，pygame将图片转换为一个Surface对象
        for i in range(0, int(imgs_repeat)):
            i_left = i * cell_size
            small_imgs.append(llk_base.subsurface(i_left,0,cell_size,cell_size))

    '''
    初始化游戏
    '''
    def initGame():
        for i in range(0, int(imgs_repeat)):
            for j in range(0, 4):
                tmp_game.append(i)

        total = game_cols * game_rows
        for x in range(0, total):
            index = random.randint(0, total - x - 1)
            mid_game.append(tmp_game[index])
            del tmp_game[index]

        # 一维转为二维，y为高
        for y in range(0, game_rows):
            for x in range(0, game_cols):
                if x == 0:
                    cur_game.append([])
                cur_game[y].append(mid_game[x + y * game_rows])

    pygame.display.set_caption('Hi,连连看！')

    '''
    显示   game_screen.blit(small_imgs[0],(x_position,y_position))
    '''
    def drawGame():
        game_screen.fill(bg_color)
        for y in range(0, game_rows):
            for x in range(0, game_cols):
                if cur_game[y][x] != EMPTYCELL:
                    game_screen.blit(small_imgs[cur_game[y][x]],(x_position + x * cell_size,y_position + y * cell_size))
        pygame.display.flip()

    '''    
    让游戏界面居中显示
    '''
    os.environ['SDL_VIDEO_CENTERED'] = '1' 
    game_screen = pygame.display.set_mode(game_size)  
    # 获取屏幕的宽度和高度
    game_screen_width = game_screen.get_width()
    game_screen_height = game_screen.get_height()
    
    # 计算图片应该被放置的位置，使其居中
    x_position = (game_screen_width // 2) - (game_cols * cell_size // 2)
    y_position = (game_screen_height // 2) - (game_rows * cell_size // 2)

    splitImg()

    game_screen.fill(bg_color)   #1、填充背景颜色，这样也把上一次的图像刷掉了。
    
    initGame()
    drawGame()

    pygame.display.flip() #3、双缓冲机制，一次性将缓冲好的内容显示在屏幕上

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # 检查鼠标事件
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                print("鼠标点击:", event.pos[0], event.pos[1])
                

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()