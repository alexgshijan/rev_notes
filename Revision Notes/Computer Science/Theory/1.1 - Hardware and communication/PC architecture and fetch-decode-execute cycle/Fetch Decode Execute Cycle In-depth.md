- Instructions are fetched from main memory (RAM), decoded to see what needs to be done and executed (carried out) 
- The program counter (PC) register in the CPU keeps track of the current instruction number.  This increases by 1 (increments) during the fetch phase so that it will point to the next instruction. 
- This PC register value is then sent to be stored in the memory address register (MAR).
- The CPU sends the address of the next instruction to be fetched along the address bus at the start of the cycle.
- When the instruction is fetched, it is sent along the data bus, and held in the current instruction register (CIR) . 
- The address that the instruction involves (e.g. load from address 99) is held in the memory address register (MAR).
- Takes a copy of the CIR, then the data involved in the instruction (e.g. the data loaded from address 99) is held in the memory data register (MDR).

*Note : Throughout this process, the accumulator register holds data values of whatever the CPU is working on*
The speed of this process is determined by the clock speed on the CPU  The process starts as soon as the computer is turned on, and doesn’t stop until the computer is turned off. 
