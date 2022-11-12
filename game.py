import sys, pygame
from random import seed
from random import randint
from node import Node


testNode1 = Node(3)
testNode1.positionX = 400;
testNode1.positionY = 100;

testNode2 = Node(9)
testNode2.positionX = 300;
testNode2.positionY = 200;

testNode3 = Node(7)
testNode3.positionX = 500;
testNode3.positionY = 200;

testNode1.left = testNode2
testNode1.right = testNode3

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

def draw_vector(node1, node2, color = NODE_COLOR):
    vector = pygame.draw.polygon(
        screen,
        (color),
        [
            (node1.positionX + 1, node1.positionY - 1),
            (node1.positionX + 1, node1.positionY - 1),
            (node2.positionX - 1, node2.positionY + 1),
            (node2.positionX - 1, node2.positionY + 1)
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

    draw_node_to_screen(testNode1, random_color)
    draw_node_to_screen(testNode2, random_color)
    draw_node_to_screen(testNode3, random_color)
    draw_vector(testNode1, testNode2, random_color)
#    circle = pygame.draw.circle(screen, (random_color), (400, 100), RADIUS)
#    circle = pygame.draw.circle(screen, (NODE_COLOR), (500, 200), RADIUS)
#    circle = pygame.draw.circle(screen, (NODE_COLOR), (300, 200), RADIUS)
#    vector = pygame.draw.polygon(
#        screen,
#        (NODE_COLOR),
#        [
#            (400 + 1, 100 - 1),
#            (400 + 1, 100 - 1),
#            (500 - 1, 200 + 1),
#            (500 - 1, 200 + 1)
#        ],
#        3)
#    vector_2 = pygame.draw.polygon(
#        screen,
#        (NODE_COLOR),
#        [
#            (400 + 1, 100 - 1),
#            (400 + 1, 100 - 1),
#            (300 - 1, 200 + 1),
#            (300 - 1, 200 + 1)
#        ],
#        3)
    pygame.display.update()



