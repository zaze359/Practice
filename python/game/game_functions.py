# coding=UTF-8

import sys

import pygame


def check_events(ship):
    # 监听键盘和鼠标事件
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    # 填充背景
    screen.fill(ai_settings.bg_color)
    # 绘制飞船
    ship.blitme()
    # 屏幕可见
    pygame.display.flip()
