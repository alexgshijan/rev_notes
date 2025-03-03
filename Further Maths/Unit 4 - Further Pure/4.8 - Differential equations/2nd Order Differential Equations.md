For second order differentials we can make the substitution $x=Ae^{mt}$ as it's a general sol for a term that can differentiated twice to equal it's original term.

**Key Terms**
*Auxiliary Equation* - The equation formed by subbing in $x=Ae^{mt}$ and simplifying.
*Homogenous Equation* - Where RHS is = 0
*Inhomogeneous Equation* - Where RHS is $\neq$ 0
*Complimentary Function* - The solution of a homogeneous 2nd ODE 
*Particular Function* - The solution of an inhomogeneous 2nd ODE

**Worked Example** - $\frac{d^{2}x}{dt^{2}}+2 \frac{dx}{dt}-8x=0$
$$\text{Let }x=Ae^{mt}\implies \frac{dx}{dt}=mAe^{mt}\implies \frac{d^{2}x}{dt^{2}}=m^{2}Ae^{mt}$$
Sub this into the original equation 
$$\frac{d^{2}x}{dt^{2}}+2 \frac{dx}{dt}-8x=0\to m^{2}Ae^{mt}+2mAe^{mt}-8Ae^{mt}=0\implies m^2+2m-8=0$$
We can finally find values for m and then write it as a general solution 
$$x=Ae^{2t}+be^{-4t}$$
**General Solutions**

| Roots of auxiliary equation     | Form of General Solution      |
| ------------------------------- | ----------------------------- |
| Two distinct real roots a and b | $x=Ae^{at}+Be^{bt}$           |
| One repeated root m             | $x=(A+Bx)e^{mt}$              |
| Pure imaginary roots $\pm ni$   | $x=A\cos nt+B\sin nt$         |
| Complex roots $p\pm qi$         | $x=e^{pt}(A\cos qt+B\sin qt)$ |
