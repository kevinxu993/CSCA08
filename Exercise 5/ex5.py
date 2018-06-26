def function_names(fiha):
    '''(io.TextIOWrapper) -> list of str
    Takes as a parameter a file_handle open for reading, and returns a list of
    all of the function names in that file.
    REQ: The file_handle opens a file for reading
    >>> function_names(fiha)
    ['insert', 'up_to_first', 'cut_list']
    '''
    # create a new list
    name = []
    # go through the entire file and find all of the functions
    for line in fiha:
        if line.startswith("def"):
            # get the name of the function found
            temp = line[line.find("def") + 4:line.find("(")]
            # add the name to the list
            name.append(temp)
    # return the list
    return name


def justified(fiha):
    '''(io.TextIOWrapper) -> bool
    Takes as a parameter a file handle open for reading, and returns a boolean
    which is true if and only if every line in that file is left-justified.
    REQ: The file_handle opens a file for reading
    >>> justified(fiha)
    True
    '''
    for line in fiha:
        if line.startswith(" "):
            return False
    return True


def section_average(fiha, section):
    '''(io.TextIOWrapper, str) -> float or None
    Return the average midterm mark for all students in that section, or
    return None if the section code does not appear in the marks file for any
    students.
    REQ: The file_handle opens a file for reading
    REQ: section is a string
    >>> section_average(open("ex5_grade_file.txt", "r"), "LEC01")
    17.25
    '''
    mark = []
    total = 0
    num = 0
    for line in fiha:
        mark.append(line.split())
    for n in range(len(mark)):
        if mark[n][-2] == section:
            total = total + float(mark[n][-1])
            num = num + 1
    if num == 0:
        return None
    else:
        return total/num
