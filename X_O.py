import pygame
import sys


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[None] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= cell_x < self.width and 0 <= cell_y < self.height:
            return cell_x, cell_y
        return None, None

    def place_marker(self, cell_x, cell_y, player):
        if self.board[cell_y][cell_x] is None:
            self.board[cell_y][cell_x] = player

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.cell_size + self.left, y * self.cell_size + self.top,
                                   self.cell_size, self.cell_size)
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)
                if self.board[y][x] == 'X':
                    self.draw_cross(screen, x, y)
                elif self.board[y][x] == 'O':
                    self.draw_circle(screen, x, y)

    def draw_cross(self, screen, x, y):
        offset = 2
        start_pos1 = (x * self.cell_size + self.left + offset, y * self.cell_size + self.top + offset)
        end_pos1 = (x * self.cell_size + self.left + self.cell_size - offset,
                    y * self.cell_size + self.top + self.cell_size - offset)
        start_pos2 = (x * self.cell_size + self.left + self.cell_size - offset, y * self.cell_size + self.top + offset)
        end_pos2 = (x * self.cell_size + self.left + offset, y * self.cell_size + self.top + self.cell_size - offset)
        pygame.draw.line(screen, (0, 0, 255), start_pos1, end_pos1, 2)
        pygame.draw.line(screen, (0, 0, 255), start_pos2, end_pos2, 2)

    def draw_circle(self, screen, x, y):
        offset = 2
        center = (
            x * self.cell_size + self.left + self.cell_size // 2, y * self.cell_size + self.top + self.cell_size // 2)
        radius = self.cell_size // 2 - offset
        pygame.draw.circle(screen, (255, 0, 0), center, radius, 2)


pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

board = Board(10, 7)  # Поле 3x3
board.set_view(100, 100, 50)

current_player = 'X'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cell_x, cell_y = board.get_cell(event.pos)
            if cell_x is not None and cell_y is not None:
                board.place_marker(cell_x, cell_y, current_player)
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'

    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
