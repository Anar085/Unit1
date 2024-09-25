# Project Unit 1 : A simple currency converter
## Criterion A: Planning

## Problem definition: 
I have been hired by Ms.Kubato, a school teacher who is in charge of school computers. These computers are both for use of teachers and students, and they contain software applications for only teacher use. In that school, teachers use 8 different software applications to record participation of students, to make assessments, and to prepare exam questions. Of course, these kind of apps should be limited for only teacher use, and these software apps are locked to prevent student use, but each of those applications has distinct passwords for safety reasons (foreseeing the case of revealing one of the passwords). Now, the problem is that not all teachers know the passwords for all locked applications and a challenge we face if one teacher changes the password, other teachers will not be able to know the password and access the software applications. Additionally, saving those passwords to unprotected place can cause unpreventable problem. My client is concerned about having not safe and sustainable e-school system .

## Proposed Solution:
I am proposing, to resolve this problem,  to create a currency converter (which is very unattractive software application for student use) which contains a secret function that is only revealed when a hidden code is entered. Once the correct code is typed into the currency converter, it transforms into the password manager that Ms. Kubota requires. This is an  adequate solution for that teacher as it solves the problem or keeping password information both protected and hidden.

To create computer applications that can run on the terminal some options are Visual basic, python, C or etc.
I proposed to use Python because it is multi-platform, meaning that can be used in any device (Windows, MacOs, etc) .
Additionally, Python's cross-platform compatibility ensures that the application can be used by teachers on various devices without requiring significant modifications.
My client also require permanent storage, so to solve this requirement I proposed to use a simple .csv file in contrast to a full fledge database. This is an adequate option because it is light weight. The .csv file is also a suitable option because it is a simple text-based format that is easy to read, write, and understand. This makes it easier to manage and edit the stored data if necessary. Additionally, .csv files are widely supported by various software applications, ensuring compatibility with different tools that teachers might use to access and manage their passwords.

[1] Guido , Real Python, "Why python is the best" 2024. (MLA reference)

## Success criteria:
1. Basic Currency Converter Functionality:
    The currency converter is capable of converting between 5 currencies.
   **[ISSUE TACKLED]**: `The currency converter functions as expected, providing accurate conversions.`
1. If the user enters the secret code ("uniqueschool2024") as an amount for converting, the program will change modes and act as a password manager.
    **[ISSUE TACKLED]**: `The secret code effectively triggers the hidden functionality.`
1. In password manager mode, the user should be able to perform CVUDG operations (Create, View, Update, Delete, Generate):
   * Add a password (for a software application).
   * View the stored passwords (only if they re-enter the secret code).
     **[ISSUE TACKLED]**: `The password manager allows for complete management of stored passwords`
1. Save passwords permanently and store them encrypted
    **[ISSUE TACKLED]**: `The .csv file provides a certain level of security for storing sensitive information`
1. Use the terminal to interact with the user.
    **[ISSUE TACKLED]**: `The terminal interface simplifies the application's use and accessibility`


