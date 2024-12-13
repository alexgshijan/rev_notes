These structures are composed of nodes (also called leaves) and the links between them (also called branches). The top node is also known as the root node. Nodes further down the tree are child/children nodes. *In a binary tree, nodes are only allowed to have two children (left and right branches)*

**Traversal methods for trees. - Output then used for other methods**
*Pre order traversal* - Root, Left, Right - This method can be used to make a copy of the tree.
*In order traversal*- Left, Root, Right - As the name suggests, this will return the data in the correct order
*Post order traversal* - Left, Right, Root - This method can be used to delete the tree.

*Balancing Act*
A tree is only balanced if the difference between the height of the left sub-tree and right sub-tree is not greater than 1 for each node

*Representing a binary in a 2D array*
Allocate indexes to all nodes, starting at 0 for root. Each index has it's left pointer value and it's right pointer value. If there is no child at that location, use index -1 