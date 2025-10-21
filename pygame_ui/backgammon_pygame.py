import pygame
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.backgammon_game.backgammongame import BackgammonGam
"""constantes"""
WIDTH, HEIGHT = 1000, 700
MARGIN = 40
POINT_WIDTH = 60
POINT_HEIGHT = 200
CHECKER_RADIUS = 25
"""colores"""
BG = (210, 180, 140)
BROWN_DARK = (139, 69, 19)
BROWN_LIGHT = (205, 133, 63)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
RED = (220, 20, 60)
def render_board(screen, game, font):
    """Dibuja el tablero y retorna hitmap para clicks"""
    screen.fill(BG)
    board = game.__board__
    hitmap = {}
    for visual_idx in range(12):
        board_idx = 11 - visual_idx
        x = MARGIN + visual_idx * POINT_WIDTH
        if visual_idx >= 6:
            x += 40
        y_base = HEIGHT - MARGIN - POINT_HEIGHT
        draw_point(screen, x, y_base, board_idx, board, False, hitmap)
        num_text_bottom = font.render(str(12 - visual_idx), True, BLACK)
        screen.blit(num_text_bottom, (x + POINT_WIDTH//2 - 10, HEIGHT - MARGIN + 5))
    for visual_idx in range(12):
        board_idx = 12 + visual_idx
        x = MARGIN + visual_idx * POINT_WIDTH
        if visual_idx >= 6:
            x += 40
        draw_point(screen, x, MARGIN, board_idx, board, True, hitmap)
        num_text = font.render(str(13 + visual_idx), True, BLACK)
        screen.blit(num_text, (x + POINT_WIDTH//2 - 10, MARGIN - 25))
    bar_x = MARGIN + 6 * POINT_WIDTH
    pygame.draw.rect(screen, BROWN_DARK, (bar_x, MARGIN, 40, HEIGHT - 2*MARGIN))
    white_bar = board.get_bar_count("white")
    black_bar = board.get_bar_count("black")
    if white_bar > 0:
        for i in range(white_bar):
            cx = bar_x + 20
            cy = HEIGHT - MARGIN - 30 - i * (CHECKER_RADIUS * 2 + 3)
            pygame.draw.circle(screen, WHITE, (cx, cy), CHECKER_RADIUS)
            pygame.draw.circle(screen, BLACK, (cx, cy), CHECKER_RADIUS, 2)
        hitmap[24] = pygame.Rect(bar_x, HEIGHT // 2, 40, HEIGHT // 2 - MARGIN)
    if black_bar > 0:
        for i in range(black_bar):
            cx = bar_x + 20
            cy = MARGIN + 30 + i * (CHECKER_RADIUS * 2 + 3)
            pygame.draw.circle(screen, BLACK, (cx, cy), CHECKER_RADIUS)
            pygame.draw.circle(screen, WHITE, (cx, cy), CHECKER_RADIUS, 2)
        hitmap[24] = pygame.Rect(bar_x, MARGIN, 40, HEIGHT // 2 - MARGIN)
    bear_off_x = MARGIN + 12 * POINT_WIDTH + 40
    bear_off_width = 100
    pygame.draw.rect(screen, (100, 100, 100), (bear_off_x, HEIGHT // 2, bear_off_width, HEIGHT // 2 - MARGIN), 2)
    bear_off_text = font.render("OFF", True, BLACK)
    screen.blit(bear_off_text, (bear_off_x + 35, HEIGHT - MARGIN - 20))
    white_off = board.off["white"]
    if white_off > 0:
        off_text = font.render(f"W:{white_off}", True, WHITE)
        screen.blit(off_text, (bear_off_x + 35, HEIGHT // 2 + 10))
    hitmap[25] = pygame.Rect(bear_off_x, HEIGHT // 2, bear_off_width, HEIGHT // 2 - MARGIN)
    pygame.draw.rect(screen, (100, 100, 100), (bear_off_x, MARGIN, bear_off_width, HEIGHT // 2 - MARGIN), 2)
    screen.blit(bear_off_text, (bear_off_x + 35, MARGIN + 5))
    black_off = board.off["black"]
    if black_off > 0:
        off_text = font.render(f"B:{black_off}", True, BLACK)
        screen.blit(off_text, (bear_off_x + 35, HEIGHT // 2 - 30))
    hitmap[26] = pygame.Rect(bear_off_x, MARGIN, bear_off_width, HEIGHT // 2 - MARGIN)
    draw_info(screen, game, font)
    return hitmap