# Criterion B: Design
### System Diagram
![image](https://github.com/user-attachments/assets/82d4bbea-9973-41dc-b0ba-20ed9978c34e)

**Fig 1** System Diagram showing the minimal requirement for the hardware and software used for
proposed solution. The lock indicates encryption.



### Flow diagrams for algorithms
![image](https://github.com/user-attachments/assets/8a54209d-3035-45c5-a207-24cc507940b1)
**Fig. 2** This is the flow diagram for the algorithm used in convercy converter.
![image](https://github.com/user-attachments/assets/e82b41ab-18fe-4415-8e27-5ef2b6dc3f24)
**Fig. 3** This is the flow diagram for the algorithm used in password manager.
![image](https://github.com/user-attachments/assets/c2c2f9a7-75e5-4a94-a878-15df420ab5c9)

**Fig. 4** This is the flow diagram for the algorithm used in "remove" operation.



### Data storage
![image](https://github.com/user-attachments/assets/97bb39b3-5f00-4b83-a370-813eb7f7c2fe)

**Fig. 5**I am proposing to use .csv file to store the encrytped information as CSV files are a simple and widely used format for storing tabular data. They are essentially text files where data is separated by commas, making them easy to read, write, and understand by both humans and computers. This simplicity makes it easier to manage and edit the stored data if necessary. Additionally, .csv files are widely supported by various software applications, ensuring compatibility with different tools that teachers might use to access and manage their passwords. These are the reasons for choosing .csv file.
### Sketches of the application (wireframe diagrams)
![image](https://github.com/user-attachments/assets/5d244887-32f6-43aa-a06c-95f568235bbc)

### Test plan
| Test Case | Test Description                                                                                                       | Expected Result                                                                 | Pass/Error |
|-----------|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|------------|
| 1         | Enter an invalid currency code (e.g., "EUD")  for the "from" and "to" currency.                                        | Display an error message  indicating invalid currency.                          | Pass       |
| 2         | Enter an lowercase currency code  (e.g., "usd") for the "from" and "to" currency.                                      | Display an error message indicating  only typing options are in upper case      | Pass       |
| 3         | Enter an input unrelated to currency codes (e.g., "money")  for the "from" and "to" currency.                          | Display an error message indicating invalid currency.                           | Pass       |
| 4         | Enter an amount with both numeric and non-numeric characters  (e.g., "100abc") for the amount to convert.              | Display an error message indicating invalid amount.                             | Pass       |
| 5         | Enter an amount with multiple decimal points  (e.g., "10.12.13") for the amount to convert.                            | Display an error message  indicating invalid amount.                            | Pass       |
| 6         | Enter an amount with only non-numeric characters  (e.g., "abc.abc") for the amount to convert.                         | Display an error message  indicating invalid amount.                            | Pass       |
| 7         | Enter the secret code "unique" for the amount to convert.                                                              | Switch to password manager mode.                                                | Pass       |
| 8         | Enter a number out of range(1-6)  (e.g., "15") for the operation to perform.                                           | Display an error message  indicating invalid operation number.                  | Pass       |
| 9         | Enter a number in a range(1-6)  (e.g., "5") for the operation to perform.                                              | Properly functions the operation  and asks for an app number                    | Pass       |
| 10        | Enter an input with non-numeric symbols  (e.g., "23wfjw.9?") for the operation number to perform.                      | Display an error message  indicating invalid operation number.                  | Pass       |
| 11        | Enter a number out of range(1-8(length of app list))  (e.g., "15") for the app number to perform a selected operation. | Display an error message  indicating invalid app number.                        | Pass       |
| 12        | Enter a number in a range(1-8(length of app list))  (e.g., "5") for the app number to perform a selected operation.    | Properly operates with selected  application                                    | Pass       |
| 13        | Enter an input with non-numeric symbols (e.g., "1.rt45?") for the app number to perform a selected operation.          | Display an error message  indicating invalid app number.                        | Pass       |
| 14        | Enter an existing app name for adding to the password manager                                                          | Display an error message indicating that the app is in already password manager | Pass       |
### Record of Tasks
| Task number | Planned action                                                                                      | Planned outcome                                                                                  | Time estimated | Target completion date | Criterion |
|-------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------|------------------------|-----------|
| 1           | 1st Meeting with the client                                                                         | Obtaining a problem definition, understanding what the situation is                              | 20 min         | September 7            | A         |
| 2           | Presenting my draft solution to the client                                                          | Discussing success criterions and getting confirmation                                           | 30 min         | September 10           | A         |
| 3           | Creating system diagram and sharing with the client                                                 | Letting my customer know hardware and software requirements and limitations of my solution       | 1 hour         | September 12           | B         |
| 4           | Creating wireframe diagrams and data storage and predicting  potential needs                        | Establish a solid foundation for the development process and  ensuring a more successful outcome | 3 hours        | September 14           | B         |
| 5           | Creating 3 flow charts for Currency Converter,  Password Manager , and one of the operations in PM  | Getting deeper understanding of how the algorithms of my program work                            | 3 hour         | September 15           | B         |
| 6           | Designing the user interface (UI) for the currency converter                                        | Having a visually appealing and intuitive UI for currency conversion                             | 2 hours        | September 16           | C         |
| 7           | Developing the currency conversion algorithm                                                        | Accurate calculations for various currency pairs                                                 | 4 hours        | September 17           | C         |
| 8           | Implementing the secret code functionality                                                          | Triggering the password manager mode when the correct code is entered                            | 2 hours        | September 18           | C         |
| 9           | Design the password manager UI                                                                      | A user-friendly interface for managing passwords                                                 | 1 hour         | September 19           | C         |
| 10          | Develop password management functionalities (CVUDG)                                                 | Ability to create, view, update, delete, and generate passwords                                     | 6 hours        | September 20           | C         |
| 11          | Implement password encryption for storage                                                           | Passwords are stored securely in the CSV file                                                    | 3 hours        | September 21           | C         |
| 12          | Develop user interface for interacting with the application                                         | So user can interact with the program through clear prompts and menus                            | 1 hour         | September 22           | C         |
| 13          | Unit test the individual functionalities                                                            | Ensure each part of the program works as expected                                                | 2 hours        | September 23           | B         |
| 14          | Integrate all functionalities and conduct system testing                                            | The entire application functions properly                                                        | 1 hour         | September 24           | B         |
| 15          | Prepare user manual                                                                                 | Users can easily understand how to use the application                                           | 30 minutes     | September 24           | B         |
| 16          | Conduct final review with Ms. Kubota                                                                | Ensure the application meets her needs and expectations                                          | 45 minutes     | September 25           | A         |
