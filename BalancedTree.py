#  File: BalancedTree.py
#  Description: Creates a balanced binary tree

#  Student Name: Woongchan Lee
#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim
#  Partner UT EID: DK25659

#  Course Name: CS 313E
#  Unique Number: 85575
#  Date Created: 08/05/2019
#  Date Last Modified: 08/05/2019


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    # Returns the height of the tree
    def get_height(self, aNode):
        if aNode == None:
            return 0
        height = 0
        nodes_level = Queue()
        nodes_level.enqueue(aNode)
        while not nodes_level.is_empty():
            new_level = Queue()
            # add all nodes from the next level into a Queue
            for i in range(nodes_level.size()):
                node = nodes_level.dequeue()
                if node != None:
                    if node.lchild != None:
                        new_level.enqueue(node.lchild)
                    if node.rchild != None:
                        new_level.enqueue(node.rchild)
            # set to check to next level
            nodes_level = new_level
            # increment height
            height += 1
        return height

    # return height of left subtree minus height of right subtree
    def get_balance_factor(self):
        return self.get_height(self.lchild) - self.get_height(self.rchild)

    def __str__(self):
        s = '(' + str(self.data) + ', ' + str(self.get_balance_factor()) + ')'
        return s


class Tree (object):
    def __init__(self):
        self.root = None
        self.size = 0

    # insert data into the tree
    def insert_node(self, data):
        new_node = Node(data)
        self.size += 1
        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node


    # Prints out all nodes at the given level
    def print_level(self, level):
        nodes_level = Queue()
        nodes_level.enqueue(self.root)
        if level <= 0:
            return None
        while level > 1:
            new_level = Queue()
            # add all nodes in the next level to a Queue
            for i in range(nodes_level.size()):
                node = nodes_level.dequeue()
                if node.lchild != None:
                    new_level.enqueue(node.lchild)
                if node.rchild != None:
                    new_level.enqueue(node.rchild)
            # go to next level
            nodes_level = new_level
            # decrement level counter
            level -= 1
        # print all nodes in level Queue
        for i in range(nodes_level.size()):
            print(str(nodes_level.dequeue()), end=' ')
        print()

    # Returns the height of the tree
    def get_height(self):
        height = -1
        nodes_level = Queue()
        nodes_level.enqueue(self.root)
        while not nodes_level.is_empty():
            new_level = Queue()
            # add all nodes from the next level into a Queue
            for i in range(nodes_level.size()):
                node = nodes_level.dequeue()
                if node.lchild != None:
                    new_level.enqueue(node.lchild)
                if node.rchild != None:
                    new_level.enqueue(node.rchild)
            # set to check to next level
            nodes_level = new_level
            # increment height
            height += 1
        return height

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        num = self.num_recur(self.root)
        return num

    def num_recur(self, aNode):
        if aNode == None:
            return 0
        num_left = self.num_recur(aNode.lchild)
        num_right = self.num_recur(aNode.rchild)
        return num_left + num_right + 1

    def get_balance_factor(self, aNode):
        return self.num_nodes(aNode.lchild) - self.num_nodes(aNode.rchild)


# input text file as a sorted integer list
def read_file(file_name):
    inf = open(file_name, 'r')
    list = inf.readline().split()
    if '\n' in list:
        list.pop()
    new_list = []
    for item in list:
        new_list.append(int(item))
    new_list.sort()
    return new_list


# return a list in an order such that it will create a balanced tree
def binary_sort(nums, l, r):
    # base case
    if r == l:
        return [nums[l]]
    if r < l:
        return []
    new_list = []
    mid_ind = (l + r) // 2
    # add the middle index element
    new_list.append(nums[mid_ind])
    # recurse for list items
    list_left = binary_sort(nums, l, mid_ind - 1)
    list_right = binary_sort(nums, mid_ind + 1, r)
    # add items into output list
    if len(list_left) == len(list_right):
        for i in range(len(list_left)):
            new_list.append(list_left[i])
            new_list.append(list_right[i])
    elif len(list_left) < len(list_right):
        j = 0
        for i in range(len(list_left)):
            new_list.append(list_left[i])
            new_list.append(list_right[i])
            j = i + 1
        for i in range(j, len(list_right)):
            new_list.append(list_right[i])
    elif len(list_left) > len(list_right):
        j = 0
        for i in range(len(list_right)):
            new_list.append(list_left[i])
            new_list.append(list_right[i])
            j = i + 1
        for i in range(j, len(list_left)):
            new_list.append(list_left[i])
    return new_list


def main():
    nums = read_file('tree.txt')
    nums = binary_sort(nums, 0, len(nums) - 1)
    tree = Tree()
    for num in nums:
        tree.insert_node(num)
    height = tree.get_height()
    for level_num in range(1, height + 2):
        tree.print_level(level_num)


main()

