Simplex :
- With this method, data only travels in one direction meaning that no return packets are allowed
- Traditional satellite connections for TVs (not connected to the internet) use simplex mode as satellite dishes only receive data, they don’t send anything back

Half-duplex and duplex :
- These methods use separate cables to send data back and forth. 
- A twisted pair cable such as a CAT5 Ethernet cable might have two pairs for uploading and two for downloading so that packets travelling in opposite directions don’t interfere with each other
- *Half duplex makes full use of all cables when transmitting data, but flow can switch direction based on communication needed.
- *Full duplex allows for transmission in both directions simultaneously* 
- As packets can travel in either direction along the same line, sometimes there are collisions when two packets are sent along the same line in different directions. We could mitigate this by : 
	- Devices should wait a random (why random?) amount of time before sending the packets again if using the same line
	- Use a priorities policy, perhaps where one machine is chosen to always send their data first or
	- You could implement a round-robin style system where each PC takes turns to send their packets

Multiplexing :
- This process involves taking several data streams and combining them to send them across a single wire (mux)
- When the data reaches it’s destination, the single stream is split back up into the original separate streams (demux)
- You can also reverse this process – this is known as inverse multiplexing 
- It could save on costs, with less wires/cables needing to be installed 
- Good for linking serial and parallel transmissions 
- It could also increase transfer speeds in some circumstances
- Can you think of any examples of where it might be used?