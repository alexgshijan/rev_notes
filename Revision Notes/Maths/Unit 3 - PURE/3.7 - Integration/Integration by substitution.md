For some integrations involving a complicated expression, we can make a substitution to turn it into an equivalent integration that is simpler.

*First we introduce a new variable, lets use a worked example* 
$$u=2x+5 \text{ to find} \int x\sqrt{2x+5}\text{ dx}$$
*Let's rearrange u to find some key information*
$$\frac{\delta u}{\delta x}=2,\delta u =2\delta x, \delta x=\frac{\delta u}{x},x=\frac{u-5}{2}$$
*Let's sub these back into the original equation*
$$\int x\sqrt{2x+5}\text{ dx}=\int\frac{u-5}{2}\sqrt{u}\cdot\delta u\frac{1}{2}=\int(u-5)\sqrt{u}\cdot\delta u\frac{1}{4}$$
*We then need to actually integrate in terms of u*
$$=\int u^{\frac{3}{2}}-5u^{\frac{1}{2}}\cdot\delta u\frac{1}{4}=\frac{1}{4}(\frac{2}{5}u^{\frac{5}{2}}-\frac{10}{3}u^{\frac{3}{2}})+C$$
*Finally sub the value for u back in and then clean up*
$$=\frac{(2x+5)^{\frac{5}{2}}}{10}-\frac{5(2x+5)^{\frac{3}{2}}}{6}+C$$


**Note :**
When using this method for a fraction with the denominator $a+x^{2}$, use $x=\tan\theta$, and with the denominator $\sqrt{a-x^{2}}$,  use $x=\sqrt{a}\sin\theta$

