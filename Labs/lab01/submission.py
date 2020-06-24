## import modules here


################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    if x in (0, 1):
        return x

    start = 0
    end = int(x / 2)
    root = 0

    while start <= end:
        mid = int((start + end) / 2)

        if mid ** 2 == x:
            return mid

        if mid ** 2 < x:
            start = mid + 1
            root = mid
            continue

        end = mid - 1

    return root


################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them
def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    x = x_0

    for i in range(MAX_ITER):
        x_new = x - f(x) / fprime(x)

        if abs(x - x_new) < EPSILON:
            return x

        x = x_new

    return x


################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def make_tree(tokens): # do not change the heading of the function
    root = Tree(tokens[0])
    parent = root
    node = root
    temp = []

    for i in tokens[1:]:
        if i == '[':
            temp.append(parent)
            parent = node
        elif i == ']':
            parent = temp[-1]
            temp = temp[:-1]
        else:
            node = Tree(i)
            parent.add_child(node)

    return root

def max_depth(root): # do not change the heading of the function
    if not root.children:
        return 1

    d = [1]

    for i in root.children:
        d.append(max_depth(i) + 1)

    return max(d)
