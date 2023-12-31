import pygame

from decor import beck_ground, wolk_right, wolk_left, player_stop
from utils import draw_text

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1380, 820))

player_anim_count = 0  # анимация персонажа
bg_x = 0
bg_sound = pygame.mixer.Sound('sounds/voice fon.mp3')

player_speed = 15  # скорость перемещения персоножа
player_x = 150  # координата начального положения персонажа x
player_y = 530  # координата начального положения персонажа y
player_rectangl = pygame.image.load('images/player_right/1.png')

ghost = pygame.image.load('images/ghost.png')
ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 3000)  # таймер появления призраков
ghost_list_in_game = []

reload = pygame.image.load('images/reload.png')
reload_timer = pygame.USEREVENT + 2
pygame.time.set_timer(reload_timer, 15000)
reload_list_in_game = []

stone = pygame.image.load('images/stone.png')
stone_timer = pygame.USEREVENT + 3
pygame.time.set_timer(stone_timer, 20000)
stone_list_in_game = []

is_jump = False
jump_count = 10

pygame.init()

label = pygame.font.Font('fonts/RobotoMono-Italic-VariableFont_wght.ttf', 100)
lose_lable = label.render('Ты Умер', False, ('black'))
restart_lable = label.render('играть снова', False, ('blue'))
restart_lable_rect = restart_lable.get_rect(topleft=(300, 500))

set_score = 0
bullets_left = 10  # счетчик выстрелов

bullet = pygame.image.load('images/paintball.png').convert_alpha()
bullets = []

gameplay = True
running = True

while running:
    keys = pygame.key.get_pressed()
    screen.blit(beck_ground(), (bg_x, 0))
    screen.blit(beck_ground(), (bg_x + 1380, 0))
    draw_text(screen, str(bullets_left), 50, 30, 10)  # отображение счетчика выстрелов
    draw_text(screen, 'score' + ' - ' + str(set_score), 50, 1100, 10)

    if gameplay:
        player_rect = player_rectangl.get_rect(topleft=(player_x, player_y))

        if ghost_list_in_game:
            for (i, element) in enumerate(ghost_list_in_game):
                screen.blit(ghost, element)
                element.x -= 15

                if element.x < - 10:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(element):
                    gameplay = False

        if reload_list_in_game:
            for (r, elements) in enumerate(reload_list_in_game):
                screen.blit(reload, elements)
                elements.x -= 50

                if elements.x < - 10:
                    reload_list_in_game.pop(r)

                if player_rect.colliderect(elements):
                    bullets_left += 10
                    reload_list_in_game.pop(r)

        if stone_list_in_game:
            for (s, el) in enumerate(stone_list_in_game):
                screen.blit(stone, el)
                el.x -= 30
            if el.x < - 10:
                stone_list_in_game.pop(s)

        if keys[pygame.K_LEFT]:
            screen.blit(wolk_left()[player_anim_count], (player_x, player_y))
        elif keys[pygame.K_RIGHT]:
            screen.blit(wolk_right()[player_anim_count], (player_x, player_y))
        else:
            screen.blit(player_stop(), (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 30:  # раница перемещения в лево
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 1250:  # граница перемещения в право
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -10:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10

        if player_anim_count == 9:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -1380:
            bg_x = 0

        if bullets:
            for (i, elem) in enumerate(bullets):
                screen.blit(bullet, (elem.x, elem.y))
                elem.x += 25

                if elem.x > 1850:
                    bullets.pop(i)

                if ghost_list_in_game:
                    for (index, ghost_el) in enumerate(ghost_list_in_game):
                        if elem.colliderect(ghost_el):
                            ghost_list_in_game.pop(index)
                            bullets.pop(i)
                            set_score += 1

                if stone_list_in_game:
                    for (index, stone_el) in enumerate(stone_list_in_game):
                        if elem.colliderect(stone_el):
                            bullets.pop(i)
                            if player_rect.contains(stone_el):
                                gameplay = False


    else:
        screen.fill('red')
        screen.blit(lose_lable, (500, 300))
        screen.blit(restart_lable, restart_lable_rect)

        mouse = pygame.mouse.get_pos()
        if restart_lable_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ghost_list_in_game.clear()
            stone_list_in_game.clear()
            bullets.clear()
            bullets_left = 10
            set_score = 0
            is_jump = False

    pygame.display.update()  # обновление экрана

    for event in pygame.event.get():  # event список всех возможных событий
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(1380, 650)))
        if event.type == reload_timer:
            reload_list_in_game.append(reload.get_rect(topleft=(1380, 250)))
        if event.type == stone_timer:
            stone_list_in_game.append(stone.get_rect(topleft=(1380, 610)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_a and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 20, player_y + 130)))
            bullets_left -= 1

    clock.tick(10)
