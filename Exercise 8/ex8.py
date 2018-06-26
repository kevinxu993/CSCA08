class LightSwitch():
    '''A class to represent a light switch'''

    def __init__(self, state):
        '''(LightSwitch, str) -> NoneType
        Create a new light that can be on or off.
        REQ: state is a str which should be either 'on' or 'off'.
        '''
        # check the state is on or off
        self._state = state == 'on'

    def turn_on(self):
        '''(LightSwitch) -> NoneType
        Turn the light on.
        '''
        self._state = True

    def turn_off(self):
        '''(LightSwitch) -> NoneType
        Turn the light off.
        '''
        self._state = False

    def flip(self):
        '''(LightSwitch) -> NoneType
        Flip the light's state.
        '''
        # if the light is on, turn it off
        if self._state is True:
            self._state = False
        # if the light is off, turn it on
        elif self._state is False:
            self._state = True

    def __str__(self):
        '''(LightSwitch) -> str
        Return a string representation of the light switch.
        '''
        # if the light is on, then its state is on
        if self._state is True:
            self._cond = 'on'
        # if the light is off, then its state is off
        elif self._state is False:
            self._cond = 'off'
        # create the string
        self._str = 'I am ' + self._cond
        # return the string
        return self._str


class SwitchBoard(LightSwitch):
    '''A class to represent a board of switches'''

    def __init__(self, num):
        '''(SwitchBoard, int) -> NoneType
        Create a new board of a number of switches that are initially off.
        REQ: num is an int representing the number of switches on the board.
        REQ: num >= 1.
        '''
        # set the number of the switches
        self._num = num
        # create a list to represent the board
        self._board = []
        # put the lights on the board
        i = 0
        while(i <= num):
            self._board.append(LightSwitch('off'))
            i = i + 1

    def __str__(self):
        '''(SwitchBoard) -> str
        Return a string representation of the board.
        '''
        # create a string of integers representing the switches that are on
        self._ind = ''
        # create a list of integers representing the switches that are on
        self._inde = []
        # put the indices in the string and the list
        for i in range(0, self._num):
            if self._board[i]._state is True:
                self._ind = self._ind + ' '
                self._ind = self._ind + str(i)
                self._inde.append(i)
        # create the string
        self._str = 'The following switches are on:' + self._ind
        # return the string
        return self._str

    def which_switch(self):
        '''(SwitchBoard) -> list
        Return a list of integers representing the switches that are on.
        '''
        # return the list
        return self._inde

    def flip(self, n):
        '''(SwitchBoard, int) -> NoneType
        Flip the state of the n'th switch.
        REQ: n should be an integer representing "n'th".
        REQ: n >= 1
        '''
        # check if the number is in the range of the board
        if 0 < n < len(self._board):
            # if the switch is on, turn it off
            if self._board[n-1]._state is True:
                self._board[n-1]._state = False
            # if the switch is off, turn it on
            elif self._board[n-1]._state is False:
                self._board[n-1]._state = True

    def flip_every(self, n):
        '''(SwitchBoard, int) -> NoneType
        Flip the state of every n'th switch, starting at 0.
        REQ: n should be an integer representing "every n'th".
        REQ: n >= 1.
        '''
        # for every n'th switch starting at 0
        for i in range(0, len(self._board), n):
            # if the switch is on, turn it off
            if self._board[i]._state is True:
                self._board[i]._state = False
            # if the switch is off, turn it on
            elif self._board[i]._state is False:
                self._board[i]._state = True

    def reset(self):
        '''(SwitchBoard) -> NoneType
        Turns all switches off.
        '''
        # for every switches on the board
        for element in self._board:
            # the state becomes 'off'
            element._state = False

if __name__ == '__main__':
    board = SwitchBoard(1024)
    for i in range(1, 1024):
        board.flip_every(i)
    print(board)
    print(board.which_switch())
