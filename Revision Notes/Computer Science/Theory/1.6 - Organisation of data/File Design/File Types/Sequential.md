**A serial file which is sorted in some fashion (e.g. alphabetical or numerical order)**
This is faster than [[Serial]] 

*To add to the sequential file new records need to be added at the correct location.  As records must be in key order, a new copy is made of the file.*
Records are copied across from the old to the new.  When the point is reached for the new record, it is added to the copy.  Then the remainder of the records on the old copy is copied to the new copy. 

*Likewise when a record is to be deleted, a copy is made of the file, one record at a time, with the record to be deleted simply not being copied across*