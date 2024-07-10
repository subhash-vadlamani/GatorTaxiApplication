class RBTNodeClass:
    def __init__(self, ride, min_heap_node):
        """
        This class is used to create a node for the Red Black Tree.
        The Node for the Red Black Tree contains ride that it is
        associated to and also the corresponding min_heap_node location.
        :param ride:
        :param min_heap_node:
        """
        self.ride = ride
        self.parent = None  # parent node
        self.left = None  # left node
        self.right = None  # right node
        self.color = 1  # 1=red , 0 = black
        self.min_heap_node = min_heap_node
