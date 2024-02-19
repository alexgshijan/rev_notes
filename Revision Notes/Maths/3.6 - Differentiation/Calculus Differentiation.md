[[1.7 - Differentiation]]  from first principles for $\sin x$ and $\cos x$.
$$f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$$
**Where $f(x)=\sin x$**
$$f'(x)=\lim_{h\to 0}\frac{\sin(x+h)-\sin(x)}{h}$$
*[[3.5 - Trigonometry]] Identities can be used to expand the $\sin(x+h)$*
$$f'(x)=\lim_{h\to 0}\frac{\sin x\cos h+\sin h\cos x-\sin x}{h}$$
*[[3.5 - Trigonometry]] Small Angle approximation means $\sin h=h$ and $\cos h =1- \frac{h^{2}}{2}$*
$$f'(x)=\lim_{h\to 0}\frac{\sin x(1- \frac{h^{2}}{2})+h\cos x-\sin x}{h}$$
*We can then expand and collect like terms*
$$f'(x)=\lim_{h\to 0}\frac{\sin x- \sin x\frac{h^{2}}{2}+h\cos x-\sin x}{h}=\lim_{h\to 0}\frac{h\cos x- \sin x\frac{h^{2}}{2}}{h}$$ *Then divide through by $h$*
$$f'(x)=\lim_{h\to 0} \cos x- \sin x\frac{h}{2}$$
*As $h$ tends towards 0, it will eventually = 0*
$$\therefore f'(x)=\cos x$$


**Where $f(x)=\cos x$**
$$f'(x)=\lim_{h\to 0}\frac{\cos(x+h)-\cos(x)}{h}$$
*[[3.5 - Trigonometry]] Identities can be used to expand the $\cos(x+h)$*
$$f'(x)=\lim_{h\to 0}\frac{\cos x\cos h-\sin h\sin x-\cos x}{h}$$
*[[3.5 - Trigonometry]] Small Angle approximation means $\sin h=h$ and $\cos h =1- \frac{h^{2}}{2}$*
$$f'(x)=\lim_{h\to 0}\frac{\cos x(1- \frac{h^{2}}{2})-h\sin x-\cos x}{h}$$
*We can then expand and collect like terms*
$$f'(x)=\lim_{h\to 0}\frac{\cos x- \frac{h^{2}}{2}\cos x-h\sin x-\cos x}{h}=\lim_{h\to 0}\frac{- \frac{h^{2}}{2}\cos x-h\sin x}{h}$$
 *Then divide through by $h$*
 $$f'(x)=\lim_{h\to 0}[- \frac{h}{2}\cos x-\sin x]$$
 *As $h$ tends towards 0, it will eventually = 0*
$$\therefore f'(x)=-\sin x$$