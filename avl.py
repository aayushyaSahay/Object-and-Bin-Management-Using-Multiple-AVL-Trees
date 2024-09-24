from node import Node

def comp_1(node_1, node_2):
    return node_1.key - node_2.key

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)
        self.size += 1

    def _insert(self, node, key, value = None):
        if not node:
            return Node(key, value)
        comparison = self.comparator(Node(key,value), node)
        if comparison < 0:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return self._balance(node)

    def delete(self, key, value = None):
        self.root = self._delete(self.root, key, value)
        self.size -= 1

    def _delete(self, node, key, value = None):
        if not node:
            return node
        comparison = self.comparator(Node(key, value), node)
        if comparison < 0:
            node.left = self._delete(node.left, key, value)
        elif comparison > 0:
            node.right = self._delete(node.right, key, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key, temp.value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return self._balance(node)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node or node.key == key:
            return node
        comparison = self.comparator(Node(key), node)
        if comparison < 0:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def _balance(self, node):
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def _get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def _get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node.left)

    def in_order_traversal(self):
        result = []  
        self._in_order(self.root, result) 
        return result

    def _in_order(self, node, result):
        if not node:
            return
        self._in_order(node.left, result)
        result.append(node.key)  
        self._in_order(node.right, result)
