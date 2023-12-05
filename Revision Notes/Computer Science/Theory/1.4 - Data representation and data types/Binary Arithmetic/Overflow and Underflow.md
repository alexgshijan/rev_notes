Computers work with a **fixed [[Computer Science/Theory/1.1 - Hardware and communication/Topic Keywords|world length]]**.
This means the amount of bits in a memory location allocated to a particular operation (e.g. 5-bit, 8-bit, 32 bit, 64 bit etc). It is also the amount the CPU can hold in its registers, and the amount of data that can be transferred along a bus at any one time. 

Sometimes, binary arithmetic may result in a complication: 
- **Overflow** occurs if the result of an arithmetic operation is too large to be stored in the location allocated to it 
- **Underflow** occurs in the result of the operation is too small to be stored in the location allocated to it 

*These complications should be dealt with to avoid crashes*

One method of dealing with overflow is to increase the storage length allocated to each number representation. 2 adjacent memory locations could be used if 1 is not long enough 
A number stored like this is called a **_double-precision number_**
Underflow is less common, but could occur for example if 6 was divided by 12 resulting in 0.5 
This answer is too small to store in fixed-length word structure so underflow would occur. This is solved by using fixed and floating point numbers which we will look at next lesson.