import pygame

font_name = pygame.font.match_font('arial')



def draw_text(surf, text, size, x, y):
    """написание заданного текста на экране игры"""
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, 'WHITE')
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


