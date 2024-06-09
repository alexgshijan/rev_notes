**Inverse Trig functions**
$$\cos^{-1} x=\sec x,\sin^{-1} x=\csc x,\tan^{-1} x=\cot x$$
We can use those to derive new trig identities 
$$1+\tan ^{-2}x=\sin^{-2}x,1+\tan ^{2}x=\sin^{2}x$$


**Rewriting $b\sin x + c\cos x=R\sin(x+a)$**

*First we expand $R\sin(x+a)$ using the double angle formula*
$$R\sin (x+a)=R\sin x\cos a+R\sin a\cos x$$
*Compare coefficients with the original $b\sin x + c\cos x$*
$$b=R\cos a \text{ , }c=R\sin a$$
*Use trig identities to find R and a*
$$\tan a=\frac{R\sin a}{R\cos a}\therefore\tan^{-1}\frac{c}{b}=a$$
$$R=\sqrt{b^{2}+c^{2}}$$
*Finally rewrite the equation*
$$b\sin x + c\cos x=\sqrt{b^{2}+c^{2}}\sin(x+\tan^{-1}\frac{c}{b})$$