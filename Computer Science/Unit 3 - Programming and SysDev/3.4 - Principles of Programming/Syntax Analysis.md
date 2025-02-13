**During syntax analysis, the computer must check through the string of tokens that has been created. BNF and syntax diagrams can be used to represent the rules that syntax has to follow and show how it is defined in a programming language*

| BNF Notation           | Meaning                                               |
| ---------------------- | ----------------------------------------------------- |
| < >                    | Encloses each element that can be broken down further |
| ::=                    | Defines the rule for a previous element               |
| \|                     | User to indicate OR                                   |
| < x > ::= a \| < x > a | recursion, allows a user to add infinitely as needed  |

**Syntax Diagrams**
Rectangle - Represent a non terminal element 
Oval - Represent a terminal element
Rectangle with arrow from end to start - Represents a non terminal that can be recursively used.