Stacks in a First in Last Out basis.

Pushing – adding a new elements to the top of the stack.
Popping – removing the element at the top of the stack

*This structure is used when calling a sub-routine (function) in a program – the return address is placed on top of the stack and removed when the function returns to the main. It’s also used when undoing actions in programs.*

*Implementation*
Linked list – add a new node to the top (or bottom) of the list, remove the top (or bottom) node from the list – just be sure to stick with whichever end you chose! We need to keep track of the top and bottom of the list with two pointers
Array/list (Python) – add a new element to the end of the array, remove the last element from the array. Again, keep track of the first and last elements with pointers