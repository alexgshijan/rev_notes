*Data structure which uses a hashing algorithm/formula on the data itself to determine where a data item should be stored.* Hash tables consist of two parts: an array with an associated hash function/algorithm. The hash function takes a piece of data known as a key and generates a hash value; this is used as the index in the array.

The algorithm is specifically applied to one item of the data in a record, which is known as the “hash key”. This is usually the unique identifier field, but could be any of them. *It is quicker to search by applying the algorithm to the search term than it is to search through the indexes linearly (or sequentially)*

*Pros*
- Extremely fast access thanks to non-sequential (random/direct) searching
- Can be an efficient use of storage space if the algorithm is well designed

*Cons*
- Can lead to collisions
- Could potentially lead to memory redundancy if data is spread too far apart
- If the hashing algorithm is too complicated, it could take too long to process!
- Hashing algorithms have to be well designed, or the gains from direct access will be lost

**Solutions to Collisions**
*Rehashing - Best Solution*
- Apply a different/backup hashing algorithm to data to produce a unique hash code
- Or re-do the original to get an algorithm which generates a better range of indexes
*Daisy Chain - 2nd Best*
- If there is a collision, use a linked list at that location to store all of the keys that share the code
*Linear Probing - 3rd Best*
- If our hash code is taken, search in a linear fashion until we find the next free one
*Overflow Areas - Worst*
- Set aside a special area (collection of hash codes) which can be used in the case of a collision
- Had to be accessed linearly, so defeats the point of the more efficient access