*When integrating something you suspect to be a function, multiplied by it's differential, we use reverse chain rule*

We *estimate* what we think the integral is, by increasing the power by 1 and ignoring any coefficients. We then differentiate the estimate, and find the difference between our estimate's differential and the original value.

*Worked Example :*
$$\int{x(x^{2}+5)}^{3}\text{ dx}\approx (x^{2}+5)^{4}$$
$$\frac{d}{dx}(x^{2}+5)^{4}=(\frac{d}{dx}(x^{2}+5))(4)(x^{2}+5)^{3}=8x(x^{2}+5)^{3}$$
$$x(x^{2}+5)^{3}=\frac{1}{8}(8x(x^{2}+5)^{3})$$
$$\therefore \int{x(x^{2}+5)}^{3}\text{ dx}=\frac{1}{8} (x^{2}+5)^{4}$$
