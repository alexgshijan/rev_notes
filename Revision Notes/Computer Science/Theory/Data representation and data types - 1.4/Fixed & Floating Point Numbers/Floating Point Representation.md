**In normal maths, a way to represent large numbers is using standard form**

![[Pasted image 20231123092901.png]]

This can be imitated in binary using floating point representation. 

The **mantissa** section is represented as a fixed point binary number, which could be either a sign/magnitude or two’s complement number. The number of bits allocated to this determines the **precision** of the number – how small a fraction can be stored (therefore how accurate the number is)

The **exponent** section is represented as a separate binary number, again either with sign/magnitude or two’s complement. The number of bits allocated to this determines the **range** of the number – the maximum and minimum numbers that can be represented in a given amount of memory.