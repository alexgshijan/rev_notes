**Every single character have their own binary code.**
These codes are determined by the **character set** the computer is using to interpret the key press. Do you know of any character sets?
There are 3 main sets to know about: **ASCII, EBCDIC** and **Unicode**

**ASCII :**
Stands for “American Standard Code for Information Interchange”
Each character on the keyboard is represented and has a code
There is a standard set where each code is 7 bits of binary…
And an extended set where the codes are 8 binary bits
Example: 
	*A* = 01000001 
	*ESC key* = 00011011
[[Screenshot 2023-11-17 at 09.23.15.png|Ascii Table]]

**EBCDIC :**
Stands for “Extended Binary Coded Decimal Interchange Code”
Used in older business mainframes (central server)
Preferred for business where a lot of data is processed
Can’t directly communicate with a computer using ASCII, needs to be translated

**Unicode and UCS – ISO 10646 :**
UCS stands for unified character set
Many languages use different letters or symbols.
A much bigger set than ASCII is needed. 8-bit ASCII has 256 different codes
ISO 10646 uses 31 bits and allows for 2 billion codes
Unicode is a small subset of this which uses 16 bits to give around 65000 codes
Unicode and UCS are different, but generally they are considered interchangeably
Unicode incorporates ASCII