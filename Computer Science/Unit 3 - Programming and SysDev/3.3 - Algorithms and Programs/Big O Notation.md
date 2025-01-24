\The CPU and main memory are valuable resources. There is a limit on what can be done in a given amount of time - When we design algorithms we want to be as efficient as possible. Big O Notation measures and compares the time & space complexity and performance of algorithms - It looks at how long an algorithm takes in the worst-case scenario. 

*An “O” is used as a prefix for all expressions written in big O notation. An “n” is used to refer to the number of items. This is the algorithms “growth rate”, it can apply to both the time and space complexities.*

**Complexities** - (where a represent constants & n is number of items.)
- Constant - O(a) - Complexity remains constant no matter how much data processed.
	- Performance doesn't change no matter the size of data.
	- A lot of algorithms have constant for their space complexity, as it doesn't take up any extra space even if there are more items in the array.
	- Hashed Random Access would be a valid example of this.
- Logarithmic - O(log n) - Complexity rises decreasingly as more data processed.
	- Binary search and binary tree search are examples of this. 
	- For large data sets, these are much quicker than a linear search.
- Linear - O(n) - Complexity proportional to the number of items.
- Polynomial - O($n^{a}$) - Complexity rises increasingly as more data processed.
	- Examples of these would be functions that use nested loops like Nested + Bubble
- Exponential - O($a^{n}$) - Complexity rises exponentially as more data processed.
*In order of best to worst time complexity, on average.*

Note that as n tends of infinity, coefficients of the notation becomes irrelevant. When considering the complexity of an algorithm, you need to consider each individual component and the complexity it adds.

```
for j in 0 to N:
	print(j)
```
This loop is going to happen N times. The loop itself has a growth rate of O(N). The line inside the loop is not dependant on the value of N, so it has a growth rate of O(1). Therefore complexity is N + 1. However, if we scale up the value of N towards infinity, the +1 becomes insignificant, so we can simplify it to O(N)

**Time Complexity** - Considering the extra space the algorithm uses as it is running

Bubble & insertion sort don’t create any new data structures or require more storage as they are running, so they are O(1)
Merge sort requires the creation of N new lists when it is separating the elements out so that they can be merged back together, so has a space complexity of O(N)
Quick sort is a recursive algorithm, so will be O(log(N)) for the same reasons as binary search.