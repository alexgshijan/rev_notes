When a database file is created, records and fields can be given either a *variable* or *fixed* length.
Regardless of the allocated length, the record or field will use up all the allocated space

**Fixed Length :**
- Each field/record has a set length which is given when the file is made 
- The size of a record can be easily calculated 
- Each item is easier to search for/access, because their locations can be calculated
- Potential for a lot of wasted memory space

**Variable Length :**
- The length of the data does not need to be pre-defined 
- Good for when there is an unknown or wide range of possible data items
- Saves space (no space wasted with empty records/files)
- However it's harder to read/ write to.