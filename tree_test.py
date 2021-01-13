class Node:
  def __init__(self, idx):
      self.data = ""
      self.left = idx
      self.right = -1

class ExpressionTree:
    def __init__(self):
      self.tree = list()
      for index in range(1, 21):
       self.tree.append(Node(index))

      self.fringe = list()
      self.root = 0
      self.next = 0

    def isOperator(self, s):
         if '+' in s:
          return True
         if '-' in s:
          return True
         if '*' in s:
          return True
         if "/" in s:
          return True
         return False

    def insert(self, token):
        if self.next == -1:  # check if tree is full
            print("Tree has no space")
            return False  # tree is not full, safe to insert new token

        if self.next == 0:
            self.tree[self.root].data = token
            self.next = self.tree[self.root].left
            self.tree[self.root].left = -1
        else:
            current = 0  # index of the current node
            previous = -1  # index of previous node
            new_node = self.tree[self.next]  # declare new node
            new_node.data = token  # Finding the node at which the NewNode can be inserted
            while current != -1:
                curr_node = self.tree[current]
                if self.isOperator(curr_node.data):
                    if curr_node.left == -1:
                        curr_node.left = self.next
                        self.next = new_node.left
                        new_node.left = -1
                        current = -1
                    elif curr_node.right == -1:
                        curr_node.right = self.next
                        self.next = new_node.left
                        new_node.left = -1
                        current = -1
                    elif self.isOperator(self.tree[curr_node.left].data):
                        previous = current
                        current = curr_node.left
                        self.fringe.append(previous)
                    elif self.isOperator(self.tree[curr_node.right].data):
                        previous = current
                        current = curr_node.right
                        self.fringe.append(previous)
                    else:
                        previous = self.fringe.pop(-1)
                        current = self.tree[previous].right
                else:
                    print("Can not insert here")
                    return False

    def infix(self, root, arr):
        if root.data != "":
            if self.isOperator(root.data):
                arr.append('(')
                self.infix(self.tree[root.left], arr)
            arr.append(root.data)
            self.infix(self.tree[root.right], arr)
            if self.isOperator(root.data):
                arr.append(')')



expressionTree = ExpressionTree()
expressionTree.insert('+')
expressionTree.insert('x')
expressionTree.insert('+')
expressionTree.insert('y')
expressionTree.insert('x')



import math

x = 5
y = 5
l = math.log(x)
assignment = {"x" : x, "y" : y, "log": l}


arr = []
expressionTree.infix(expressionTree.tree[0], arr)
expression_string = ''.join(arr[1:-1])
print(expression_string)


def find_operator(stack):
    op_list = ["+","-","*","/"]
    print(stack)
    length = len(stack) - 1
    print("Length: ", length)
    for op in op_list:
        idx = 0
        for lit in reversed(stack):
            print(lit,idx)
            if lit == op:
                return length - idx
            idx += 1
    return -1

def processing(stack):

    op_idx = find_operator(stack)
    print("found it:  ", op_idx)
    right = stack.pop()  # get right number




    #TODO: search for operator and split by idx
    #print(right)
    if right in assignment.keys():
        right = assignment[right]
    else:
        right = int(right)
    operator = stack.pop()  # get operator


    left = stack.pop()  # get left number

    if left in assignment.keys():
        left = assignment[left]
    else:
        left = int(left)

    if '+' in operator:
        left += right
    elif '-' in operator:
        left -= right
    elif '*' in operator:
        left *= right
    elif '/' in operator:
        left /= right
    return left, stack

def calculate(expression):


    stack = []
    count = 0
    left = 0
    #TODO: ADD SUPPORT FOR MULTIPLE LITERALS
    length = len(expression)
    for char in expression:

        if count+1 < length:
            if ord(expression[count+1]):
                stack.append(char)
                count+=1
                continue

        stack.append(char)
        if char == ')':
            stack.pop()
            left, stack = processing(stack)
            stack.pop()
            stack.append(left)

        if count == len(expression)-1: # last char of expression string
            left, stack = processing(stack)
        count += 1
    return left

print(calculate(expression_string))