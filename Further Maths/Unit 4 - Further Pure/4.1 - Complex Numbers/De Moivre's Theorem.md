*Points to remembers*
- Odd functions are where f(-x)= -f(x), Even functions are where f(-x)=f(x)
- [[Argand Diagram]]

**Formula :**$$(\cos\theta+i\sin\theta)^{n}=\cos n\theta+i\sin n\theta \text{ for any integer } n$$
**Using de Moivre's Theorem to find trigonometric identities**
Let $Z=\cos\theta+i\sin\theta \implies Z^{n}=\cos n\theta+i\sin n\theta\hspace{0.5cm}\text{ and  }\hspace{0.5cm}Z^{-n}=\cos n\theta-i\sin n\theta$ 

*By summing and collecting terms we derive the following*
$$\sin n\theta=\frac{Z^{n}-Z^{-n}}{2i}\hspace{0.5cm}\text{ and  }\hspace{0.5cm}\cos n\theta=\frac{Z^{n}+Z^{-n}}{2}$$
**Example use-case - Express $\cos^{5}\theta$ as multiple angles**
*Let $Z=\cos\theta+i\sin\theta$, using de Moivre's Theorem we know that $\cos n\theta=\frac{Z^{n}+Z^{-n}}{2}$
In order to use this formula for our case of $\cos^{5}\theta$, we set n equal to 1*
$$\cos \theta=\frac{Z^{1}+Z^{-1}}{2}\to\cos^{5} \theta=\frac{(Z^{1}+Z^{-1})^{5}}{2^{5}}=\frac{(Z^{1}+Z^{-1})^{5}}{32}$$
*Use [[Binomial Theorem - Expansion]] to expand this term.*
$$(Z^{1}+Z^{-1})^{5}=Z^{5}+5Z^{3}+10Z+10Z^{-1}+5Z^{-3}+Z^{-5}$$
*Use the inverse of the original identity $\cos n \theta=\frac{Z^{n}+Z^{-n}}{2}\implies 2\cos n \theta=Z^{n}+Z^{-n}$*
$$(Z^{1}+Z^{-1})^{5}= 2\cos 5\theta+10\cos 3\theta + 20\cos\theta\implies\frac{(Z^{1}+Z^{-1})^{5}}{32}=\frac{2\cos 5\theta+10\cos 3\theta + 20\cos\theta}{32}$$
*Finally we tidy our results and conclude.*
$$\therefore\cos^{5}\theta=\frac{2\cos 5\theta+10\cos 3\theta + 20\cos\theta}{32}$$

We can consider the imaginary and real separately to suit our use case

**Roots of Unity Example : Solve $x^{3}=1$**
*Method 1*
As the largest is odd we know that at least one root must be real and that the remaining roots must be conjugate pairs. By cube rooting 1 we can find the real root is (x-1), checking using the [[Remainder Theorem]]. By using polynomial division, to find the remaining quadratic and then using the quadratic equation, we find that $x=1,\frac{-1+\sqrt{3}i}{2},\frac{-1-\sqrt{3}i}{2}$

*Method 2*
We let $Z=1$ and treat it as a complex number, we find that the modulus of Z is 1 and the argument would be $0,2\pi,4\pi,...$ As our modulus is 1, we use the identity $Z=e^{i\theta}$, input our arguments and then cube root. This gives us the values of $x=e^{0},e^{\frac{2\pi i}{3}},e^{\frac{4\pi i}{3}}$ or $x=1,\frac{-1+\sqrt{3}i}{2},\frac{-1-\sqrt{3}i}{2}$ 

*Method 3*
Draw an argument diagram, for roots of unity the $2\pi$ is split equally by the value of the power, with 1 as the first solution. Use trig to find the rest.x

