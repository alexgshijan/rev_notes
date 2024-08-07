Entities : **Significant objects, people, places or events in a system** 
Attributes : **Additional data attached to each entity,  can be stored and analysed in some way**

Entity relationship diagrams (ERDs) can be used to model real world systems, showing their entities, attributes and how the entities relate to one another

Relationships are how *entities interact or relate to each other* within the system (real and virtual). These relationships can be “one to one”, “one to many” or “many to many”.

*Note in a one to many relationship, a UID of the 'one' would be attached to each of the 'many' entities*

**Examples :**
1. One Team has many players - *Note these lines represent many to one*
	![[Screenshot 2024-01-10 at 11.44.00.png]]
2. One Team has many players - *Note attributes also specified*
	![[Screenshot 2024-01-10 at 11.45.45.png]]
3. One Team has a manager - *Note a manager comes under the Team*
	![[Screenshot 2024-01-10 at 11.53.38.png]]
4. A football team is made up of a number of players, each of which plays for a single team at any one time. These teams play at a number of stadiums during a season. Each team has a manager who is only allowed to manage one club at a time. - *Note combine ERDs*
	![[Screenshot 2024-01-10 at 12.02.49.png]]

**Data redundancy and data inconsistencies are an issue when working with large data bases.**
A method of dealing with that is by using link tables to turn a many-to-many relation into a one-to-many *link table* many-to-one
