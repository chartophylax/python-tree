
# Обход двоичного дерева в ширину / в глубину
 
class Node:
    def __init__(self, data, left, right):
        self._data = data
        self._left = left
        self._right = right
 
class BinaryTree:
    def __init__(self):
        self._root = None
 
    def make_tree(self, node):
        self._root = node
 
    def insert(self, node):
                 # Вот построить полное двоичное дерево
        lst = []
        def insert_node(tree_node, p, node):
            if tree_node._left is None:
                tree_node._left = node
                lst.append(tree_node._left)
                return
            elif tree_node._right is None:
                tree_node._right = node
                lst.append(tree_node._right)
                return
            else:
                lst.append(tree_node._left)
                lst.append(tree_node._right)
                if p > (len(lst) -2):
                    return
                else:
                    insert_node(lst[p+1], p+1, node)
 
 
        lst.append(self._root)
        insert_node(self._root, 0, node)
 
def breadth_tree(tree):
    lst = []
 
    def traverse(node, p):
        if node._left is not None:
            lst.append(node._left)
        if node._right is not None:
            lst.append(node._right)
        if p > (len(lst) -2):
            return
        else:
            traverse(lst[p+1], p+1)
 
    lst.append(tree._root)
    traverse(tree._root, 0)
 
         # Результат обхода существует в lst таблице
    for node in lst:
        print node._data
 
def depth_tree(tree):
    lst = []
    lst.append(tree._root)
    while len(lst) > 0:
        node = lst.pop()
        print node._data
        if node._right is not None:
            lst.append(node._right)
        if node._left is not None:
            lst.append(node._left)
 
if __name__ == '__main__':
    lst = [12, 9, 7, 19, 3, 8, 52, 106, 70, 29, 20, 16, 8, 50, 22, 19]
    tree = BinaryTree()
         # Сгенерировать полное двоичное дерево
    for (i, j) in enumerate(lst):
        node = Node(j, None, None)
        if i == 0:
            tree.make_tree(node)
        else:
            tree.insert(node)
 
         # Обход в ширину
    breadth_tree(tree)
 
         # Первый обход глубины
    depth_tree(tree)
