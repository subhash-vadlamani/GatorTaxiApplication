from rbt_node import RBTNodeClass

class RedBlackTree:
    def __init__(self):
        """
        Creating the root of the Red Black Tree. Since we know that the root of the red black tree
        is always a black node, we color it black.
        """
        self.null_node = RBTNodeClass(None, None)
        self.null_node.left = None
        self.null_node.right = None
        self.null_node.color = 0
        self.root = self.null_node

    # This method fetches the ride with the rideNumber same as that of 'key'
    def get_ride_with_key(self, key):
        temp = self.root

        #searching the tree to find the node with rideNumber equal to the key
        # This is the same method used in the regular binary search tree.
        while temp != self.null_node:
            if temp.ride.rideNumber == key:
                return temp
            if temp.ride.rideNumber < key:
                temp = temp.right
            else:
                temp = temp.left

        return None

        # Balancing the tree after deletion

    """
        Method to balance the red black tree after the node deletion
        Input is the node that is deleted
    """

    def balance_rbt_after_delete(self, node):

        # Check if the color of the node is black and it is not the rood node
        while node != self.root and node.color == 0:
            if node == node.parent.right:
                parent_sibling = node.parent.left
                # Check if the sibling of the node is red. if it is, rotate the parent node in the opposite side of the sibling
                if parent_sibling.color != 0:
                    node.parent.color = 1
                    parent_sibling.color = 0
                    self.right_rotation(node.parent)
                    parent_sibling = node.parent.left

                # If any children of the parent's siblings is black.
                if parent_sibling.right.color == 0 and parent_sibling.left.color == 0:
                    parent_sibling.color = 1
                    node = node.parent
                else:
                    # If the color of the left child of the parent's siblign is black
                    if parent_sibling.left.color != 1:
                        # Change the color of the right child of the parent's sibling to black
                        parent_sibling.right.color = 0
                        # Change the color of the parent's sibling to red
                        parent_sibling.color = 1
                        # Perform a left rotation about the parent's sibling that we are considering
                        self.left_rotation(parent_sibling)

                        parent_sibling = node.parent.left

                    # Change the color of the parent's sibling to the same color as that of the current node's parent
                    parent_sibling.color = node.parent.color
                    node.parent.color = 0
                    parent_sibling.left.color = 0
                    self.right_rotation(node.parent)
                    node = self.root
            # If the sibling is black, the method checks if both children of the sibling are also black.
            # If they are, it colors the sibling red and moves up to the parent node.
            else:
                parent_sibling = node.parent.right
                # If the color of the parent's siblign is red
                if parent_sibling.color != 0:
                    node.parent.color = 1
                    parent_sibling.color = 0
                    self.left_rotation(node.parent)
                    parent_sibling = node.parent.right


                # If the color of the parent's siblings children are both black

                if parent_sibling.right.color == 0 and parent_sibling.left.color == 0:
                    parent_sibling.color = 1
                    node = node.parent
                else:
                    if parent_sibling.right.color != 1:
                        parent_sibling.left.color = 0
                        parent_sibling.color = 1
                        self.right_rotation(parent_sibling)
                        parent_sibling = node.parent.right

                    parent_sibling.color = node.parent.color
                    node.parent.color = 0
                    parent_sibling.right.color = 0
                    self.left_rotation(node.parent)
                    node = self.root

        #Finally, the method sets the color of the node to black to ensure that the properties of the red-black tree are maintained.

        node.color = 0


    def rbt_switch(self, node, child_node):
        # If the parent of the node is None, the node is the root, so set the root to the child node
        if node.parent is None:
            self.root = child_node
        # If the node is the right child of its parent, set the right child of the parent to the child node
        elif node == node.parent.right:
            node.parent.right = child_node
        # Otherwise, the node is the left child of its parent, so set the left child of the parent to the child node
        else:
            node.parent.left = child_node
        # Set the parent of the child node to the parent of the node
        child_node.parent = node.parent


    # Method to delete the node with a specific key from the red black tree.

    # The method searches the tree for the node with the given key and if found, stores it in the delete_node variable.


    def delete_node_method(self, node, key):
        deleted_node = self.null_node
        #The method then checks if the deleted_node has any children, and based on that, decides which node to replace it with.
        # The method then performs the replacement using the __rb_transplant method, which replaces the deleted_node with the x node.


        while node != self.null_node:
            if node.ride.rideNumber == key:
                deleted_node = node
            if node.ride.rideNumber >= key:
                node = node.left
            else:
                node = node.right

        if deleted_node == self.null_node:
            return
        heap_node = deleted_node.min_heap_node
        y = deleted_node
        y_original_color = y.color
        if deleted_node.left == self.null_node:
            x = deleted_node.right
            self.rbt_switch(deleted_node, deleted_node.right)
        elif (deleted_node.right == self.null_node):
            x = deleted_node.left
            self.rbt_switch(deleted_node, deleted_node.left)
        else:
            y = self.minimum(deleted_node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == deleted_node:
                x.parent = y
            else:
                self.rbt_switch(y, y.right)
                y.right = deleted_node.right
                y.right.parent = y

            self.rbt_switch(deleted_node, y)
            y.left = deleted_node.left
            y.left.parent = y
            y.color = deleted_node.color
        if y_original_color == 0:
            self.balance_rbt_after_delete(x)

        return heap_node

    def get_rides_in_range(self, low, high):
        res = []
        self.find_rides_in_range(self.root, low, high, res)
        return res

    def minimum(self, node):
        while node.left != self.null_node:
            node = node.left
        return node

    def balance_rbt_after_insert(self, curr_node):

        """
        This method is responsbile for balancing the red black trees and making sure that
        the properties of the red black trees hold after the insertion.
        :param curr_node:
        :return:
        """
        while curr_node.parent.color == 1:
            # If the parent of the current node is the left child of it's parent
            if curr_node.parent == curr_node.parent.parent.left:
                # Get the sibling of the parent
                parent_sibling = curr_node.parent.parent.right

                # If the color of the sibling is black
                if parent_sibling.color == 0:
                    if curr_node == curr_node.parent.right:
                        curr_node = curr_node.parent
                        self.left_rotation(curr_node)
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    self.right_rotation(curr_node.parent.parent)
                else:
                    parent_sibling.color = 0
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    curr_node = curr_node.parent.parent

            # If the parent of the current node is the right child of it's parent
            else:
                parent_sibling = curr_node.parent.parent.left
                if parent_sibling.color == 0:
                    if curr_node == curr_node.parent.left:
                        curr_node = curr_node.parent
                        self.right_rotation(curr_node)
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    self.left_rotation(curr_node.parent.parent)
                else:
                    parent_sibling.color = 0
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    curr_node = curr_node.parent.parent

            if curr_node == self.root:
                break
        # Making the color of the root black
        self.root.color = 0

    def find_rides_in_range(self, node, low, high, res):
        if node == self.null_node:
            return

        if low < node.ride.rideNumber:
            self.find_rides_in_range(node.left, low, high, res)
        if low <= node.ride.rideNumber <= high:
            res.append(node.ride)
        self.find_rides_in_range(node.right, low, high, res)


    # Method to find the rides that are in the price range of 'low' to 'high'




    def left_rotation(self, x):
        """
        Method that is responsible for making the right child('b') of the node 'a' as the parent of 'a' and making
        'a' the left child of 'b'.
        :param x:
        :return:
        """
        y = x.right
        x.right = y.left
        if y.left != self.null_node:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotation(self, x):
        """
        Method that is responsible for making the left child('b') of the node 'a' as the parent of 'a' and
        making the node 'a' as the right child of node 'b'.
        :param x:
        :return:
        """
        y = x.left
        x.left = y.right
        if y.right != self.null_node:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Method to insert the element into the red black tree
    def insert(self, ride, min_heap):
        node = RBTNodeClass(ride, min_heap)
        node.parent = None
        node.left = self.null_node
        node.right = self.null_node
        node.color = 1
        insertion_node = None
        temp_node = self.root

        # Elements in the Red Black tree are arranged according to the ride number value
        # That is, the key for the elements to be arranged like that is the ride number.
        while temp_node != self.null_node:
            insertion_node = temp_node
            if node.ride.rideNumber < temp_node.ride.rideNumber:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        node.parent = insertion_node
        if insertion_node is None:
            self.root = node
        elif node.ride.rideNumber > insertion_node.ride.rideNumber:
            insertion_node.right = node
        else:
            insertion_node.left = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.balance_rbt_after_insert(node)

    def delete_node(self, rideNumber):
        return self.delete_node_method(self.root, rideNumber)
