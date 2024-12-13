*This method finds the roots at points at which the gradient is small*

*We rearrange the equation equal to x, we then iterate through values of x, feeding the output value as our new x. This value should then converge onto our roots.*

Note that if the value diverges, then there are no values with small gradients, and so a new $x_0$ must be selected.

*As far as notation goes, here is an example :*
$$x^{3}-7x+3=0 \to x_{n+1} = (7x_n-3)^{\frac{1}{3}}$$
Note that $x_{0}$ is an arbitrary value we choose. We can be kinda smart with this by selecting values near valid roots

*There is also another trick you can employ, you can rearrange the original formula to get different curves, which allows us to investigate different roots regardless of it's original gradient*

By plotting our x series on a graph we can form the following diagrams. Note that if the gradient at the point is positive it forms a 'staircase', else it forms a cobweb.

![[image.png]]

We can finally use [[Intermediate Value Theorem]] to prove a root using rounding bounds