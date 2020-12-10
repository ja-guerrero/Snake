import pygame
from pygame.math import Vector2
import pygame_menu
from colors import *
from sys import exit
from random import randint


Light_Green = (175, 215, 70)
Red = (196, 12, 33)
Green = (4, 59, 16)
WHITE = (255,255,255)


class Snake:
    def __init__(self):
        self.body = [Vector2(6,10), Vector2(5,10), Vector2(5,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * size)
            y_pos = int(block.y * size)
            block_rect = pygame.Rect(x_pos,y_pos, size, size)
            pygame.draw.rect(SCREEN, (14, 85, 199), block_rect )
    
    def move_snake(self):

        if self.new_block == True:
            tail = self.body[:]
            tail.insert(0,tail[0] + self.direction)
            self.body = tail[:]
            self.new_block = False
        else:
            tail = self.body[:-1]
            tail.insert(0,tail[0] + self.direction)
            self.body = tail[:]

    def add_block(self):
        self.new_block = True

    def body(self):
        lst = []
        for i in self.body:
            lst.append((i.x, i.y))
        return lst

         
snake_copy = Snake().body

class Fruit:
    def __init__(self):
        self.randomize()
        global snake_copy

    def draw(self):
        fruit_border = pygame.Rect(int(self.x * size), int(self.y *size ), size, size )
        SCREEN.blit(apple, fruit_border)

    def randomize(self):
        self.x = randint(0, cols-1)
        self.y = randint(0, rows-1)
        self.pos = Vector2(self.x, self.y)
        while self.pos in snake_copy[:]:
            self.x = randint(0, cols-1)
            self.y = randint(0, rows-1)
            self.pos = Vector2(self.x, self.y)


class main:
    def __init__(self):
        self.fruit = Fruit()
        self.snake = Snake()
    
    def update(self):
        self.snake.move_snake()
        self.game_logic()


    def draw_objects(self):
        self.fruit.draw()
        self.snake.draw_snake()

    def game_logic(self):
        self.snake.head = self.snake.body[0]
        self.fruit_pos = self.fruit.pos 


        #The border
        if self.snake.head.x > 19.75 or self.snake.head.x < 0 or self.snake.head.y > 19.75 or self.snake.head.y < 0:
            self.game_over()


        #Apple Collision and Snake expansion
        if self.snake.head == self.fruit_pos:
            self.fruit.randomize()
            self.snake.add_block()

        #Snake Collison with itself
        for pos in self.snake.body[1:]:
            if pos == self.snake.body[0]:
                self.game_over()


    def draw_grid(self):
        grid_color = (167, 209, 61)
        for row in range(rows):
            if row % 2 == 0:
                for col in range(cols):
                    if col % 2 == 0:
                        grid_rect = pygame.Rect(row*size, col*size, size, size)
                        pygame.draw.rect(SCREEN,grid_color, grid_rect)
            else:
                for col in range(cols):
                    if col % 2 !=0:
                        grid_rect = pygame.Rect(row*size, col*size, size, size)
                        pygame.draw.rect(SCREEN,grid_color, grid_rect)


    def game_over(self):
        pygame.quit()
        exit()
    


pygame.init() 
rows, cols = 20, 20
size = 40
SCREEN = pygame.display.set_mode((rows*size, cols*size))
pygame.display.set_caption("Snake")
SCREEN.fill(Light_Green)
running = True
clock = pygame.time.Clock()

apple = pygame.image.load('apple.png').convert_alpha()
apple = pygame.transform.scale(apple, (40,40))

snake = pygame.image.load


main = main()


def start_the_game():
    # Do the job here !
    
    rows, cols = 20, 20
    size = 40

    SCREEN.fill(Light_Green)
    running = True
    clock = pygame.time.Clock()

    apple = pygame.image.load('apple.png').convert_alpha()
    apple = pygame.transform.scale(apple, (50,50))

    snake = pygame.image.load

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    left = Vector2(-1, 0)
    right = Vector2(1, 0)
    up = Vector2(0, -1)
    down = Vector2(0, 1)
    excpetions = [left]


    while running:
        SCREEN.fill(Light_Green)
        main.draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                pygame.quit()
            if event.type == SCREEN_UPDATE:
                main.update()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if up in excpetions:
                        main.snake.direction
                    else:    
                        main.snake.direction = up
                        excpetions.pop()
                        excpetions.append(down)

                if event.key == pygame.K_DOWN:
                    if down in excpetions:
                        main.snake.direction
                    else:    
                        main.snake.direction = down
                        excpetions.pop()
                        excpetions.append(up)

                if event.key == pygame.K_LEFT:
                    if left in excpetions:
                        main.snake.direction
                    else:    
                        main.snake.direction = left
                        excpetions.pop()
                        excpetions.append(right)


                if event.key == pygame.K_RIGHT:
                    if right in excpetions:
                        main.snake.direction
                    else:    
                        main.snake.direction = right
                        excpetions.pop()
                        excpetions.append(left)

        main.draw_objects()
        pygame.display.update()
        clock.tick(120)




menu = pygame_menu.Menu(300, 400, 'Snake',theme=pygame_menu.themes.THEME_BLUE)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(SCREEN)
