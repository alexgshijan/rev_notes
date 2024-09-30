*The shortest distance of a point $A$ to a plane is the distance $AP$ where $AP$ is a line perpendicular to the plane and $P$ is a point on the plane.*

**Formula for shortest distance from point to a plane  :**$$|\frac{\alpha n_{1}+\beta n_{2}+\gamma n_{2}+d}{\sqrt{n_{1}^{2}n_{2}^{2}n_{3}^{2}}}|$$
**Shortest distance between two parallel lines :**

*Select a random point on line 1 called P and a random point on line 2 called M in terms of the vector equation.*$$OP=\pmatrix {a\\b\\c} \text{ and }OM=\pmatrix{x\\y\\z}+\lambda\pmatrix{p\\q\\r}=\pmatrix{x+\lambda p\\y+\lambda q\\z+\lambda r}$$*Find distance PM. $$PM=OM-PM=\pmatrix{x+\lambda p\\y+\lambda q\\z+\lambda r}-\pmatrix{a\\b\\c}=\pmatrix{x+\lambda p-a\\y+\lambda q-b\\z+\lambda r-c}$$Then dot product PM with the direction, acknowledging it must be perpendicular.*$$\therefore\pmatrix{x+\lambda p-a\\y+\lambda q-b\\z+\lambda r-c}\cdot\pmatrix{p\\q\\r}=0=p(x+\lambda p-a)+q(y+\lambda q-b)+r(z+\lambda r-c)$$*Finally we expand out and calculate the value of our variable. Then we sub back into PM and mod it to get our shortest distance.*


**Shortest distance between two skew lines :**

*You ned to find point P on one line and point Q on the other such that PQ is perpendicular to both lines.*

*Select a random point on line 1 called P and a random point on line 2 called M both in terms of the vector equation.*$$OP=\pmatrix {a\\b\\c}+\micro\pmatrix{m\\n\\o}=\pmatrix{a+\micro m\\b+\micro n\\c+\micro o\\} \text{ and }OM=\pmatrix{x\\y\\z}+\lambda\pmatrix{p\\q\\r}=\pmatrix{x+\lambda p\\y+\lambda q\\z+\lambda r}$$*We can use OP and OM to calculate PM*$$PM=OM-OP=\pmatrix{x+\lambda p\\y+\lambda q\\z+\lambda r}-\pmatrix{a+\micro m\\b+\micro n\\c+\micro o\\}=\pmatrix{x+\lambda p-a-\micro m\\y+\lambda q-b-\micro n\\z+\lambda r-c-\micro o\\}$$*Find the dot product values of both directions with PM. then simultaneous equations to find the values of lambda and mew. Then we sub back into PM and mod it to get our shortest distance.*$$\pmatrix{x+\lambda p-a-\micro m\\y+\lambda q-b-\micro n\\z+\lambda r-c-\micro o\\}\cdot\pmatrix{m\\n\\o}=0\text{ and }\pmatrix{x+\lambda p-a-\micro m\\y+\lambda q-b-\micro n\\z+\lambda r-c-\micro o\\}\cdot\pmatrix{p\\q\\r}=0$$
