import sys

import pygame


def check_events():
    """监听键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最新绘制的屏幕可见
    pygame.display.flip()
