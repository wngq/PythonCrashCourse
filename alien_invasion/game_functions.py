import sys

import pygame


def check_events(ship):
    """监听键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出游戏
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # 向左移动飞船
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            # 按键松开时，停止移动
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最新绘制的屏幕可见
    pygame.display.flip()
