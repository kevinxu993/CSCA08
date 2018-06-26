def percent_to_gpv(percentage_mark):
    '''(int) -> float
    Take a percentage mark (int) as input, and returns the corresponding Grade
    Point Value (float).
    REQ: 0 <= percentage_mark <= 100
    >>> percent_to_gpv(99)
    4.0
    >>> percent_to_gpv(60)
    1.7
    '''
    # Take a percentage mark to convert it to a GPV
    if (percentage_mark >= 85 and percentage_mark <= 100):
        gpv = 4.0
    elif(percentage_mark >= 80):
        gpv = 3.7
    elif(percentage_mark >= 77):
        gpv = 3.3
    elif(percentage_mark >= 73):
        gpv = 3.0
    elif(percentage_mark >= 70):
        gpv = 2.7
    elif(percentage_mark >= 67):
        gpv = 2.3
    elif(percentage_mark >= 63):
        gpv = 2.0
    elif(percentage_mark >= 60):
        gpv = 1.7
    elif(percentage_mark >= 57):
        gpv = 1.3
    elif(percentage_mark >= 53):
        gpv = 1.0
    elif(percentage_mark >= 50):
        gpv = 0.7
    elif(percentage_mark >= 0):
        gpv = 0.0

    # Return the corresponding Grade Point Value
    return gpv


def card_namer(value, suit):
    '''(str, str) -> str
    Take two single character strings, representing the value and suit of a
    card following the shorthand below, and returns the full name of the card.
    REQ: Choose value from "A" 2 to 9 "T" "J" "Q" "K"
    REQ: Choose suit from "D" "C" "H" "S"
    >>> card_namer('Q','D')
    'Queen of Diamonds'
    >>> card_namer('9','S')
    '9 of Spades'
    >>> card_namer('8','T')
    'CHEATER!'
    '''
    # Card value
    if(value == "A"):
        val = "Ace"
    elif(value == "T"):
        val = "10"
    elif(value == "J"):
        val = "Jack"
    elif(value == "Q"):
        val = "Queen"
    elif(value == "K"):
        val = "King"
    elif(2 <= int(value) <= 9):
        val = value
    # Card suit
    if(suit == "D"):
        su = "Diamonds"
    elif(suit == "C"):
        su = "Clubs"
    elif(suit == "H"):
        su = "Hearts"
    elif(suit == "S"):
        su = "Spades"
    # If the suit input isn¡¯t one of the recognized inputs
    else:
        return "CHEATER!"
    # Return the full name of the card
    return val + " of " + su


def my_str(inp):
    '''(obj) -> str
    Take an object as input, and returns a string representation of that
    object.
    REQ: obj != None
    >>> my_str("Hello")
    'Hello'
    >>> my_str(False)
    'NO'
    >>> my_str(42)
    'Medium Number'
    >>> my_str(42.0)
    '42.0'
    >>> my_str(3.1415926)
    '3.14'
    >>> my_str([1, 2, 3])
    'I dunno'
    '''
    if(isinstance(inp, str)):
        return inp
    elif(isinstance(inp, bool)):
        if(inp is True):
            return "YES"
        if(inp is False):
            return "NO"
    elif(isinstance(inp, int)):
        if(inp <= 10):
            return "Small Number"
        elif(11 <= inp <= 99):
            return "Medium Number"
        else:
            return "Large Number"
    elif(isinstance(inp, float)):
        return str(round(inp, 2))
    else:
        return "I dunno"

if  __name__ == "__main__":
    import doctest
    doctest.testmod()