# coding=UTF-8

import pygame
import os


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始化位置"""
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载图片
        self.image = pygame.image.load(
            os.getcwd() + '/python/game/images/ship.bmp')
        # 获取图片矩形
        self.rect = self.image.get_rect()
        # 获取屏幕矩形
        self.screen_rect = screen.get_rect()

        # print("-------------------")
        # print(self.rect)
        # print(self.screen_rect)
        # print(self.screen_rect.centerx)
        # print(self.screen_rect.bottom)
        # print("-------------------")

        self.rect.centerx = self.screen_rect.centerx
        # self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        # rect 中只能存储整数，另起一个遍历存储小数
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """指定位置绘制"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
