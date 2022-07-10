# ----------------------------------------------------------------
# Author: Brian Gill, Jeremy Jacobs, Joshua Macy
# Date: 1 July 2022
# Purpose: Course registration system for students
# -----------------------------------------------------------------

# import two function defining modules
import student


# validate PIN to student ID
def login(id, s_list):
    pin = input('Enter PIN: ')
    for x in range(len(s_list)):
        if s_list[x][1] == pin and s_list[x][0] == id:
            print('ID and PIN verified\n')
            return True
    print('ID or PIN incorrect\n')
    return False


def main():
    # predefined data
    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]

    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}

    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': []}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}
    # menu system
    user_id = '1'
    while user_id != '0':
        user_id = input('Enter ID to log in, or 0 to quit: ')
        if user_id == '0':
            break
        else:
            valid = login(user_id, student_list)
        if valid:
            choice = input('Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit:')
            while choice != '0':
                if choice == '1':
                    student.add_course(user_id, course_roster, course_max_size)
                    
                elif choice == '2':
                    student.drop_course(user_id, course_roster)
                    
                elif choice == '3':
                    student.list_courses(user_id, course_roster)
                    
                elif choice == '4':
                    print('4')  # add fx
                    
                else:
                    print("Invalid choice")
                
                print()
                choice = input(
                        'Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit:')
                
            print('Session ended')
            print()


main()
