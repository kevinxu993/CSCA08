def copy_me(L):
    '''(list) -> list
    Takes as input a list, and returns a copy of the list with the following
    changes:
    Strings have all their letters converted to upper-case
    Integers and floats have their value increased by 1
    booleans are negated (False becomes True, True becomes False)
    Lists are replaced with the word "List"
    REQ: The input should be a list
    >>> copy_me(['abc', 1, 2.5, True, False, [3, 4, 5]])
    ['ABC', 2, 3.5, False, True, 'List']
    '''
    # create a copy of the input
    newL = L[:]
    for i in range(len(L)):
        # Strings have all their letters converted to upper-case
        if(isinstance(L[i], str)):
            newL[i] = L[i].upper()
        # Integers and floats have their value increased by 1
        elif(type(L[i]) == int) or (type(L[i]) == float):
            newL[i] = L[i] + 1
        # booleans are negated (False becomes True, True becomes False)
        elif(L[i] is True):
            newL[i] = False
        elif(L[i] is False):
            newL[i] = True
        # Lists are replaced with the word "List"
        elif(isinstance(L[i], list)):
            newL[i] = "List"
    # return the new copy
    return newL


def mutate_me(LIST):
    '''(list) -> None
    Takes as input a list, returns None, and changes the input list in the
    following ways:
    Strings have all their letters converted to upper-case
    Integers and floats have their value increased by 1
    booleans are negated (False becomes True, True becomes False)
    Lists are replaced with the word "List"
    REQ: The input should be a list
    >>> mutate_me(['abc', 1, 2.5, True, False, [3, 4, 5]])

    '''
    # create a copy of the input
    newLIST = LIST[:]
    for i in range(len(LIST)):
        # Strings have all their letters converted to upper-case
        if(isinstance(LIST[i], str)):
            newLIST[i] = LIST[i].upper()
        # Integers and floats have their value increased by 1
        elif(type(LIST[i]) == int) or (type(LIST[i]) == float):
            newLIST[i] = LIST[i] + 1
        # booleans are negated (False becomes True, True becomes False)
        elif(LIST[i] is True):
            newLIST[i] = False
        elif(LIST[i] is False):
            newLIST[i] = True
        # Lists are replaced with the word "List"
        elif(isinstance(LIST[i], list)):
            newLIST[i] = "List"
    LIST[:] = newLIST
    # return None
    return None
