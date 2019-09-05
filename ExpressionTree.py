
#  File: ExpressionTree.py
#  Description: Reads an expression and converts it into an expression tree

#  Student Name: Woongchan Lee
#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim
#  Partner UT EID: DK25659

#  Course Name: CS 313E
#  Unique Number: 85575
#  Date Created: 07/29/2019
#  Date Last Modified: 07/29/2019


class Stack (object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stackis empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return len(self.stack)


class Node (object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        # self.parent = None

    def __str__(self):
        s = str(self.data)
        return s


class Tree (object):
    def __init__(self):
        self.root = None
        self.operators = ['+', '-', '*', '/', '//', '%', '**']
        self.expr = ''

    # creates an expression tree based on a string expression
    # assumes that expression is written correctly
    def create_tree(self, expr):
        self.expr = expr
        s = Stack()
        cur = None
        for char in expr:
            if char == '(':
                if self.root == None:
                    self.root = Node('')
                    cur = self.root
                cur.lchild = Node('')  # new node as the left child of the current node
                s.push(cur)  # push current node on the stack
                cur = cur.lchild  # make current node equal to the left child
            elif char in self.operators:
                if self.root == None:
                    self.root = Node('')
                    cur = self.root
                cur.data = char  # current node data equals operator
                s.push(cur)  # push current node on the stack
                cur.rchild = Node('')  # new node as the right child of the current node
                cur = cur.rchild  # make current node equal to the left child
            elif char != ')':  # if character is an operand
                if self.root == None:
                    self.root = Node('')
                    cur = self.root
                if self.is_int(char):  # check if char is integer
                    cur.data = int(char)
                else:
                    cur.data = float(char)
                cur = s.pop()  # make current node equal to the parent by popping
            elif not s.is_empty():  # if character is a right parenthesis
                cur = s.pop()  # make current node equal to the parent by popping)

    # helper method for recursion
    def evaluate(self, aNode):
        value = self.eval(aNode)
        self.root = None
        self.create_tree(self.expr)
        return value

    # recursive method to solve value of expression tree
    def eval(self, aNode):
        if aNode != None:
            # if children are not usable operands, recursively go down tree and solve
            if not isinstance(aNode.lchild.data, (int, float)):
                self.eval(aNode.lchild)
            if not isinstance(aNode.rchild.data, (int, float)):
                self.eval(aNode.rchild)
            # both children are now numbers, now use operator on both children
            if aNode.data == '+':
                aNode.data = aNode.lchild.data + aNode.rchild.data
            elif aNode.data == '-':
                aNode.data = aNode.lchild.data - aNode.rchild.data
            elif aNode.data == '*':
                aNode.data = aNode.lchild.data * aNode.rchild.data
            elif aNode.data == '/':
                aNode.data = aNode.lchild.data / aNode.rchild.data
            elif aNode.data == '//':
                aNode.data = aNode.lchild.data // aNode.rchild.data
            elif aNode.data == '%':
                aNode.data = aNode.lchild.data % aNode.rchild.data
            elif aNode.data == '**':
                aNode.data = aNode.lchild.data ** aNode.rchild.data
            return aNode.data
        return None

    # prints expression tree in prefix
    def pre_order(self, aNode):
        if aNode != None:
            print(aNode.data, end=' ')
            self.pre_order(aNode.lchild)
            self.pre_order(aNode.rchild)

    # prints expression tree in postfix
    def post_order(self, aNode):
        if aNode != None:
            self.post_order(aNode.lchild)
            self.post_order(aNode.rchild)
            print(aNode.data, end=' ')

    # returns True if string is an integer
    # does not return True for floats
    def is_int(self, string):
        try:
            int(string)
            return int(string) == float(string)
        except ValueError:
            return False


def read_in(file_name):
    inf = open(file_name, 'r')
    string = inf.readline()
    inf.close()
    return string


def main():
    string = read_in('expression.txt')
    # create tree
    exp_tree = Tree()
    exp_tree.create_tree(string.split())
    # test evaluate method
    if '\n' in string:
        print(string[0:len(string)-1], '=', exp_tree.evaluate(exp_tree.root))
    else:
        print(string, '=', exp_tree.evaluate(exp_tree.root))
    # test pre_order method
    print('Prefix Expression:', end=' ')
    exp_tree.pre_order(exp_tree.root)
    # test post_order method
    print('\nPostfix Expression:', end=' ')
    exp_tree.post_order(exp_tree.root)
    print()


main()

