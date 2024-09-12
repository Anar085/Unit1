# Project Unit 1 : A simple currency converter
## Criterion A: Planning

## Problem definition: 
I have been hired by a school teacher who is in charge of school computers. These computers are also for usa of teachers and they contain software applications for only teacher use. These software apps are locked to prevent student use. In that school, teachers use 8 different software applications to record participation of students, to make assessments, and to prepare exam questions. Of course, these kind of apps should be limited for only teacher use, but each of those applications has distinct passwords for safety reasons (in case of revealing one of the passwords). Now, the problem is that not all teachers know the passwords for all locked applications and a challenge we face is that some older teachers often forget the required app passwords. Additionally, saving those passwords to unprotected place can cause unpreventable problem. My client is concerned about having not safe and sustainable e-school system  (** See the evidence of the consultation in the Appendix **).

## Proposed Solution:
I am proposing, to resolve this problem,  to create a currency converter (which is very unattractive software application for student use) which contains a secret function that is only revealed when a hidden code is entered. Once the correct code is typed into the currency converter, it transforms into the password manager that the teacher requires. This is an  adequate solution for that teacher as it solves the problem or keeping password information both protected and hidden.

## Success criteria:
1. Basic Currency Converter Functionality:
   The currency converter should accept user input to perform basic operations (addition, subtraction, multiplication, division).
Ensure it can handle typical errors (e.g., division by zero) and give appropriate feedback.
Hidden Functionality:
If the user enters the secret code ("open123"), the program will change modes and act as a password manager.
In password manager mode, the user should be able to:
Add a password (for example, for a website).
View the stored passwords (only if they re-enter the secret code).
Optionally, display the passwords in a "masked" form (e.g., showing only the first and last characters).
Basic Security Features:
Store passwords in a text file.
HL: Implement a basic obfuscation technique or basic encryption (e.g., reversing the password string or shifting characters by a fixed number) 
User Interaction:
Use the terminal to interact with the user.
