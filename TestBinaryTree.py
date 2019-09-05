#  File: TestBinaryTree.py
#  Description: Models Binary Tree class with methods that calculate height, levels, and number of nodes

#  Student Name: Woongchan Lee
#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim
#  Partner UT EID: DK25659

#  Course Name: CS 313E
#  Unique Number: 85575
#  Date Created: 08/01/2019
#  Date Last Modified: 08/01/2019


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

    def __str__(self):
        s = str(self.data)
        return s


class Tree (object):
    def __init__(self):
        self.root = None
        self.size = 0

    # insert data into the tree
    def insert_node (self, data):
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

    # search for a node with given data
    def search_node(self, data):
        current = self.root
        while (current != None) and (current.data != data):
            if (data < current.data):
                current = current.lchild
            else:
                current = current.rchild
        return current

    # inorder traversal - left, center, right
    def in_order(self, aNode):
        if (aNode != None):
            self.in_order(aNode.lchild)
            print(aNode.data)
            self.in_order(aNode.rchild)

    # preorder traversal - center, left, right
    def pre_order(self, aNode):
        if (aNode != None):
            print(aNode.data)
            self.pre_order(aNode.lchild)
            self.pre_order(aNode.rchild)

    # postorder traversal - left, right, center
    def post_order(self, aNode):
        if (aNode != None):
            self.post_order(aNode.lchild)
            self.post_order(aNode.rchild)
            print(aNode.data)

    # Find the node with the smallest value
    def min_node(self):
        current = self.root
        parent = self.root
        while (current != None):
            parent = current
            current = current.lchild
        return parent

    # Find the node with the largest value
    def max_node(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.rchild
        return parent

    # delete a node with a given key
    def delete_node(self, data):
        delete_node = self.root
        parent = self.root
        is_left = False

        # if empty tree
        if (delete_node == None):
            return None

        # find the node containing the data
        while (delete_node != None) and (delete_node.data != data):
            parent = delete_node
            if (data < delete_node.data):
                delete_node = delete_node.lchild
                is_left = True
            else:
                delete_node = delete_node.rchild
                is_left = False

        # if node not found
        if (delete_node == None):
            return None

        # check if the delete node is a leaf node
        if (delete_node.lchild == None) and (delete_node.rchild == None):
            if (delete_node == self.root):
                self.root = None
            elif (is_left):
                parent.lchild = None
            else:
                parent.rchild = None

        # check if the delete node is a node with only a left child
        elif (delete_node.rchild == None):
            if (delete_node == self.root):
                self.root = delete_node.lchild
            elif (is_left):
                parent.lchild = delete_node.lchild
            else:
                parent.rchild = delete_node.lchild

        # Delete node is a node with only right child
        elif (delete_node.lchild == None):
            if (delete_node == self.root):
                self.root = delete_node.rchild
            elif (is_left):
                parent.lchild = delete_node.rchild
            else:
                parent.rchild = delete_node.rchild

        # Delete node is a node with both left and right child
        else:
            # Find delete node's successor and successor's parent nodes
            successor = delete_node.rchild
            successor_parent = delete_node

            while (successor.lchild != None):
                successor_parent = successor
                successor = successor.lchild

            # Successor node right child of delete node
            if (delete_node == self.root):
                self.root = successor
            elif (is_left):
                parent.lchild = successor
            else:
                parent.rchild = successor

            # Connect delete node's left child to be successor's left child
            successor.lchild = delete_node.lchild

            # Successor node left descendant of delete node
            if (successor != delete_node.rchild):
                successor_parent.lchild = successor.rchild
                successor.rchild = delete_node.rchild
        self.size -= 1
        return delete_node

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        # create two lists of entire tree through BFS traversal
        o_lst = self.BFS_list()
        p_lst = pNode.BFS_list()
        if len(o_lst) != len(p_lst):
            return False
        # compare list items
        for i in range(len(o_lst)):
            if o_lst[i] != p_lst[i]:
                return False
        return True

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

    # returns a list of entire tree in breadth first search order
    def BFS_list(self):
        lst = []
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            item = q.dequeue()
            lst.append(int(str(item)))
            if item.lchild != None:
                q.enqueue(item.lchild)
            if item.rchild != None:
                q.enqueue(item.rchild)
        return lst


def main():
    # Create three trees - two are the same and the third is different
    tree1 = Tree()
    tree1.insert_node(14)
    tree1.insert_node(19)
    tree1.insert_node(22)
    tree1.insert_node(17)
    tree1.insert_node(21)
    tree1.insert_node(10)
    tree1.insert_node(8)
    tree1.insert_node(12)

    tree2 = Tree()
    tree2.insert_node(14)
    tree2.insert_node(19)
    tree2.insert_node(22)
    tree2.insert_node(17)
    tree2.insert_node(21)
    tree2.insert_node(10)
    tree2.insert_node(8)
    tree2.insert_node(12)

    tree3 = Tree()
    tree3.insert_node(14)
    tree3.insert_node(5)
    tree3.insert_node(3)
    tree3.insert_node(11)
    tree3.insert_node(16)
    tree3.insert_node(22)

    # Test your method is_similar()
    print('Tree 1 is similar to Tree 2:', tree1.is_similar(tree2))
    print('Tree 1 is similar to Tree 3:', tree1.is_similar(tree3), '\n')

    # Print the various levels of two of the trees that are different
    print('Tree1 level 1:', end=' ')
    tree1.print_level(1)
    print('Tree1 level 2:', end=' ')
    tree1.print_level(2)
    print('Tree1 level 3:', end=' ')
    tree1.print_level(3)
    print('Tree1 level 4:', end=' ')
    tree1.print_level(4)
    print()

    print('Tree3 level 1:', end=' ')
    tree3.print_level(1)
    print('Tree3 level 2:', end=' ')
    tree3.print_level(2)
    print('Tree3 level 3:', end=' ')
    tree3.print_level(3)
    print()

    # Get the height of the two trees that are different
    print('Height of Tree 1:', tree1.get_height())
    print('Height of Tree 3:', tree3.get_height(), '\n')

    # Get the total number of nodes in a binary search tree
    print('Number of nodes in Tree 1:', tree1.num_nodes())
    print('Number of nodes in Tree 2:', tree2.num_nodes())
    print('Number of nodes in Tree 3:', tree3.num_nodes())


main()

