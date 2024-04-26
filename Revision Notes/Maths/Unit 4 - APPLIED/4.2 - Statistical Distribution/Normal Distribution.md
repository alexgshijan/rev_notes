*Normal Distribution curves generally look like a bell curve*

**$X$ modelled with the distribution $N(\micro,\sigma^{2})$**

*Where :*
- Mean is represented as $\micro$
- [[Standard Deviation]] is represented as $\sigma$ 
- The data is continuous 
- The area under the graph is 1
- Standard Deviations above the mean is represented as $Z$
- Sample Size is represented as $n$

*The curve has points of inflection one standard deviation from the mean*

**Calc Method**
- Use the `Distribution` submenu
- Since this method uses continuous data, there is no need to change numbers between 'greater than' and 'greater than or equal to'

*You're not required to use the formula for this.*

**Note :**
- If the data peaks too high in the centre and isn't high enough for outer values, increase the variance

**Formula for the Z value :**
X ~ $N(0, 1^{2})$, *we then feed in our probability and we get the Z values as our x*
$$Z=\frac{X-\micro}{\sigma}$$
**Approximating a Binomial Distribution**
An optimal time to use normal distribution rather than binomial, is where you have close to 0.5 probability of an event happening and when you have a high number of trials.

*We use the following calculations to go from Binomial to Normal*
- $\micro=np$
- $\sqrt{np(1-p)}$

However since binomial is discrete, we have to make continuity corrections. This means that we formulate new x values, considering bounds.