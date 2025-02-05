Proof by induction of [[De Moivre's Theorem]]
$$\text{Prove }(\cos\theta+i\sin\theta)^{n}=\cos n\theta+i\sin n\theta \text{ for any integer } n$$
*Let $n = 1$*
$$(\cos\theta+i\sin\theta)^{1}=\cos 1\theta+i\sin 1\theta$$
*Therefore for $n=1$ this proof is valid. Now that we have proved for our base case let's setup our induction process. As such, let $n=k+1$ where $n=k$ is a valid solution for $(\cos\theta+i\sin\theta)^{n}=\cos n\theta+i\sin n\theta$*
$$(\cos\theta+i\sin\theta)^{k+1}=\cos(k+1)\theta+i\sin(k+1)\theta$$
*Let's take the RHS and turn it into the LHS*
$$\text{RHS : }(\cos\theta+i\sin\theta)^{k+1}=(\cos\theta+i\sin\theta)^{k}(\cos\theta+i\sin\theta)^{1}=(\cos k\theta+i\sin k\theta)(\cos\theta+i\sin\theta)$$
*Expand and collect real and imaginary terms*
$$=\cos k\theta\cos \theta-\sin k\theta\sin\theta+i(\cos k\theta\sin\theta+\cos\theta\sin k\theta)$$
*Sub in our trig double angle identities*
$$=\cos(k+1)\theta+i\sin(k+1)\theta = LHS$$
*As proof is valid for $n=1$ and where $n=k$ is valid, $n=k+1$ is also valid. By Proof by Induction $(\cos\theta+i\sin\theta)^{n}=\cos n\theta+i\sin n\theta$ True for all positive integers $n$*