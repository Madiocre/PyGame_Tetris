#!/usr/bin/env python3
""" Settings file for Game data and such """
import pygame


#Gamesize
COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

#Side bar size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRAC = 0.7
SCORE_HEIGHT_FRAC = 1 - PREV_HEIGHT_FRAC

#Window
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + 3 * PADDING
WIDNOW_HEIGHT = GAME_HEIGHT + 3 * PADDING

#Game behavior
UPDATE_START_SPEED = 800
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2(COLUMNS // 2 , -1)

#Colors
YELLOW = '#F1E60D'
RED = '#E51B20'
BLUE = '#204B8B'
GREEN = '#65B32E'
PURPLE = '#7B217F'
CYAN = '#6CC6D9'
ORANGE = '#FO7E14'
GREY = '#1C1C1C'
LINE_CLR = '#FFFFFF'

#Tetrominis
TETROMIS = {
        'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': CYAN},
        'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': PURPLE},
        'O': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': YELLOW},
        'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': GREEN},
        'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': RED},
        'J': {'shape': [(0,0), (0,-1), (1,0), (-1,1)], 'color': BLUE},
        'L': {'shape': [(0,0), (0,-1), (1,0), (1,1)], 'color': ORANGE}
}

SCORE_DATA = {1: 40, 2: 100, 3: 400, 4: 1200}
