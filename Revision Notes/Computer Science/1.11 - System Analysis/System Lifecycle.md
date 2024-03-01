*Systems life cycle – problem definition*
**Is there a problem with the current system, or are there problems that an entirely new system could solve?**
The customer might think they know what they want, but chances are this is quite vague. The systems analyst needs to clearly establish what the problems are and what they new system could do to solve them. At this stage, the *scope* of the problem will be laid out. This will say exactly what the new system should do when complete, and how it will solve the perceived problems of the customer.

*Feasibility Study*
Economic:
- The project will have a limited budget
- Costs such as maintenance, salaries, hardware and software
- Profit turnover
Time:
- Can the project realistically be done on time?
- What different factors need to be taken into consideration at this stage?
Technical:
- Are the resources available sufficient for completing the project? 
- Are the developers who work for the company taking on the project skilled in the necessary areas?
Political:
- What is the proposed project includes aspects that are politically sensitive? 
- For example, any system relating to the NHS, prison service, HMRC, animal testing, or self driving cars could lead to divisive opinion and bad publicity if things go wrong
Legal:
- New systems must comply with the laws of the country or countries it will be released in
- This starts with data protection laws but can include a whole host of different legislation depending on what the system is for

*Investigation and Analysis*
Observation
- Analyst shadowing employees to make notes on how they do their job in their natural environment to see how the business works.
Questionnaire
- Allows analyst to get a large quantity of data from lots of employees. 
- Faster than observing or interviewing every single employee at a company if it’s a big organisation
Interview 
- Good place to start with analysis – typically done with a few of the key stakeholders. Allows for collection of detailed, accurate information
Document Collection 
- Gathering of business related documents such as invoices, orders, financial records, memos
- Good way to examine the sorts of data the new system will handle

*Abstraction*
- This is the idea of having generalised solutions to a variety of specific problems
- “The meaning behind the idea must be separated from the details of how it will work or be implemented”
- Control Abstraction - Hiding complex functions behind call phrases to simplify code construction
- Data Abstraction - Hiding actual data and variables behind call phrases to simplify code construction 
*Decomposition*
- This is the process of breaking problems down into separate parts to solve each part individually 
- This also involves producing diagrams to represent the different individual parts of a system and how they relate to one another, including entity relationship diagrams (ERDs), data flow diagrams (DFDs) and flowcharts.

*Build and Testing*
White Box
- Used for testing the structure of the code. There will be multiple paths a program can take (when using if statements for example) and each of these must be tested 
- It is called “white box” because the testers are aware of what the code looks like. Often this means it’s the developers themselves who perform this type of testing
Black Box
- Here the functionality of the program is tested based on the requirements specification. No paths are examined here – this is just for testing that the overall code does what it should!
- This is usually done by people other than the developers who were not involved in making the system, so they have no idea what the code looks like
Alpha
- Always carried out by developers and “in house” teams
- Unstable, lacking functionality 
- Takes place in early and mid-term development stages
Beta
- Happens later on in development when the product is closer to finished and is more stable (less likely to crash)
- Given to a select group of customers to test. 
- Useful for finding bugs the developers may not have come across
End User
- This is the final testing phase. 
- The person/people who will be using the system when it is finished test it as if they were using it normally 
- Checks that the developer has produced a system which meets the need of the customer

*Changeover*
Direct - Also referred to as “Big bang” changeover, this is where the old system is instantly shut off/discarded and replaced with the new one
- Not as expensive
- Can't be used while shutdown
- If system doesn't work, you are unable to use old system
- Users can't get acclimated to the system
- Quick Process

Phased - With this method, smaller parts of the system are replaced a little bit at a time.
- The system adoption approach can be more tailored to the requirements 
- The old system and new system may not be able to integrate nicely

Pilot - When businesses (especially larger ones) are split up over several sites, one site could trial the new system before it is distributed to the rest of the company’s sites
- Can be tested at one site, so it doesn't shut down all the sites.
- Communication between sites using old and new system may be hard 

Parallel - In this case both systems run simultaneously, side by side.
- More Robust
- More Expensive + Time Consuming

*Documentation*
User Documentation 
- Step-by-step getting started guide 
- Installation guide
- General user guide 
- Reference manual 
- Online help 
- Error help/troubleshooting guide
- FAQs
- Glossary of terms

Maintenance Documentation 
- Diagrams used in analysis and design 
- Data structure descriptions/tables 
- Algorithm designs 
- Annotated code listings
- Variable lists 
- Data dictionary (description of data fields and their types, size etc.)
- Hardware & software requirements 
- Configuration guide and options

*Maintenance*
Usually a plan of maintenance provided by the developer after the launch of the new system will be agreed upon as part of the contract. This might be a set period of time after implementation during which the developer fixes problems for free, or alternatively on a “pay as you go” basis

Adaptive
- This is where bugs are fixed and extra functionality is added to the system. 
- Systems might come in different versions, with companies starting with the basic package and upgrading later on.

Corrective
- This is where problems are reasonably likely to occur and are fixed when they come up. The aim is to provide a system that matches the original specification as closely as possible. This often corresponds with a maintenance contract between the business and the developer.

Perfective
- Like corrective maintenance, but here the idea is for the system to **exactly** match the specification with no problems whatsoever.  
- This is expensive and time consuming but is necessary in certain systems such as safety critical systems (air traffic control, nuclear power facilities etc)

*Evaluation*
Requirements - Does it meet the functionality set out in the requirements specification?
Performance - Does it respond in a timely manner for the user?
Robustness - Does the software often crash or encounter bugs?
Cost - Did the project go over-budget at all?
Usability - Is the project usable by the end user?