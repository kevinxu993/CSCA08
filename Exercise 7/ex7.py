def create_dict(fh):
    '''(io.TextIOWrapper) -> dict of {str: [str, str, str, int, str]}
    Returns a dictionary that maps a string to a list of strings and ints.
    REQ: The parameter should be an open file handle.
    '''
    # create an empty dictionary
    d = {}
    # read the lines in the file
    for line in fh:
        # split all the words into a list
        [username, firstname, lastname, age, gender, email] = line.split()
        # map the elements from the list to the dictionary
        d[username] = [lastname, firstname, email, int(age), gender]
    # return the dictionary
    return d


def update_field(di, un, nof, nv):
    '''(dict, str, str, str or int) -> NoneType
    Takes a dictionary, a username, the name of a field, and a new value to
    replace the current value of the specified and mutate the dictionary as
    appropriate.
    REQ: The name of a field should be one of: 'LAST', 'FIRST', 'E-MAIL', 'AGE'
    or 'GENDER'.
    >>> update_field({'sclause': ['Clause', 'Santa', 'santa@christmas.np',\
    450, 'M']}, 'sclause', 'AGE', 999)
    '''
    # get the index of the name of a field
    ind = helper(nof)
    # mutate the dictionary
    di[un][ind] = nv


def helper(inp):
    '''(str) -> int
    Returns a integer representing a index of a list.
    REQ: inp is a string.
    >>> helper('LAST')
    0
    '''
    # create a new integer
    ind = None
    # check what the input is and assign corresponding value to index
    if(inp == 'LAST'):
        ind = 0
    elif(inp == 'FIRST'):
        ind = 1
    elif(inp == 'E-MAIL'):
        ind = 2
    elif(inp == 'AGE'):
        ind = 3
    elif(inp == 'GENDER'):
        ind = 4
    # return the index
    return ind


def select(dic, nofs, nofc, v):
    '''(dict, str, str, str or int) -> set
    Returns a set of all the data elements from the selected fields of people
    whose checked fields were equal to the checked value.
    REQ: The name of a field should be one of: 'LAST', 'FIRST', 'E-MAIL', 'AGE'
    or 'GENDER'.
    >>> select({'sclause':['Clause', 'Santa', 'santa@christmas.np', 450, 'M'],\
    'ebunny':['Bunny', 'Easter', 'bunny@easter.hop', 99, 'M'],\
    'tfairy':['Fairy', 'Tooth', 'fairy@money4teeth.net', 0, 'F']}, 'E-MAIL',\
    'GENDER', 'M')
    {'santa@christmas.np', 'bunny@easter.hop'}
    '''
    # create a new set
    res = set()
    # get the indices of the names of fields
    inds = helper(nofs)
    indc = helper(nofc)
    # check the whole dictionary
    for ele in dic:
        # if the checked field is equal to the checked value
        if(dic[ele][indc] == v):
            # add the selected field to the set
            res.add(dic[ele][inds])
    # return the set
    return res
