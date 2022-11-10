import sys, pygame
from random import seed
from random import randint

WIDTH = 800
HEIGHT = 600
RADIUS = 25
GRAY_BG = 42, 42, 42
NODE_COLOR = 120, 24, 24

screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))

# def initializeGameTree():
    # root = Node(10)
    # root.left = Node(4)
    #
    # ...
    #
    # TODO 

def draw_vector(node_1, node2, color = NODE_COLOR):
    vector = pygame.draw.polygon(
        screen,
        (color),
        [
            (400 + 1, 100 - 1),
            (400 + 1, 100 - 1),
            (500 - 1, 200 + 1),
            (500 - 1, 200 + 1)
        ],
        3)

def draw_node_to_screen(node, color = NODE_COLOR):    
    circle = pygame.draw.circle(screen, color, (node.positionX, node.positionY), RADIUS)
    #TODO



pygame.init()




while True:
    pygame.time.wait(400) # wait
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    random_color = randint(0, 255), randint(0, 255), randint(0, 255)

    screen.fill(GRAY_BG)

    circle = pygame.draw.circle(screen, (random_color), (400, 100), RADIUS)
    circle = pygame.draw.circle(screen, (NODE_COLOR), (500, 200), RADIUS)
    circle = pygame.draw.circle(screen, (NODE_COLOR), (300, 200), RADIUS)
    vector = pygame.draw.polygon(
        screen,
        (NODE_COLOR),
        [
            (400 + 1, 100 - 1),
            (400 + 1, 100 - 1),
            (500 - 1, 200 + 1),
            (500 - 1, 200 + 1)
        ],
        3)
    vector_2 = pygame.draw.polygon(
        screen,
        (NODE_COLOR),
        [
            (400 + 1, 100 - 1),
            (400 + 1, 100 - 1),
            (300 - 1, 200 + 1),
            (300 - 1, 200 + 1)
        ],
        3)
    pygame.display.update()



