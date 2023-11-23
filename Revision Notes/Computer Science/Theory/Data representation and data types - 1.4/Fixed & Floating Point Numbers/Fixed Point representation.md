A normal non-whole (also known as **real**) number could be represented as 11.75

In binary, this could be written as follows in a 6 bit unsigned binary representation:![[Screenshot 2023-11-23 at 09.24.34.png]] 
The point (also known as binary point – like decimal point in base 10) is assumed here to be at a fixed location. 

Note that it does not take up any memory itself and is only included to illustrate its location. A programmer might specify that the point is always 2 from the right.

To the right of the point each new digit adds halves in value, rather than double when adding digits to the left of the point. 

More digits to the left allow for **larger numbers**, whilst more digits to the right allow for **greater precision.** That is, we can represent numbers more accurately. We’ll come back to this idea later on.

**Negatives :**
The problem with using fixed point representation is that to represent a very large number or a very precise number (numerous decimal places) in binary a **large amount of bits** would be required.
The alternative is to use [[Floating Point Representation]] . This overcomes the problem with fixed point, but at the cost of taking **longer to process** because the CPU must convert them before performing any operation with them.