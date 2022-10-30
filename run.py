from random import randint


class Board:  # the main class is from CI Battleship project
    """
    Main board class. Sets board size, the number of ships, 
    the player's name and the board type (player or computer board)
    Has methods for adding ships and guesses and printing the board.
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [['.' for i in range(size)] for j in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print_board(self):
        """
        Displays the board
        """
        for i in range(len(self.board)):    # idea to loop a print statement
            print(" ".join(self.board[i]))  # from CI battleship

    def adding_ships(self, a, b, type):
        """
        Adds ships to the board for the player. 
        Adds ship coordinates to the self.ships list for the computer. 
        """
        if self.type == 'computer':
            self.ships.append((a, b))
        elif self.type == 'player':
            self.board[a][b] = '@'
            self.ships.append((a, b))

    def guess(self, x, y):
        """
        Checks whether the guess is a hit or miss.
        """
        if (x, y) in self.ships:
            self.board[x][y] = '*'
        else:
            self.board[x][y] = 'X'


def welcome_message(board_size, number_of_ships):
    """
    Displays the welcome message.
    Specifies the board size and the number of ships.
    Displays the coordinates for the top left corner.
    """

    # the welcome text is inspire from Ultimate battleships project ci
    message = f'''
    ---------------------------------------------
           Welcome to the BATTLESHIPS GAME!
       Board Size: {board_size}; Number of Battleships: {number_of_ships}
    Top left corner coordinates - row: 1, col: 1
    ---------------------------------------------

    '''
    print(message)
    return message


def name_input():
    """
    Gets player name with user input.
    Validates player name.
    Returns the name.
    """
    while True:  # love-sandwiches CI  the idea to use a while True loop
        input_text = "Type in your battle name (max 30 characters):"
        name = input(input_text + "\n")
        print('-' * len(input_text))
        if validate_name(name):
            return name


def validate_name(name):
    """
    Raises ValueError is the name is too long or an empty string
    """

    name_length = len(name)
    if name_length > 30:
        print(f"Your name has {name_length} characters and it exceeds"
              " the limit of 30 characters: \nTry entering a shorter "
              "battle name!")
        return False
    elif name == '':
        print("You submitted an empty string. Think of a cool battle"
              " name and try again!")
        return False
    else:
        return True


def name():
    """
    Prompt the player to type in the name and return the name when 
    it is valid.
    """
    player_name = name_input()
    valid_name = validate_name(player_name)

    while valid_name is False:
        player_name = name_input()
        valid_name = validate_name(name)

    return player_name


def main():
    """
    Main function
    """
    # board_size = 5
    # number_of_ships = 4
    # welcome_message(board_size, number_of_ships)
    # name = name_input()
    # print(name)
    # board(board_size)


# main()

# a = Board(5, 4, "matt", 'computer')
# x = Board(5, 4, "greg", 'player')
# x.adding_ships(1, 2, 'player')
# x.print_board()
# x.adding_ships(0, 1, 'player')
# x.print_board()
# x.adding_ships(2, 3, 'player')
# x.print_board()
# x.adding_ships(3, 4, 'player')
# x.print_board()
# x.adding_ships(2, 2, 'player')
# x.print_board()

# x.adding_ships(0, 0, 'player')


# x.print_board()

# x.guess(1, 1)
# x.print_board()

a = name()
print(a)
