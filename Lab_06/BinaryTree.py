from collections import deque 
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key =obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        #print(self.key, end=" ")
        arr = [self.key]
        if self.leftChild:
            arr += self.leftChild.preorder()
        if self.rightChild:
            arr += self.rightChild.preorder()

        return arr

    def postorder(self, arr=[]):
        #print("key", self.key)
        if type(arr) is not list:
            arr = []

        if self.leftChild:
            #print("Go Left to", self.leftChild.key)
            self.leftChild.postorder(arr)
        if self.rightChild:
            #print("Go Right to", self.rightChild.key)
            self.rightChild.postorder(arr)
        #print(self.key, end=" ")
        arr.append(self.key)
        return arr

    def countNodes(self):
        count = 1
        if self.leftChild:
            count += self.leftChild.countNodes()
        if self.rightChild:
            count += self.rightChild.countNodes()
        return count

    def inorder(self):
        """
        Based on the code from: https://www.geeksforgeeks.org/stack-in-python/

        """
        # Set current to root of binary tree
        current = self
        stack = [] # initialize stack

        while True:
            # Fill the stack with left side of tree
            if current is not None:

                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stack.append(current)
                
                current = current.leftChild


            # Once we get to the bottom of tree,
            # Print the node
            # If the node has right branches, proceed the order in that direction
            # otherwise go to the parent(last position of the stack after popping the current node)
            elif(stack):
                current = stack.pop()
                print(current.key, end=" ") # Python 3 printing

                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.rightChild

            else:
                break
        print("")

    def printLevels(self):
        queue = [self]

        while len(queue) > 0:
            current = queue.pop(0)
            print(current.key, end=" ")
            leftChild = current.getLeftChild()
            rightChild = current.getRightChild()
            if leftChild:
                queue.append(leftChild)
            if rightChild:
                queue.append(rightChild)






