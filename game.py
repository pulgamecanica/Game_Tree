import sys, pygame, math
from random import seed
from random import randint
from node import Node

GRAY_BG = 192, 192, 192     # Color
NODE_COLOR = 105, 105, 105  # Color
SQUARE_COLOR = 79, 74, 75   # Color
TEXT_COLOR = 230, 230, 230  # Color
BLUE = 57, 69, 78
RED = 161, 49, 42

TREE_WIDTH = 800                    # Width area that the Tree Covers
TREE_HEIGHT = 300                   # Height area that the Tree Covers
WINDOW_WIDTH = TREE_WIDTH + 100     # Width area that the Window Covers
WINDOW_HEIGHT = TREE_HEIGHT + 100   # Height area that the Window Covers

MAX_DEPTH = 5                                   # Depth of the Game Tree
ALGO_SPEED = 300
RADIUS = (TREE_WIDTH * 0.75) / (2**MAX_DEPTH)   # Radius of the node

# Set the screen configuration
screen = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

def setNode(parent, right_position_count = 0):
    if (parent.height() >= MAX_DEPTH - 1):
        return
    parent.left = Node()
    parent.left.parent = parent
    parent.left.positionX = parent.positionX - (TREE_WIDTH / 2 ** parent.left.height() / 2)
    parent.left.positionY = parent.left.height() * (TREE_HEIGHT / (MAX_DEPTH - 1))
    setNode(parent.left, right_position_count)
    parent.right = Node()
    parent.right.parent = parent
    parent.right.positionX = parent.positionX + (TREE_WIDTH / 2 ** parent.right.height() / 2)
    parent.right.positionY = parent.right.height() * (TREE_HEIGHT / (MAX_DEPTH - 1))
    setNode(parent.right, right_position_count + 1)

def initializeGameTree(depth = MAX_DEPTH):
    root = Node()
    root.positionY = RADIUS
    root.positionX = TREE_WIDTH / 2
    setNode(root)
    return (root)

def draw_vector_to_screen(node1, node2, color = NODE_COLOR):
    vector = pygame.draw.polygon(
        screen,
        (color),
        [
            (node1.positionX, node1.positionY),
            (node1.positionX, node1.positionY),
            (node2.positionX, node2.positionY),
            (node2.positionX, node2.positionY)
        ],
        2)

def draw_node_to_screen(node, color = NODE_COLOR):
    circle = pygame.draw.circle(screen, color, (node.positionX, node.positionY), RADIUS)
    if node.data:
        font = pygame.font.Font('Sono-VariableFont.ttf', 20)
        text = font.render(str(node.data), True, (TEXT_COLOR))
        textRect = text.get_rect()
        textRect.center = (node.positionX, node.positionY)
        screen.blit(text, textRect)

def draw_tree_to_screen(node, color = NODE_COLOR):
    if node.left:
       draw_tree_to_screen(node.left, color)
    if node.right:
        draw_tree_to_screen(node.right, color)
    draw_node_to_screen(node, color)
    if node.parent:
        draw_vector_to_screen(node.parent, node, color)
    pygame.display.update()


def print_tree(node):
    if (node):
        print_node_info(node)
        if node.left:
            print("\nLeft:")
            print_tree(node.left)
        if node.right:
            print("\nRight:")
            print_tree(node.right)

def print_node_info(node):
    print("Node: ", node)
    print("\tData:", node.data, "[", node.positionX, ",", node.positionY, "]")
    if node.parent:
        print("\tParent:", node.parent)
    else:
        print("\tNo parent")
    if node.right:
        print("\tRight Child:", node.right)
    else:
        print("\tThere is no right child of the node")
    if node.left:
        print("\tLeft Child:", node.left)
    else:
        print("\tThere is no left child of the node")

def set_up_numbers(node, array):
    if node.left:
        set_up_numbers(node.left, array)
    if node.right:
        set_up_numbers(node.right, array)
    if not node.left and len(array):
        node.data = array.pop()

def draw_list_bottom(array):
    array.reverse()
    font = pygame.font.Font('Sono-VariableFont.ttf', 20)
    square_center_height = ((WINDOW_HEIGHT - TREE_HEIGHT) / 2) + TREE_HEIGHT + RADIUS
    list_len = len(array)
    square_len = TREE_WIDTH / list_len
    for i, elem in enumerate(array):
        rect = pygame.Rect(0, 0, ((WINDOW_HEIGHT - TREE_HEIGHT) / 2) * 0.75, ((WINDOW_HEIGHT - TREE_HEIGHT) / 2) * 0.75)
        rect.center = ((square_len * (i + 1)) - (square_len / 2), square_center_height)
        pygame.draw.rect(screen, (SQUARE_COLOR), rect)
        text = font.render(str(elem), True, (TEXT_COLOR))
        textRect = text.get_rect()
        textRect.center = ((square_len * (i + 1)) - (square_len / 2), square_center_height)
        screen.blit(text, textRect)
        
def draw_right_side_bar():
    font = pygame.font.Font('Sono-VariableFont.ttf', 20)
    for i in range(0, MAX_DEPTH):
        if (i % 2):
            text = font.render("MIN", True, (SQUARE_COLOR))
        else:
            text = font.render("MAX", True, (SQUARE_COLOR))
        textRect = text.get_rect()
        textRect.center = (((WINDOW_WIDTH - TREE_WIDTH) / 2) + TREE_WIDTH, (i * (TREE_HEIGHT / (MAX_DEPTH - 1)) + RADIUS * (i == 0)))
        screen.blit(text, textRect)


def draw_mini_max(node, is_max, depth = MAX_DEPTH):
    draw_node_to_screen(node, BLUE)
    pygame.time.wait(ALGO_SPEED)
    pygame.display.update()
    if depth == 1:
        return
    listChildren = [node.left, node.right]
    if (is_max):
        bestValue = -math.inf
        bestPath = None
        for child in listChildren:
            draw_mini_max(child, not is_max, depth - 1)
            if child.data and child.data > bestValue:
                bestValue = child.data
                bestPath = child
    else:
        bestValue = +math.inf
        bestPath = None
        for child in listChildren:
            draw_mini_max(child, not is_max, depth - 1)
            if child.data and child.data < bestValue:
                bestValue = child.data
                bestPath = child
    node.data = bestValue
    node.path = bestPath
    pygame.time.wait(ALGO_SPEED)
    if (node.data == node.left.data):
        draw_node_to_screen(node.left, RED)
    else:
        draw_node_to_screen(node.right, RED)
    draw_node_to_screen(node, BLUE)
    pygame.display.update()

def print_best_path(node):
    if not node:
        return
    if not node.height():
        print ("*** min_max: Best Path (starting at root) ***")
    if node.path:
        if node.path == node.left:
            print("<- [LEFT]")
        else:
            print("-> [RIGHT]")
        print_best_path(node.path)

pygame.init()
root = initializeGameTree()
array = [10, 5, 7, 11, 12, 8, 9, 8, 5, 12, 11, 12, 9, 8, 7, 10]
array.reverse()
set_up_numbers(root, array.copy())
# print_tree(root)

screen.fill(GRAY_BG)
draw_tree_to_screen(root)
draw_list_bottom(array.copy())
draw_right_side_bar()
pygame.display.update()
draw_mini_max(root, True)
print_best_path(root)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.update()
