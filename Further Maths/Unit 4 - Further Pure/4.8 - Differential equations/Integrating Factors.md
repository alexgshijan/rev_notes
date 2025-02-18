**Example : Find the general sol of the differential equation :**
$$\cos x \frac{\delta y}{\delta x}-y\sin x=x^{2}$$
*By inspection spot the derivative that is the LHS*
$$\frac{\delta}{\delta x}(y\cos x)=x^{2}\implies y=\frac{x^{3}}{3\cos x}+\frac{C}{\cos x}$$
It is important note that it is very common that one of the sides on these questions are product rules in disguise.

**What is the integrating factor?**
An integrating factor is a method that can be used to write some first order differential equations in the form of an exact differential equation, so that they can be integrated. This factor is $e^{\int{P(x) dx}}$ for the form shown below. We can safely ignore the constant of the factor.
$$\frac{\delta y}{\delta x}+P(x)y=Q(x)$$
#wip add an example using integrating factors