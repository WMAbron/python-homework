'''Willie Abron 10/16/2018
Creating a program that asks users for the students and quiz scores to list the average.
'''

def main():
    try:
        num_students, num_quizzes = input1()
        student_score_sets_compiled, grand_avg = input2process(num_students, num_quizzes)
        final_outputs(student_score_sets_compiled, grand_avg, num_students, num_quizzes)
        print('Thank you for using the program')
    except Exception as err:
        print(err)


def input1():
    print('How many students are taking quizzes? ')
    num_students = input_pos_int()
    print('How many quizzes will each one take? ')
    num_quizzes = input_pos_int()
    return num_students, num_quizzes

def input_pos_int(): # makes sure input over 0 is 'int-able'
    pos_int = input('\tEnter a positive whole number: ')
    while pos_int.isnumeric() is False or pos_int == '0':
        pos_int = input('\tPlease enter a whole number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int

def input2process(num_students, num_quizzes):
    student_score_sets_compiled = [] # list of lists-init outside of loop to include all students
    grand_avg = 0.0
    grand_total = 0
    for student in range(num_students):
        student_score_set = [] # Re-initialize in outerloop, to restart for each student
        total_points = 0
        quiz_average = 0.00
        print(f'Quiz info for student #{student + 1}: ')
        for quiz in range(num_quizzes):
            print(f'\tScore for quiz #{quiz + 1}:')
            quiz_score = input_pos_int() # call function to  provide valid float
            student_score_set.append(quiz_score)
            print(student_score_set)#turned on during development to check code
            total_points += quiz_score #total_points = total_points + quiz_score
            quiz_average = total_points / num_quizzes
        grand_total += total_points
        student_score_sets_compiled.append(student_score_set)#builds list - add each student's score set

        loop_outputs(total_points, quiz_average, student, student_score_set)
        grand_avg = grand_total / num_students / num_quizzes
        return student_score_sets_compiled, grand_avg

def loop_outputs(total_points,quiz_average, student, student_score_set):
    print(f'Quiz scores for student #{student + 1}: {student_score_set} ')
    print(f'\tTotal points = {total_points}')
    print('\tQuiz Average = {quiz_average:<0.2f}')

def final_outputs(student_score_sets_compiled, grand_avg, num_students,num_quizzes):
    print(f'Overall results for {num_students} students & {num_quizzes} quizzess: ')
    print('Here are the sets compiled: ', student_score_sets_compiled)
    print(f'Group average = {grand_avg:<0.2f}')
    for score_set in student_score_sets_compiled:
        print('Student', student_score_sets_compiled.index(score_set)+1, 'scores =', score_set)
main()
