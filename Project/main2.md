# Project Unit 1 : A simple currency converter
## Criterion A: Planning

## Problem definition: 
I have been hired by Ms.Kubato, a school teacher who is in charge of school computers. These computers are both for use of teachers and students, and they contain software applications for only teacher use. In that school, teachers use 8 different software applications to record participation of students, to make assessments, and to prepare exam questions. Of course, these kind of apps should be limited for only teacher use, and these software apps are locked to prevent student use, but each of those applications has distinct passwords for safety reasons (foreseeing the case of revealing one of the passwords). Now, the problem is that not all teachers know the passwords for all locked applications and a challenge we face if one teacher changes the password, other teachers will not be able to know the password and access the software applications. Additionally, saving those passwords to unprotected place can cause unpreventable problem. My client is concerned about having not safe and sustainable e-school system .

## Proposed Solution:
I am proposing, to resolve this problem,  to create a currency converter (which is very unattractive software application for student use) which contains a secret function that is only revealed when a hidden code is entered. Once the correct code is typed into the currency converter, it transforms into the password manager that Ms. Kubota requires. This is an  adequate solution for that teacher as it solves the problem or keeping password information both protected and hidden.

To create computer applications that can run on the terminal some options are Visual basic, python, C or etc.
I proposed to use Python because it is multi-platform, meaning that can be used in any device (Windows, MacOs, etc) .
Additionally, Python's cross-platform compatibility ensures that the application can be used by teachers on various devices without requiring significant modifications.
My client also require permanent storage, so to solve this requirement I proposed to use a simple .csv file in contrast to a full fledge database. This is an adequate option because it is light weight ...

[1] Guido , Real Python, "Why python is the best" 2024. (MLA reference)

## Success criteria:
1. Basic Currency Converter Functionality:
    The currency converter is capable of converting between 5 currencies.
   **[ISSUE TACKLED]**: `The currency converter functions as expected, providing accurate conversions.`
1. If the user enters the secret code ("uniqueschool2024") as an amount for converting, the program will change modes and act as a password manager.
    **[ISSUE TACKLED]**: `The secret code effectively triggers the hidden functionality.
`
1. In password manager mode, the user should be able to perform CRUD operations (Create, Replace, Update, Delete):
   * Add a password (for a website).
   * View the stored passwords (only if they re-enter the secret code).
     **[ISSUE TACKLED]**: `The password manager allows for complete management of stored passwords`
1. Save passwords permanently and store them encrypted
    **[ISSUE TACKLED]**: `The .csv file provides a certain level of security for storing sensitive information`
1. Use the terminal to interact with the user.
    **[ISSUE TACKLED]**: `The terminal interface simplifies the application's use and accessibility`


# Criterion B: Design
### System Diagram
**Fig 1** System Diagram showing the minimal requirement for the hardware and software used for
proposed solution. The lock indicates encryption.



### Flow diagrams for algorithms

**Fig. 1** This is the flow diagram for the algorithm used to search in the data file...

### Data storage

### Sketches of the application (wireframe diagrams)

### Test plan

### Record of Tasks
| Task number | Planned action                                      | Planned outcome                                                                            | Time estimated | Target completion date | Criterion |
|-------------|-----------------------------------------------------|--------------------------------------------------------------------------------------------|----------------|------------------------|-----------|
| 1           | 1st Meeting with the client                         | Obtaining a problem definition, understanding what the situation is                        | 20 min         | September 7            | A         |
| 2           | Presenting my solution to the client                | Discussing success criterions and getting confirmation                                     | 30 min         | September 10           | A         |
| 3           | Creating system diagram and sharing with the client | Letting my customer know hardware and software requirements and limitations of my solution | 1 hour         | September 12           | B         |
| 4           |                                                     |                                                                                            |                |                        |           |
| 5           |                                                     |                                                                                            |                |                        |           |
| 6           |                                                     |                                                                                            |                |                        |           |
| 7           |                                                     |                                                                                            |                |                        |           |
| 8           |                                                     |                                                                                            |                |                        |           |
