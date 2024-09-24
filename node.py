class Node:
    def __init__(self, key, value=None):
        self.key = key  # Can be bin_id or object_id
        self.value = value  # The associated data (either bin or object)
        self.left = None
        self.right = None
        self.height = 1



