**An algorithm is applied to the data which generates a hash key. This acts as a kind of index number and must be unique for each record. When a query is made, a hash is made from the query that directs it straight to the needed value**. This is the fastest method

*This is by far the quickest method, but also the most complex & hardest to implement*
The idea here is that a “hashing algorithm” is used on an item the data itself- usually a key field like an ID or name to give an index value. This value represents the physical location of where the data will be stored (or found if you’re searching for the data)
Data that will be stored is known as the “hash key”. 
It is quicker to search by applying the algorithm to the search term than it is to search through the hash keys linearly

Extremely fast access thanks to non-sequential searching, however can lead to collisions if the same value is generated for multiple data items, could potentially lead to memory redundancy if data is spread too far apart. If the hashing algorithm is too complicated, it could take too long to process

**Overflow :**
- One way of dealing with collision is to use an overflow area
- These are basically just areas of unorganised memory where things are put temporarily, like a serial file
- And like a serial file, they come with all of the drawbacks in terms of poor efficiency and slow search/access times 
- When these overflow areas become too big they need to be reorganised. This might involve recreating the whole structure using a new hashing algorithm (known as rehashing)