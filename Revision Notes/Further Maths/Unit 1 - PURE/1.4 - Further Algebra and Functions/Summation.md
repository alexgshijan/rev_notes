**Sigma Notation** - Note that for r>1, consider splitting into two terms with both r=1 and finding the difference. ie.$\sum\limits^{50}_{r=30}=\sum\limits^{50}_{r=1}-\sum\limits^{29}_{r=1}$
$$\sum\limits^{EndValue}_{r=StartValue}\to\sum^{n}_{r=1}r=\frac{n}{2}(n+1)$$

**Induction proof with summation** - This is a common question, while the exact summation changes the proof always follows the same structure.
$$\text{Prove }\sum\limits^{n}_{r=1}{r^{3}}=\frac{n^{2}(n+1)^{2}}{4}$$
*Let $n=1$*
$$LHS:\sum\limits^{1}_{r=1}r^{3}=1^{3}=1\text{ and }RHS: \frac{1^{2}(1+1)^{2}}{{4}}=\frac{4}{4}=1$$
*Therefore for $n=1$ this proof is valid. Now that we have proved for our base case let's setup our induction process. As such, let $n=k+1$ where $n=k$ is a valid solution for $\sum\limits^{n}_{r=1}{r^{3}}=\frac{n^{2}(n+1)^{2}}{4}$*
$$\sum\limits^{k+1}_{r=1}{r^{3}}=\sum\limits^{k}_{r=1}{r^{3}}+\sum\limits^{k+1}_{r=k+1}{r^{3}}$$
*Now sub in our formulae*
$$\sum\limits^{k+1}_{r=1}{r^{3}}=\frac{k^{2}(k+1)^{2}}{4}+(k+1)^{3}=\frac{k^{2}(k+1)^{2}+4(k+1)^{3}}{4}=\frac{(k+1)^{2}(k^{2}+4(k+1))}{4}$$
*Our goal is to rearrange this so that we return to the original formula where $n= k+1$*
$$\sum\limits^{k+1}_{r=1}{r^{3}}=\frac{(k+1)^{2}(k^{2}+4k+4)}{4}=\frac{(k+1)^{2}(k+2)^{2}}{4}$$
*As proof is valid for $n=1$ and where $n=k$, $n=k+1$ is valid. By Proof by Induction $\sum\limits^{n}_{r=1}{r^{3}}=\frac{n^{2}(n+1)^{2}}{4}$ for all positive integers $n$*


**Summation with multiple terms** - We can split the individual terms into their own summations with the same limits.