import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
        # If inserting we must already have a tree/root
        # If value is less than self.value then self.left = value if empty
            # Otherwise keep going
        # if greater than or equal to, then go right and make a node if empty
            # Otherwise keep going

    def insert(self, value):
        checking = True
        current_node = self
        while checking is True:
            if current_node.value == value:
                return
            elif value > current_node.value:
                if current_node.right is None:
                    current_node.right = BinarySearchTree(value)
                    checking = False
                else:
                    current_node = current_node.right
            elif value < current_node.value:
                if current_node.left is None:
                    current_node.left = BinarySearchTree(value)
                    checking = False 
                else:
                    current_node = current_node.left
        
                    


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # is value >= to self.value ? move right : move left, repeat until value = self.value
        # return true unless reached None
        current_node = self
        searching = True
        while searching is True:
            if target == current_node.value:
                searching = False
                return True
            elif target > current_node.value:
                if current_node.right == None:
                    searching = False
                    return False
                elif target == current_node.value:
                    searching = False
                    return True
                else:
                    current_node = current_node.right
            elif target < current_node.value:
                if current_node.left == None:
                    searching = False
                    return False
                elif current_node.left == target:
                    searching = False
                    return True
                else:
                    current_node = current_node.left
            

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right until None then return self.value
        checking = True
        current_node = self
        while checking is True:
            if current_node.right == None:
                return current_node.value
            else:
                current_node = current_node.right


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    
    # def for_each(self, cb):
    #     def iter(node):
    #         if node:
    #             node.value = cb(node.value)
    #             iter(node.left)
    #             iter(node.right)
    #     iter(self)

    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)



    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
