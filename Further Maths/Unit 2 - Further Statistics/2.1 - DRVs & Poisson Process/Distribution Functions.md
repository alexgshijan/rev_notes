**Exponential Distribution Function**
This calculates the time between events. *The conditions for the exponential distribution to be used are the same as those for the [[Poisson Distribution]], where lambda represents how many events occur per unit time and where x represents time between events.* $$f(x)=\lbrace{\matrix{\lambda e^{-\lambda x}\hspace{1cm}\text{for }x\geq0\\0\hspace{1.9cm}\text{otherwise}}}\implies F(x)=1-e^{-\lambda x}\hspace{1cm}\text{for }x\geq0$$
*Variance and Excepted Value :*$$E(x)=\frac{1}{\lambda}\hspace{2cm}Var(x)=\frac{1}{\lambda^{2}}$$
**Cumulative Distribution Function**
*The cumulative distribution F(x) gives the probability that X is less than or equal to a certain value of x given by the formula :* $$F(x)=P(X\leq x)=\int\limits_{a}^{x}f(PDF)\hspace{0.25cm}dx$$*where a is the lowest value in the range. Ensure that you specify the range*

Note that we can find P(y < x < z) by F(z) - F(y)

**Medians, quartiles and percentiles**
- The nth percentile, pn, of X : $F(p_{n})$ = n% written as decimal
- Median would be 0.5, upper quartile 0.75 and lower 0.25