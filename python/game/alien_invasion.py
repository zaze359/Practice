# coding=UTF-8

import pygame

from settings import Settings
from ship import Ship

import game_functions as gf


def run_game():
    # 初始化
    pygame.init()

    ai_settings = Settings()
    # set_mode 设置窗口尺寸 1200x800
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen=screen, ai_settings=ai_settings)

    # 游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        # 更新屏幕
        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship)


# 运行
run_game()
