*This methods utilises the fact that the tangent of a curve generally points towards the roots of a curve.*

By rearranging the equation to find out the gradient, we discover what both  Newton and Raphson did so many years ago.
$$x_{n+1}=x_{n}-\frac{f(x_{n})}{f'(x_{n})}$$
*This method is extremely quick at converging on the root*

*There are possible points of failure*
- If you come across a stationary point - *Since this method divides by gradient*
- If there is a discontinuity in the graph