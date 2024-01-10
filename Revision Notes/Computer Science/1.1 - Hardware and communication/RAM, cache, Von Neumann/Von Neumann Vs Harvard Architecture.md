Stores Program concept : 
- As we’ve stated, programs must be in the main memory (RAM) before they can be properly run 
- This is known as the “stored program concept”, and it was masterminded by Alan Turing and John Von Neumann
- Von Neumann gives his name to a type of PC architecture which is the most commonly used today

Von Neumann architecture : 
- **All instructions and data that the instructions use are in the same memory**
- A single processor is used. The same memory stores instructions and data, and programs are executed by doing one instruction after the next with the fetch-decode-execute cycle
- A Von Neumann computer would not be able to tell if a bit pattern (like 0000111010101) was data, instructions or a combination of the two
- Whilst this architecture is the most commonly used, it has a major drawback known as the Von Neumann bottleneck 
- Whatever improvements are made to the clock speed, there is no escaping the fact that because data and instructions are stored in the same place, the CPU will spend time waiting for data retrieval
	- [[RAM vs Cache|Cache]] does provide some solution to this, because it allows the recently & frequently used data & instructions to sit closer to the CPU in faster access memory, so that it doesn’t always have to wait for the slower RAM

Harvard : 
- One alternative is the Harvard architecture which uses a separate memory for instructions and data, meaning that both can be retrieved at the same time
- This generally means less waiting around. This approach is used in [[Processor Variations|RISC]] processors 