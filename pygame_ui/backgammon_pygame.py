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
def draw_point(screen, x, y_base, board_idx, board, is_top, hitmap):
    """Dibuja un triángulo y las fichas"""
    visual_pos = board_idx + 1
    color = BROWN_DARK if ((visual_pos - 1) // 6 + visual_pos) % 2 == 0 else BROWN_LIGHT
    if is_top:
        points = [(x, y_base),
                  (x + POINT_WIDTH, y_base),
                  (x + POINT_WIDTH//2, y_base + POINT_HEIGHT)]
    else:
        points = [(x, y_base + POINT_HEIGHT),
                  (x + POINT_WIDTH, y_base + POINT_HEIGHT),
                  (x + POINT_WIDTH//2, y_base)]
    pygame.draw.polygon(screen, color, points)
    pygame.draw.polygon(screen, BLACK, points, 2)
    hitmap[board_idx] = pygame.Rect(x, y_base if not is_top else y_base, POINT_WIDTH, POINT_HEIGHT)
    point = board.get_point(board_idx + 1)  # get_point usa 1-24
    if point and point[1] > 0:
        checker_color = WHITE if point[0] == "white" else BLACK
        border_color = BLACK if point[0] == "white" else WHITE
        count = point[1]
        for i in range(count):
            cx = x + POINT_WIDTH // 2
            if is_top:
                cy = y_base + 20 + i * (CHECKER_RADIUS * 2 + 5)
            else:
                cy = y_base + POINT_HEIGHT - 20 - i * (CHECKER_RADIUS * 2 + 5)
            
            pygame.draw.circle(screen, checker_color, (cx, cy), CHECKER_RADIUS)
            pygame.draw.circle(screen, border_color, (cx, cy), CHECKER_RADIUS, 2)
def draw_info(screen, game, font):
    """Dibuja información del juego en el lado derecho"""
    info_x = MARGIN + 12 * POINT_WIDTH + 150
    small_font = pygame.font.SysFont(None, 18)
    player = game.get_current_player()
    info = f"Turno: {player.get_name()}"
    text = small_font.render(info, True, BLACK)
    screen.blit(text, (info_x, HEIGHT // 2 - 60))
    color_text = f"({player.get_color()})"
    text = small_font.render(color_text, True, BLACK)
    screen.blit(text, (info_x, HEIGHT // 2 - 40))
    moves = game.get_remaining_moves()
    if moves:
        dice_text = f"Dados: {moves}"
        text = small_font.render(dice_text, True, BLACK)
        screen.blit(text, (info_x, HEIGHT // 2 - 15))
        board = game.__board__
        color = player.get_color()
        if board.has_checkers_on_bar(color):
            tiny_font = pygame.font.SysFont(None, 16)
            warn1 = tiny_font.render("¡FICHA EN", True, RED)
            warn2 = tiny_font.render("EL BAR!", True, RED)
            warn3 = tiny_font.render("Debes", True, RED)
            warn4 = tiny_font.render("sacarla", True, RED)
            warn5 = tiny_font.render("primero", True, RED)
            screen.blit(warn1, (info_x, HEIGHT // 2 + 15))
            screen.blit(warn2, (info_x, HEIGHT // 2 + 30))
            screen.blit(warn3, (info_x, HEIGHT // 2 + 45))
            screen.blit(warn4, (info_x, HEIGHT // 2 + 60))
            screen.blit(warn5, (info_x, HEIGHT // 2 + 75))
    else:
        text = small_font.render("Presiona", True, RED)
        screen.blit(text, (info_x, HEIGHT // 2 - 10))
        text2 = small_font.render("ESPACIO", True, RED)
        screen.blit(text2, (info_x, HEIGHT // 2 + 5))
        text3 = small_font.render("para tirar", True, RED)
        screen.blit(text3, (info_x, HEIGHT // 2 + 20))