class Node:
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.path = None
        self.positionX = None # Find width --> count all the nodes of the lvl, divide them by the total with and multipy by the position of the current width 
        self.positionY = None # This is going to be the lvl 
        self.data = data

    def printNode(self):
        print(self.data)

    # Print the node to the screen, usign positionX and positionY
    def printToScreen(self, screen_surface):
        # TODO

