import avl

class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.remaining_capacity = capacity
        self.objects_tree = avl.AVLTree()  #AVL tree for objects in the bin

    def add_object(self, object):
        if self.remaining_capacity >= object.size:
            self.objects_tree.insert(object.object_id, object.size)
            self.remaining_capacity -= object.size

    def remove_object(self, object_id):
        object_node = self.objects_tree.search(object_id)
        if object_node:
            self.remaining_capacity += object_node.value
            self.objects_tree.delete(object_id)
