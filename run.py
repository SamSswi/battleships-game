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

    def print_board(self, name):
        """
        Displays the board, with the name on top.
        """

        print(f"{name}'s board:")
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
            result = "Hit"
        else:
            self.board[x][y] = 'X'
            result = "Miss"
        self.guesses.append((x, y))
        return result
    
    def generate_ships(self, num_ships, type):
        """
        Generates ships for either player or computer board.
        """

        for _ in range(num_ships):
            row = randint(0, 2)
            col = randint(0, 2)
            while (row, col) in self.ships:
                row = randint(0, 2)
                col = randint(0, 2)
            self.adding_ships(row, col, type)


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


def guess_input():
    """
    Prompts the player to guess computer's ships positions.
    Collects the imputed data.
    """
    print("Time to attack! The enemy is hiding his ships!")
    row = input("Select a row where to strike: ")
    col = input("Let's add precision to that. Select a column: ")

    player_guess = (row, col)

    return player_guess


def validate_guess(object, guess, board_size):
    """
    Check whether a player guess is valid.
    """

    try:
        row, col = guess
        v_row = int(row)
        v_col = int(col)
        upp_limit = board_size - 1
        low_limit = 0
        lower_err = v_row < low_limit or v_col < low_limit
        upper_err = v_row > upp_limit or v_col > upp_limit

        if guess in object.guesses:
            return False

        if lower_err or upper_err:
            print(f"The values must be between {low_limit} and {upp_limit}")
            return False
    except ValueError:
        print("Both coordinates must be numbers")
        return False

    return True


def final_guess_player(player, computer, board_size):
    """
    Sums up all the guessing process for the player
    """
    coordinates = guess_input()
    a = validate_guess(player, coordinates, board_size)
    while not a:
        coordinates = guess_input()
        a = validate_guess(player, coordinates, board_size)
    
    row, col = coordinates
    result = computer.guess(int(row), int(col))
    return result


def computer_guess(computer, player, board_size):
    """
    Sums up all the guessing process for computer
    """
    guess = (randint(0, board_size - 1), randint(0, board_size - 1))
    while guess in player.guesses:
        guess = (randint(0, board_size -1), randint(0, board_size - 1))

    row, col = guess
    result = player.guess(int(row), int(col))
    return result


def main():
    """
    Main function
    """
    board_size = 3
    number_of_ships = 4
    welcome_message(board_size, number_of_ships)
    name = name_input()
    player = Board(board_size, number_of_ships, name, 'player')
    computer = Board(board_size, number_of_ships, "Computer", "computer")
    player.print_board(name)
    computer.print_board('computer')
    player.generate_ships(number_of_ships, 'player')
    computer.generate_ships(number_of_ships, 'computer')
    player_score = 0
    computer_score = 0
    while player_score < number_of_ships and computer_score < number_of_ships:
        plyr_guess = final_guess_player(player, computer, board_size)
        cpu_guess = computer_guess(computer, player, board_size)
        if plyr_guess == "Hit":
            player_score += 1
        if cpu_guess == "Hit":
            computer_score += 1
        # print(player.guesses)
        # print(computer.guesses)
        player.print_board(name)
        computer.print_board('computer')
        print(f"{name}  {player_score} : {computer_score}  computer")


main()

# a = Board(5, 4, "matt", 'computer')
# x = Board(5, 4, "greg", 'player')
# x.generate_ships(4, 'player')
# a.generate_ships(4, 'computer')
# x.print_board()
# a.print_board()


# x.guess(1, 1)
# x.guess(randint(0, 4), randint(0, 4))
# x.guess(randint(0, 4), randint(0, 4))

# a.guess(randint(0, 4), randint(0, 4))

# a.print_board()
# x.print_board()


# # a = name()
# # print(a)

# # print(randint(0, 5))

# y = x.ships

# print(x.ships)