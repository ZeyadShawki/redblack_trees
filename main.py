import sys


# data structure that represents a node in the tree
class Node():

    def __init__(self, data):
        self.data = str(data)  # holds the key
        self.parent = None  # pointer to the parent
        self.left = None  # pointer to left child
        self.right = None  # pointer to right child
        self.color = 1  # 1 . Red, 0 . Black


# class RedBlackTree implements the operations in Red Black Tree
class RedBlackTree():
    def __init__(self):
        self.TNULL = Node("NIL")
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def __in_order_helper(self, node):
        if node != self.TNULL:
            self.__in_order_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.__in_order_helper(node.right)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
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

        # rotate right at node x

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
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

    # fix the red-black tree
    def __fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 1:
                    # case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # case 3.2.2
                        k = k.parent
                        self.right_rotate(k)
                    # case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color == 1:
                    # mirror case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # mirror case 3.2.2
                        k = k.parent
                        self.left_rotate(k)
                    # mirror case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    # In-Order traversal

    def inorder(self):
        self.__in_order_helper(self.root)

    def insertRb(self, key):
        # Ordinary Binary Search Insertion
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1  # new node must be red

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # if new node is a root node, simply return
        if node.parent == None:
            node.color = 0
            return

        # if the grandparent is None, simply return
        if node.parent.parent == None:
            return

        # Fix the tree
        self.__fix_insert(node)

    def get_root(self):
        return self.root

    def exists(self, val):
        curr = self.root
        MOV = curr
        # print(val)
        while MOV != self.TNULL:
            # print(MOV.data)
            if val == MOV.data:
               # print(MOV.data + "already exists")
                return True
            else:
                if val < MOV.data:
                    MOV = MOV.left
                #  print("l" + " " + MOV.data)

                else:
                    MOV = MOV.right
                #   print("r" + " " + MOV.data)
        #print("Doesn't exist")
        return False

    def load(self, dictname):
        f = open(dictname, 'rt')
        lines = f.read().splitlines()
        f.close()
        for line in lines:
            self.insertRb(line)
        # self.inorder()

    def count(self, node):
        if node.left == None and node.right == None:
            return 0
        else:
            return 1 + self.count(node.left) + self.count(node.right)

    def compareMax(self, a, b):
        if a > b:
            return a
        else:
            return b

    def height(self, node):
        if node.left == None and node.right == None:
            return 0
        else:
            return 1 + self.compareMax(self.height(node.left), self.height(node.right))


if __name__ == "__main__":
    dictname = 'EN-US-Dictionary.txt'
    bst = RedBlackTree()
    bst.load(dictname)
    while 1:
        print("RB is loaded Give ur order \n")
        a = input("FOR INSERT PRINT 1\tFOR SEARCH PRINT 2 :\n")
        if a == '1':
            b = input("insert ur word :\n")
            if bst.exists(b):
                print("word already exists")
            bst.insertRb(b)
        if a == '2':
            c = input("lookup ur word :\n")
            if bst.exists(c):
                print(c+" "+"EXISTS")
            else:
                print(c + " " + "DOESN'T EXIST")
        print(bst.height(bst.root))
        print(bst.count(bst.root))
        print("===========================================================================")
