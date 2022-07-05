#
# Brian J Gill, Joshua Macy, Jeremy Jacobs
# 3-Jul-2022
# The billing.py module for Group 5 project
#

# This function calculates the course hours and cost of enrollment.
# It has 4 parameters.  id is the ID of the student, s_in_state is a dictionary
# of in state students using a boolean expression. c_rosters is a dictionary of
# class rosters.  c_hours is a dictionary with the credit hours of each class.
# The function calculates the bill based on $225 per credit hour for in-state students
# and $850 per credit hour for out-of-state students.  After calculating the bill,
# the function returns the total number of credit hours and the total cost
# of enrollment.

def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    # Local variables to store in_state and out_state values
    in_state = 225
    out_state = 850

    # hours accumulator
    hours = 0

    # iterate through the course roster.
    for course in c_rosters.keys():
        # if the student ID is in a course_rosters values
        # add the course hours to the hours accumulator
        if id in c_rosters[course]:
            hours += c_hours[course]

    # Test if student_in_state is True.
    if s_in_state[id]:
        # Calculate for student in_state
        cost = hours * in_state

    # If student_in_state is False.
    else:
        # Calculate for student out_state
        cost = hours * out_state

    return hours, cost


# This function displays the course hours and the cost of enrollment.
# It has 2 parameters: hours is the number of course hours; cost is
# the total cost of enrollment.  This function displays the total
# number of credit hours and the total cost of enrollment.

def display_hours_and_bill(hours, cost):
    print(f'Course load: {hours} credit hours')
    print(f'Enrollment cost: ${cost:.2f}')



