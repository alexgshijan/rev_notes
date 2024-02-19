Classes are templates for modelling objects, they contain associated attributes and methods. *When you make a new object, you create an “instance” – a variable which stores all of the data for that object*

Objects are versions of the class which can be created (instanced) and interacted with. The methods in a class can be called like a normal function, and exist to manipulate the attributes (variables) in the class.

| Name | **Car** | **Employee** |
| ---- | ---- | ---- |
| Variable:DataType | Make:String<br>Model:String <br>RegNum:String <br>Speed: Int | NINumber:String<br>Name:string<br>DOB:string |
| Method(Parameters) | changeSpeed(newSpeed:int)<br>turnLeft()<br>turnRight() | EnterDetails(NI:string, Name:string, DoB:string)<br>ShowDetails() |

*Promotes reusable (modular) code and well organised, neater structure than simple procedural. However, difficult for beginner programmers to learn and relationships between classes can become confusing and complex in large systems*

**Encapsulation**
*All data in the program belongs to a class rather than floating around as independent data*. This makes things more organised – we can have multiple car objects with its associated attributes and methods with little difficulty. 

It also means that functionality and data can be hidden from the user, *access to important variables can be somewhat restricted* to protect them from unwanted change. Variables can be set as private, with public methods in order to manipulate those variables.

**Attributes**
Classes can pass down attributes and methods to other “child” classes. *These child classes are also known as subclasses.* Essentially the superclass has a set of methods and variables that all the subclass inherit, these subclasses might have their own unique set of methods and variables too.

