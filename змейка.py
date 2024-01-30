import pygame
import sys
import random
pygame.init()

size_cell = 25
h_color = (0, 171, 111)
f_color = (77, 222, 0)
zm_color = (50, 144, 0)
wh = (218, 230, 245)
blue = (169, 197, 235)
red = (236, 0, 51)
ots = 1
size = [435, 520]
blocks = 15
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
time = pygame.time.Clock()
c = pygame.font.SysFont('courier', 40)


class SnPos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ins(self):
        if not 0 <= self.x <= 14 or not 0 <= self.y <= 14:
            return False
        return True

    def __eq__(self, other):
        return isinstance(other, SnPos) and self.x == other.x and self.y == other.y


def get_block():
    x, y = random.randint(0, blocks - 1), random.randint(0, blocks - 1)
    e_block = SnPos(x, y)
    while e_block in sn_pos:
        e_block.x = random.randint(0, blocks - 1)
        e_block.y = random.randint(0, blocks - 1)
    return e_block


def db(color, row, column):
    pygame.draw.rect(screen, color, (size_cell + column * size_cell + ots * (column + 1),
                                     70 + size_cell + row * size_cell + ots * (row + 1), size_cell, size_cell))


sn_pos = [SnPos(8, 6), SnPos(8, 7), SnPos(8, 8)]
eat = get_block()
f_row = 0
f_column = 1
count = 0
v = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and f_column != 0:
                f_row = -1
                f_column = 0
            elif event.key == pygame.K_DOWN and f_column != 0:
                f_row = 1
                f_column = 0
            elif event.key == pygame.K_LEFT and f_row != 0:
                f_row = 0
                f_column = -1
            elif event.key == pygame.K_RIGHT and f_row != 0:
                f_row = 0
                f_column = 1

    screen.fill(f_color)
    pygame.draw.rect(screen, h_color, [0, 0, size[0], 70])

    show_count = c.render(f'Count: {count}', 0, wh)
    screen.blit(show_count, (size_cell, size_cell))

    for row in range(blocks):
        for column in range(blocks):
            if (row + column) % 2 == 0:
                color = blue
            else:
                color = wh
            db(color, row, column)

    head_snake = sn_pos[-1]
    if not head_snake.ins():
        print(count)
        pygame.quit()
        sys.exit()

    db(red, eat.x, eat.y)
    for block in sn_pos:
        db(zm_color, block.x, block.y)

    if eat == head_snake:
        count += 1
        if count % 5 == 0:
            v += 1
        sn_pos.append(eat)
        eat = get_block()

    nhead_snake = SnPos(head_snake.x + f_row, head_snake.y + f_column)
    sn_pos.append(nhead_snake)
    sn_pos.pop(0)

    pygame.display.flip()
    time.tick(2 + v)
