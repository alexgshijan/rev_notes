**Master file :**
- Permanent file for a system which keeps an ongoing track of information. E.g. a shop has a master file of products and what is in stock. This will contain the most up-to-date /valid version of the data

**Transaction file :** *There are 'delimiters' or special characters split records*
- A temporary file for a small period of time (perhaps a day) where *changes* are logged. After a time, the transaction file is used to update the master and emptied
- In the shop example, each till could keep a transaction file which would then be merged with the master file at the end of the day 

*Why not just edit the master file ?*
Could cause data inconsistency if two or more people accessed the same file at the same time
It could also take a long time to edit the master file as it could be a huge file

*An extension of using master and transaction files is using generations of files.* An example of this is the “grandfather-father-son” system. 

**File backup** *is copying data from one place to another.*
The copy could then be used to restore data if data were to be lost.

**File Archiving** *is the process of moving old files to a separate system in order to speed up the main one.*
On most systems, routine clearouts will get rid of old or unnecessary files to save space on the system. However, some files will be considered too important to delete and they are saved. These files will build up over time however, taking up space on the system
