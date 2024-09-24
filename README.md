# Galactic Cargo Management System (GCMS)

## Overview

The **Galactic Cargo Management System (GCMS)** is a solution to efficiently manage the allocation of cargo in starships' bins, taking into account both capacity and specific handling instructions for different types of cargo. The system implements efficient AVL tree-based algorithms for both bin and object management to ensure optimal performance.

## Features

- **Dynamic Bin Management**: Allows adding, deleting, and managing cargo bins.
- **Efficient Cargo Placement**: Based on the cargo color, the system uses either the Largest Fit or Compact Fit algorithm to place the cargo in an appropriate bin.
- **Exception Handling**: Raises a `NoBinFoundException` when no suitable bin is available for an object.
- **AVL Tree Usage**: Efficient search, insert, and delete operations are implemented using AVL trees.

## Key Algorithms

- **Largest Fit Algorithm**: Places objects in the bin with the largest available capacity.
- **Compact Fit Algorithm**: Places objects in the bin with the smallest available capacity that can still accommodate the object.
- **Handling by Cargo Color**: 
  - **Blue Cargo**: Compact Fit, Least ID.
  - **Yellow Cargo**: Compact Fit, Greatest ID.
  - **Red Cargo**: Largest Fit, Least ID.
  - **Green Cargo**: Largest Fit, Greatest ID.

## Files Overview

### 1. **main.py**
   - This is the entry point for testing and benchmarking the GCMS.
   - It compares the performance of the AVL-based GCMS with a brute-force version, `StupidGCMS`.
   - Includes performance metrics and progress bar visualization.
   - **Key Features**:
     - Adding bins and objects.
     - Deleting objects.
     - Verifying the bin and object information across implementations.
     - Provides stress-testing of random insertions and deletions.

### 2. **gcms.py**
   - Implements the core **Galactic Cargo Management System**.
   - **Key Classes**:
     - `GCMS`: Manages the bins and objects using AVL trees.
   - **Key Methods**:
     - `add_bin`: Adds a new bin.
     - `add_object`: Adds a new object, places it in the best-fit bin.
     - `delete_object`: Removes an object from its assigned bin.
     - `bin_info`: Provides information about a specific bin.
     - `object_info`: Provides information about where a specific object is placed.

### 3. **bin.py**
   - Defines the **Bin** class which represents a cargo bin.
   - **Key Features**:
     - Stores bin ID, capacity, and manages the objects using AVL trees.
     - Methods for adding and removing objects, updating bin capacity.

### 4. **object.py**
   - Defines the **Object** class which represents a cargo item.
   - **Key Features**:
     - Stores object ID, size, and color.
     - Defines the four object colors using an Enum: `BLUE`, `YELLOW`, `RED`, `GREEN`.

### 5. **avl.py**
   - Implements the **AVLTree** class, a self-balancing binary search tree.
   - **Key Features**:
     - Insert, delete, search operations.
     - Automatic balancing through rotations to ensure optimal performance.

### 6. **node.py**
   - Defines the **Node** class used in the AVL tree.
   - Each node contains a key, value, and pointers to left and right children.

### 7. **exceptions.py**
   - Custom exception handling.
   - Defines `NoBinFoundException`, raised when an object cannot be placed into any bin.

### 8. **stupid_gcms.py** (embedded in `main.py`)
   - A simple, brute-force alternative to GCMS for comparison purposes.
   - Uses standard Python lists and dictionaries to simulate bin and object management.

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd <repository-folder>
   ```
2. Make sure you have Python 3 installed.

3. Run the system:
   ```bash
   Copy code
   python main.py
   ```
4. Observe progress and test outputs. The system will compare the GCMS and StupidGCMS implementations, verifying that both work correctly.

## Example Usage
### Adding Bins
  ```python
  Copy code
  gcms.add_bin(1, 100)
  gcms.add_bin(2, 150)
  ```
### Adding Objects
  ```python
  gcms.add_object(101, 50, Color.RED)
  gcms.add_object(102, 30, Color.BLUE)
  ```
### Retrieving Bin Information
  ```python
  gcms.bin_info(1)
  ```
### Deleting an Object
  ```python
    gcms.delete_object(101)
  ```
## License
This project is licensed under the MIT License. See the LICENSE file for details.
