# Global variables. Feel free to play around with these
# but please return them to their original values before you submit.
# HINT: Your code should be using these values, if I change them (and I will)
# your output should change accordingly
a0_weight = 5
a1_weight = 7
a2_weight = 8
term_tests_weight = 25
exam_weight = 40
exercises_weight = 10
quizzes_weight = 5

a0_max_mark = 25
a1_max_mark = 50
a2_max_mark = 100
term_tests_max_mark = 50
exam_max_mark = 100
exercises_max_mark = 10
quizzes_max_mark = 5
exam_pass_mark = 40
overall_pass_mark = 50


def get_max(component_name):
    '''(str) -> float
    Given the name of a course component (component_name),
    return the maximum mark for that component. This is used to allow the GUI
    to display the "out of" text beside each input field.
    REQ: component_name in {'a0', 'a1', 'a2', 'exercises', 'term tests',
    'quizzes', 'exam'}
    >>> get_max('a0')
    25
    >>> get_max('exam')
    100
    '''
    # DO NOT EDIT THIS FUNCTION. This function exists to allow the GUI access
    # to some of the global variables. You can safely ignore this function
    # for the purposes of Ex2.
    if(component_name == 'a0'):
        result = a0_max_mark
    elif(component_name == 'a1'):
        result = a1_max_mark
    elif(component_name == 'a2'):
        result = a2_max_mark
    elif(component_name == 'exercises'):
        result = exercises_max_mark
    elif(component_name == 'term tests'):
        result = term_tests_max_mark
    elif(component_name == 'quizzes'):
        result = quizzes_max_mark
    else:
        result = exam_max_mark

    return result


def term_work_mark(a, b, c, d, e, f):
    '''(float, float, float, float, float, float) -> float
    Calculate your term mark (as a contribution to your final grade) given your
    marks on all of the coursework components.
    REQ: a,b,c,d,e,f >=0
    >>> term_work_mark(25, 50, 100, 10, 5, 50)
    60.0
    >>> term_work_mark(20, 45, 70, 8, 4, 40)
    47.9
    '''
    # calculate marks on each coursework component
    a0_mark = contribution(a, a0_max_mark, a0_weight)
    a1_mark = contribution(b, a1_max_mark, a1_weight)
    a2_mark = contribution(c, a2_max_mark, a2_weight)
    exercises_mark = contribution(d, exercises_max_mark, exercises_weight)
    quizzes_mark = contribution(e, quizzes_max_mark, quizzes_weight)
    term_tests_mark = contribution(f, term_tests_max_mark, term_tests_weight)
    # calculate total term mark
    term_Mark = a0_mark+a1_mark+a2_mark+exercises_mark+quizzes_mark\
        + term_tests_mark

    return term_Mark


def final_mark(a, b, c, d, e, f, g):
    '''(float, float, float, float, float, float, float) -> float
    Return your final mark for the term out of 100 given your marks on all of
    the coursework components including your final exam mark.
    REQ: a,b,c,d,e,f,g >=0
    >>> final_mark(25, 50, 100, 10, 5, 50, 100)
    100.0
    >>> final_mark(20, 45, 70, 8, 4, 40, 73)
    77.1
    '''
    # calculate the term mark with weight
    term_mark = term_work_mark(a, b, c, d, e, f)
    # calculate the exam mark with weight
    exam_mark = contribution(g, exam_max_mark, exam_weight)
    # calculate the final mark
    final_Mark = term_mark + exam_mark

    return final_Mark


def is_pass(a, b, c, d, e, f, g):
    '''(float, float, float, float, float, float, float) -> bool
    Return a boolean representing whether you passed the course given your\
        marks
    on all of the coursework components including your final exam mark.
    REQ: a,b,c,d,e,f,g >=0
    >>> is_pass(20, 45, 70, 8, 4, 40, 41)
    True
    >>> is_pass(20, 45, 70, 8, 4, 40, 39)
    False
    >>> is_pass(10, 21, 12, 2, 1, 15, 23)
    False
    '''
    # must get a final overall mark at or above 50
    ispass = final_mark(a, b, c, d, e, f, g) >= overall_pass_mark
    # an exam mark at or above a certain 40
    ispass = ispass and (g >= exam_pass_mark)

    return ispass


def percentage(raw_mark, max_mark):
    ''' (float, float) -> float
    Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark of max_mark.
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: raw_mark <= max_mark
    >>> percentage(15, 20)
    75.0
    >>> percentage(4.5, 4.5)
    100.0
    '''
    # calculate the number representing the first parameter as a percentage of
    # the second parameter
    percentage = raw_mark/max_mark*100

    return percentage


def contribution(raw_mark, max_mark, weight):
    ''' (float, float, float) -> float
    Given a piece of work where the student earned raw_mark marks out of a
    maximum of max_marks marks possible, return the number of marks it
    contributes to the final course mark if this piece of work is worth weight
    marks in the course marking scheme.
    REQ: raw_mark >= 0
    REQ: max_mark > 0
    REQ: weight >= 0
    >>> contribution(13.5, 15, 10)
    9.0
    '''
    result = (raw_mark/max_mark)*weight

    return result
