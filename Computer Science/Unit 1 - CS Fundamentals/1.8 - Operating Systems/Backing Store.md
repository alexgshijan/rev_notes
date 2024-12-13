FAT *“File Allocation Table”* and NTFS *“New Technology Filing System”* are both methods of storing the locations of files on secondary storage devices.

FAT also has to store meta-data about the file, including:
- File name 
- Creation date/modified date
- Start sector of the file (address with the first sector)
- File access rights (who can view/edit)
- Size of the file

The FAT stores the sector which contains the start of the file. A data structure called a “linked list” is then used. This stores the locations of each of the remaining parts of the file.  

A linked list is made up of “nodes”, which have an address, some data, and a pointer to the next part of the list. They are useful for files which are split up over different part of a disk rather than altogether in a cluster.

*however* NTFS can store files larger than 4GB which FAT and uses more advanced data structures, the read/write times are faster aswell

![[Pasted image 20240126120422.png]]