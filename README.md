# Registration Group Project

## OBJECTIVES:
- How to work within a team to create a Python program
- How to create modules and functions
- How to pass data from one function to another
- How to store data in lists and dictionaries
- How to create and use selection control structures
- How to create and use iterative control structures
- How to add comments to Python code

## GOALS:
- Work in teams to create Python programs
- Create modules and functions
- Pass data from one function to another
- Store data in lists and dictionaries
- Create and use selection control structures
- Create and use iterative control structures
- Add comments to Python code

## PROJECT DESCRIPTION
You have learned quite a lot about the basics of Python programming.  In this project, you will integrate what you have learned to develop a larger program.
This program creates a class registration system.  Students log into the class registration system and then they can add courses, drop courses, and list the courses for which they have registered.
This program has 7 functions in 3 modules: a student module, a billing module, and a main module.

## PROGRAM SUBMISSION REQUIREMENTS

You must create three Python files: 
-	The student module named student.py
-	The billing module named billing.py
-	The main module named registration.py


## MODULES
### Module: student.py

Function: add_course(id, c_roster, c_max_size)	
This function adds a student to a course.  It has three parameters: 
-	id is the ID of the student to be added
-	c_roster is a dictionary of courses offered with their student rosters
-	c_max_size is a dictionary of maximum class sizes  

This function asks user to enter the course they want to add.  
-	If the course is not offered, display error message and return.  
-	If student already registered for the course, display error message and return. 
-	If the course is full, display error message and return. 
-	If all error conditions are avoided, add the student ID to the course’s roster and display a message.  

This function has no return value.  

Function: drop_course(id, c_roster)	This function drops a student from a course.  It has two parameters: 
-	id is the ID of the student to be dropped 
-	c_roster is a dictionary of courses offered with their student rosters
This function asks user to enter the course they want to drop.  
-	If the course is not offered, display error message and return.  
-	If the student is not enrolled in that course, display error message and return.  
-	If there is no problem, remove student ID from the course’s roster and display a message.  
This function has no return value.

Function: list_courses(id, c_roster)	This function displays and counts courses a student has registered for.  It has two parameters: 
-	id is the ID of the student
-	c_roster is a dictionary of courses offered with their student rosters
This function displays the number of courses the student has registered for and which courses they are.  This function has no return value.

### Module: billing.py

Functuion: calculate_hours_and_bill (id, s_in_state, c_rosters, c_hours)	This function calculates the course hours and cost of enrollment.  It has four parameters: 
-	id is the ID of the student 
-	s_in_state is a dictionary of in state students
-	c_rosters is a dictionary of class rosters
-	c_hours is a dictionary with the credit hours of each class 
This function calculates the bill based on $225 per credit hour for in-state students and $850 per credit hour for out-of-state students. After calculating the bill, the function returns the total number of credit hours and the total cost of enrollment.

Function: display_hours_and_bill(hours, cost)	This function displays the course hours and the cost of enrollment. It has two parameters:
-	hours is the number of course hours
-	cost is the total cost of enrollment
This function displays the total number of credit hours and the total cost of enrollment.
 
 
### Module: registration.py (main module)

Function: login(id, s_list)	This function allows a student to log in.  It has two parameters: 
-	id is the ID of the student
-	s_list, which is the student list
This function asks user to enter PIN. If the ID and PIN combination is in s_list, display message of verification and return True.  Otherwise, display error message and return False.

Function: main()	This function manages the whole registration system.  It has no parameter.  It creates lists and dictionaries to store data: student list, in-state students, courses and hours, maximum class size list and roster list.  It uses a loop to serve multiple students.  Inside the loop, ask user to enter ID, and call the login function to verify student’s identity.  If login is successful, use a loop to allow a student to choose to add courses, drop courses or list courses the student has registered for or if they want to display a bill. This function has no return value.
 
## DEVIATIONS FROM PROJECT SPECIFICATION

Some deviation or creativity MAY be considered with the following guidelines:
-	Any program differences from this specification should be proposed to the instructor via email at least 1 week before the project submission deadline for approval. 
-	The change proposal should be at least 3 sentences that describe the desired change, the reason for changing, and the expected learning outcome.
-	The instructor reserves the right to NOT approve specification change requests, however a decision will be rendered within 48 hours of the request. As the primary stakeholder, the decision of the instructor is final.
-	Proposed and approved changes to the program that are subsequently implemented may enable students to receive up to 25 additional extra credit points to be added to the project grade.
-	Any extra credit awarded will be based on the amount of additional work beyond the original assignment, the utility of the improvements to the course registration system, and the level of innovation or creativity in the changes.
-	Extra credit is only eligible to working programs that still cover the functionality of the original specification.
 
 
## GRADING RUBRIC

Functional project working to specification (Application Development) [50 points]
-	All test cases pass with no issue. Test cases include the example output above with additional ad hoc testing.

Project code with appropriate comments and formatting (Quality and Secure Code) [10 points]
-	Module and function header comments and other appropriate comments
-	Well-formatted code with few PEP 8 violations

Project presentation (Effective Communication) [20 points]
-	Well organized and informative presentation given in the time limit
-	Present with video and audio
-	Appropriate attire in appropriate setting
-	Responsive to questions with thoughtful answers

Peer evaluation (Teamwork) [20 points]
-	Submission of peer evaluation
NOTE: If peer evaluation is not submitted, all points are forfeited for this category.
-	Thoughtfulness and insights provided in evaluation
-	Input from peers on teammate’s contribution and performance

Extra credit for approved and implemented changes [25 points]
-	Innovation and creativity of proposal
-	Amount of participation on team in designing and implementing extra credit
-	Amount of work involved in completing extra credit features
