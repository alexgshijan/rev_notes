$$\frac{d}{dx}\sin x=\cos x, \frac{d}{dx}\cos x=-\sin x$$

We can prove using [[1.7 - Differentiation]]  from first principles for $\sin x$ and $\cos x$.
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
****
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
****
**Where $f(x)=\sin^{-1}x$**
$$y=\sin^{-1}x$$
*We can 'sin' both sides in order to remove that inverse sin*
$$\sin y=x$$
*Now let's differentiate both sides (implicit)*
$$\frac{d}{dx}\sin y=\frac{d}{dx}x\to\frac{dy}{dx}\cos y=1$$
*We'll bring that cos to the other side in order to get dydx on it's own*
$$\frac{dy}{dx}=\frac{1}{\cos y}$$
*We want this in terms of x tho, so let's change that*
$$\frac{dy}{dx}=\frac{1}{\pm\sqrt{1-\sin^2 y}}=\frac{1}{\pm\sqrt{1-x^{2}}}$$
*The positive root is chosen because the gradient of function $sin^{-1}x$ is always positive*
$$\therefore\frac{dy}{dx}=\frac{1}{\sqrt{1-x^{2}}}$$
*Graph of arcsin / $\sin^{-1}x$*
```desmos-graph
    left=-2
    right=2
    top=2
    bottom=-2
---
y=\arcsin(x)
```
****
**Where $f(x)=\cos^{-1}x$**
$$y=\cos^{-1}x$$
*We can 'cos' both sides in order to remove that inverse cos*
$$\cos y=x$$
*Now let's differentiate both sides (implicit)*
$$\frac{d}{dx}\cos y=\frac{d}{dx}x\to-\frac{dy}{dx}\sin y=1$$
*We'll bring that negative sin to the other side in order to get dydx on it's own*
$$\frac{dy}{dx}=-\frac{1}{\sin y}$$
*We want this in terms of x tho, so let's change that*
$$\frac{dy}{dx}=-\frac{1}{\pm\sqrt{1-\cos^2 y}}=-\frac{1}{\pm\sqrt{1-x^2}}$$
*The negative version of the fraction is chosen because the gradient of function $cos^{-1}x$ is always negative*
$$\therefore\frac{dy}{dx}=-\frac{1}{\sqrt{1-x^2 }}$$
*Graph of arccos / $\cos^{-1}x$*
```desmos-graph
    left=-2
    right=2
    top=3.5
    bottom=-0.5
---
y=\arccos(x)
```
****
**Where $f(x)=\tan^{-1}x$**
$$y=\tan^{-1}x$$
*We can 'tan' both sides in order to remove that inverse tan*
$$\tan y=x$$
*Now let's differentiate both sides*
$$\frac{d}{dx}\tan y=\frac{dy}{dx}x\to\frac{dy}{dx}\sec^{2} y=1$$*We'll bring that tan to the other side in order to get dydx on it's own*
$$\frac{dy}{dx}=\frac{1}{\sec^{2}y}$$
*We can use [[3.5 - Trigonometry]] identities, $\sec^{2}x=1+tan^{2}x$*
$$\frac{dy}{dx}=\frac{1}{1+\tan^{2}y}$$
*We want this in terms of x tho, so let's change that*
$$\therefore\frac{dy}{dx}=\frac{1}{1+x^{2}}$$
*Graph of arctan / $\tan^{-1}x$*
```desmos-graph
    left=-10
    right=10
    top=2
    bottom=-2
---
y=\arctan(x)
```
