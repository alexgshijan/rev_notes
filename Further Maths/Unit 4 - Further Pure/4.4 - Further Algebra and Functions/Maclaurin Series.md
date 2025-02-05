**Assume e^x can be written in the form $e^{x}=a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+...$**

To solve first let x=0 $$e^{0}=a_{0}=1\therefore e^{x}=1+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+...$$
By differentiating this series, let x=0 & recursively work through terms
$$\frac{d}{dx}(e^{x})=e^{x}=a_{1}+2a_{2}x^{1}+3a_{3}x^{2}+...\implies e^{0}=a_{1}=1$$
By following the pattern we can derive that a_2 = 2, a_3 = 6, a_4 = 24. Alternatively we could present them as 2!, 3! and 4! respectively.

*As such we can define e^x as the following :*
$$e^{x}=\frac{x^{0}}{0!}+\frac{x^{1}}{1!}+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+...+\frac{x^{r}}{r!}\text{  for all values of x, r lim to infinity}$$

**Approximating with Maclaurin**
In essence we approximate a value by subbing into an appropriate maclaurin series equation and then increasing it's degree of accuracy by using more terms from that series. We finally need to reason why we have chosen that many terms and not more, ie. the next term won't affect the 4dp we were asked to approximate in the question.
