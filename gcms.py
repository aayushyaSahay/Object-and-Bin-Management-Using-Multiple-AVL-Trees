from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        self.bins_by_id = AVLTree()  # AVL tree for bins by bin_id
        self.objects_by_id = AVLTree()  # AVL tree for objects by object_id
        self.bins_by_capacity = AVLTree(compare_function=self.compare_bins_by_capacity)  # AVL tree for bins by capacity

    def compare_bins_by_capacity(self, bin_node_1, bin_node_2):
        if bin_node_1.key == bin_node_2.key:
            return bin_node_1.value - bin_node_2.value  # Compare by bin ID if capacities are equal
        else:
            return bin_node_1.key - bin_node_2.key  # Compare by remaining capacity


    def add_bin(self, bin_id, capacity):
        new_bin = Bin(bin_id, capacity)
        self.bins_by_id.insert(bin_id, new_bin)
        self.bins_by_capacity.insert(capacity, bin_id)

    def add_object(self, object_id, size, color):
        new_object = Object(object_id, size, color) # yaha pe new object banaya hai, isme bin_id bad me change karunga
        
        # Find the best bin based on the color and size (Compact Fit or Largest Fit)
        best_bin_id = self.find_best_bin(new_object)
        if best_bin_id is None:
            raise NoBinFoundException()
        
        new_object.bin_id = best_bin_id
        self.objects_by_id.insert(object_id, new_object)
        # he fbest bin is in tirst avl tree, waha se second avl tree mein khoj liya
        self.bins_by_id.search(best_bin_id).value.add_object(new_object)
        # adding object to the selected bin
        # Update the bin in the capacity-based AVL tree TODO: ye sab jaana chahiye find best bin function mein
        # self.bins_by_capacity.delete(best_bin.bin_id)
        # self.bins_by_capacity.insert(best_bin.bin_id, best_bin)

    def find_best_bin(self, object):
        best_bin = None
        current_node = self.bins_by_capacity.root
        
        # BLUE - least capacity + least ID
        if(object.color == Color.BLUE):
            best_fit_capacity = 0
            while current_node:
                if current_node.key >= object.size:
                    best_bin = current_node
                    best_fit_capacty = best_bin.key
                    current_node = current_node.left
                else:
                    current_node = current_node.right
                    
        #TODO: YELLOW
        elif(object.color == Color.YELLOW):
            best_fit_capacity = float('inf')
            while current_node:
                if(current_node.key >= object.size):
                    if(current_node.key < best_fit_capacity):
                        best_bin = current_node
                        best_fit_capacity = current_node.key 
                    current_node = current_node.left  
                else:
                    current_node = current_node.right
            # yaha se bhi best node mil jaygi lekin ab least id wala khojna baki hai
            current_node = best_bin
            while current_node:
                if current_node.key == best_fit_capacity:
                    best_bin = current_node
                    current_node = current_node.right
                else:
                    current_node = current_node.left

        #TODO: RED
        elif(object.color == Color.RED):
            best_fit_capacity = float('-inf')
            while current_node:
                if(current_node.key >= object.size):
                    if(current_node.key > best_fit_capacity):
                        best_bin = current_node
                        best_fit_capacity = current_node.key
                current_node = current_node.right
            # yaha se bhi best node mil jaygi lekin ab least id wala khojna baki hai
            current_node = best_bin
            while current_node:
                if current_node.key == best_fit_capacity:
                    best_bin = current_node
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            # best bin nikal gaya
        # GREEN
        else:
            while current_node:
                if current_node.key >= object.size:
                    best_bin = current_node
                    best_fit_capacity = best_bin.key
                current_node = current_node.right

        if best_bin is not None:
            # Store the bin ID and remaining capacity before deletion
            bin_id = best_bin.value  # Bin ID is stored as the value
            old_capacity = best_bin.key 

            # Delete the bin from bins_by_capacity using the old capacity
            self.bins_by_capacity.delete(old_capacity, bin_id)

            # Insert the bin back with updated capacity (new remaining capacity = old_capacity - object.size)
            self.bins_by_capacity.insert(old_capacity - object.size, bin_id)

            return bin_id  # Return the best bin ID
        else:
            return None


    def delete_object(self, object_id):
        object_node = self.objects_by_id.search(object_id)
        if object_node:
            bin_ref = self.bins_by_id.search(object_node.value.bin_id)
            if bin_ref:
                bin_ref.value.remove_object(object_id)  # Remove the object from the bin
                # Update bin in the capacity tree
                self.bins_by_capacity.delete(bin_ref.value.remaining_capacity - object_node.value.size, bin_ref.key) # acutally bin_ref ki key is id and value is a bin object
                self.bins_by_capacity.insert(bin_ref.value.remaining_capacity, bin_ref.key)  
                self.objects_by_id.delete(object_id)  # Finally, remove from the objects tree
        else:
            return None
        
    def bin_info(self, bin_id):
        bin_node = self.bins_by_id.search(bin_id)
        if bin_node:
            return (bin_node.value.remaining_capacity, bin_node.value.objects_tree.in_order_traversal())
        else:
            return None

    def object_info(self, object_id):
        object_node = self.objects_by_id.search(object_id)
        if object_node:
            return object_node.value.bin_id
        else:
            return None
            