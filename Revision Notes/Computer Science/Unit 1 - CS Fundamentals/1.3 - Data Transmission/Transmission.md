*Methods of Transmission*
Simplex :
- With this method, data only travels in one direction meaning that no return packets are allowed
- Traditional satellite connections for TVs (not connected to the internet) use simplex mode as satellite dishes only receive data, they don’t send anything back

Half-duplex and duplex :
- These methods use separate cables to send data back and forth. 
- A twisted pair cable such as a CAT5 Ethernet cable might have two pairs for uploading and two for downloading so that packets travelling in opposite directions don’t interfere with each other
- *Half duplex makes full use of all cables when transmitting data, but flow can switch direction based on communication needed.
- *Full duplex allows for transmission in both directions simultaneously* 
- As packets can travel in either direction along the same line, sometimes there are collisions when two packets are sent along the same line in different directions. We could mitigate this by : 
	- Devices should wait a random amount of time before sending the packets again if using the same line
	- Use a priorities policy, perhaps where one machine is chosen to always send their data first or
	- You could implement a round-robin style system where each PC takes turns to send their packets

*Mode of Transmission*
Parallel Transmission :
- **All of the bits in a byte are sent along several wires simultaneously.** The cable that connects these transmissions consists of many wires (usually multiples of 8) 
- This is generally used over short distances. This is because it is difficult to keep voltages on the eight wires in line with each other after a certain distance. This problem is known as **skewing**.
- Faster than Serial Transmission 

Serial Transmission :
- **Serial data transmission is when single bits are sent one after the other along a single wire**
- Examples of where this is used include under sea cable and telephone wires 
- Serial transmission is used in long-distance communication because the signal going along a single pathway is not susceptible to skew

Multiplexing
**This process involves taking several data streams and combining them to send them across a single wire (mux)** When the data reaches it’s destination, the single stream is split back up into the original separate streams (demux)
*You can also reverse this process – this is known as inverse multiplexing*

It could save on costs, with less wires/cables needing to be installed 
Good for linking serial and parallel transmissions 
It could also increase transfer speeds in some circumstances

**Examples :**
- Telephone calls, where multiple calls between different people in an area are combined and sent across a network
- Television/radio broadcasts, where multiple different stations' output signals can be combined in order to be transmitted across the country, then split up into the different channels at the destination