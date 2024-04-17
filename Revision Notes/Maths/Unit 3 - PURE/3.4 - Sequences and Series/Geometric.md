An Geometric Sequence is where you *multiply* a value to get the next value   

We use $a$ to denote the *first term*, $r$ is the *ratio* between terms, and $n$ is the *position* of the term we're interested in. We can express this with :$$u_n=ar^{n-1}$$
**Formula for an geometric series :**$$S_n=\frac{a(1-r^{n})}{1-r}$$*proof :*
$S_n=a+ar+ar^{2}+ar^{3}+ar^{4}+...+ar^{n-2}+ar^{n-1}$
$rS_n=ar+ar^{2}+ar^{3}+ar^{4}+...+ar^{n-1}+ar^{n}$
$S_n-rS_{n}= a-ar^{n}$
$S_n(1-r)= a(1-r^{n})$
$S_n=\frac{a(1-r^{n})}{1-r}$

**Sum to infinity**
A [[Geometric]] series is convergent when $|r|<1$, we can work out *the value it converges towards* by using this formula :$$S_{\infty}=\frac{a}{1-r}$$