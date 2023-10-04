import pygame

pygame.init()
screen = pygame.display.set_mode((1380, 820))  # flags=pygame.NOFRAME)  # размер экрана
pygame.display.set_caption("призраки в лесу")
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)
bg_x = 0


def beck_ground():
    """русует задний фон"""
    bg = pygame.image.load('images/9.jpg')
    return bg


def player_stop():
    """персонаж стоит на месте"""
    p_s = pygame.image.load('images/player_right/5.png').convert_alpha()
    return p_s


def wolk_right():
    """движение персонажа в право"""
    w_r = [pygame.image.load('images/player_right/1.png').convert_alpha(),
           pygame.image.load('images/player_right/2.png').convert_alpha(),
           pygame.image.load('images/player_right/3.png').convert_alpha(),
           pygame.image.load('images/player_right/4.png').convert_alpha(),
           pygame.image.load('images/player_right/5.png').convert_alpha(),
           pygame.image.load('images/player_right/6.png').convert_alpha(),
           pygame.image.load('images/player_right/7.png').convert_alpha(),
           pygame.image.load('images/player_right/8.png').convert_alpha(),
           pygame.image.load('images/player_right/9.png').convert_alpha(),
           pygame.image.load('images/player_right/10.png').convert_alpha()
           ]
    return w_r


def wolk_left():
    """движение персонажа в лево"""
    w_l = [pygame.image.load('images/player_left/1.png').convert_alpha(),
           pygame.image.load('images/player_left/2.png').convert_alpha(),
           pygame.image.load('images/player_left/3.png').convert_alpha(),
           pygame.image.load('images/player_left/4.png').convert_alpha(),
           pygame.image.load('images/player_left/5.png').convert_alpha(),
           pygame.image.load('images/player_left/6.png').convert_alpha(),
           pygame.image.load('images/player_left/7.png').convert_alpha(),
           pygame.image.load('images/player_left/8.png').convert_alpha(),
           pygame.image.load('images/player_left/9.png').convert_alpha(),
           pygame.image.load('images/player_left/10.png').convert_alpha(),
           ]
    return w_l
