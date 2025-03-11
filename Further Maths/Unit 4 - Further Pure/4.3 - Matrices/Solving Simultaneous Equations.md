**Method 1**
Where $A=\pmatrix{a&b\\c&d}$ from the simultaneous equations $ax+by=e$ and $cx+dy=f$
$$A\pmatrix{x\\y}=\pmatrix{e\\f}\implies A^{-1}A\pmatrix{x\\y}=A^{-1}\pmatrix{e\\f}$$
By multiplying the A inverse with $e,f$ we get values for $x,y$

If the two equation are contradictory, the equations are said to be inconsistent. In other cases where the equations overlap either infinitely or at a point, these are consistent. This can be observed by inspection, which is hard w/ multiple equations.

The Method can also be expanded to work with $x,y,z$

Note this method can only work if all planes meet at a single point

**Method 2 : Echelon Row Form**
Equations can be arranged into an augmented matrix. Here's an example with random numbers
$$\begin{pmatrix}
    2 & 3 & 5  &\bigm| & 5 \\
    23 & 1 & 12 &\bigm| & 4 \\
    2 & 2 & 1 &\bigm| & 2 \\ 
\end{pmatrix}$$
If the matrix is rearranged into the row echelon form, it is quite simple to solve using linear algebra and back substitution. Note that reduced echelon form is what insinuates the leading one, but it may be worth doing it just incase. Example :
$$\begin{pmatrix}
    1 & a & b  &\bigm| & d \\
    0 & 1 & c &\bigm| & e \\
    0 & 0 & 1 &\bigm| & f \\ 
\end{pmatrix}$$
*Using Reduction to turn an augmented matrix into row echelon form*
You can reduce an augmented matrix to row-echelon form by carrying out a combination of elementary row operations which can be any of the following:
- ﻿﻿Interchange any of the rows
- ﻿﻿Multiply or divide each element in any of the rows by a constant
- ﻿﻿Add or subtract a multiple of one of the rows to another row
Repeat these steps in any order in order to get row echelon form, the idea is to first get the leading 0 by subtracting/ adding another row, then to divide by a constant to get the leading 1.

**A reduced echelon form that is consistent will have a row of zeros that is equal to zero, an inconsistent will form a row of zeros that is not equal to zero.**