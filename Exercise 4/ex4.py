def insert(A, B, I):
    '''(list, list, int) -> list
    Or (str, str, int) -> str
    Takes 3 parameters, listA, listB1 and an index, then returns a copy of
    listA with the elements of listB inserted at the index.
    REQ: A, B can be lists or strings at the same time.
    REQ: I must be an integer.
    >>> insert([1, 2, 3], ['a', 'b', 'c'], 2)
    [1, 2, 'a', 'b', 'c', 3]
    >>> insert("123","abc",2)
    '12abc3'
    '''
    # returns a copy of listA with the elements of listB inserted at the index.
    return A[:I] + B + A[I:]


def up_to_first(A, B):
    '''(list, obj) -> list
    Or (str, obj) -> str
    Takes two parameters, a list (or string) and an object, and returns a copy
    of the list up to (but not including) the first occurrence of that object,
    or all of the elements if that object is not in the list.
    >>> up_to_first([1, 2, 3, 4], 3)
    [1, 2]
    >>> up_to_first([1, 2, 3, 4], 9)
    [1, 2, 3, 4]
    >>> up_to_first('abcdef', 'd')
    'abc'
    '''
    # check if the object is in the list or not and return a corresponding list
    # or string
    if(A.count(B) != 0):
        return A[:A.index(B)]
    else:
        return A


def cut_list(A, I):
    '''(list, int) -> list
    (str, int) -> str
    Given a list and an index, returns a copy of the list, but with the items
    before and after the index swapped.
    >>> cut_list([0,1,2,3,4,5,6,7,8,9], 3)
    [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]
    >>> cut_list("ABCDEFGX1234",7)
    '1234XABCDEFG'
    '''
    # returns a copy of the list, but with the items before and after the index
    # swapped
    return A[I+1:] + A[I:I+1] + A[:I]
