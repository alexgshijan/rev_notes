RAM (Random Access Memory) stores currently running programs and their data. The “random” part means that the processor can access any location equally as quickly as any other location in the RAM. Access to RAM is much faster than to a storage device such as a hard drive or USB.

RAM is still slow however when compared to the speed of the CPU, we therefore need an intermediary so that there is no “bottlenecking”. This is where cache comes in. Cache is extremely fast temporary storage inside the CPU where commonly used instructions are held

**Why not just have lots more cache :**
	However, Firstly, cache memory is very expensive. Secondly, the larger it becomes, the slower it operates. This is partly why there are multiple levels of cache memory, with each level further away from the CPU being bigger and slower. When data is required, the smallest (and fastest) level is checked first, then the second, and so on until eventually the Ram must be checked

A Cache hit is when the CPU finds what is needed from the Cache rather than searching for it in the RAM, a Cache Miss is the opposite. Programers build their programs to have more Cache hits than misses as that speeds up the program 