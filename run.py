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
    
    def generate_ships(self, num_ships, size, type):
        """
        Generates ships for either player or computer board.
        """

        for _ in range(num_ships):
            row = random_coordinate(size)
            col = random_coordinate(size)
            while (row, col) in self.ships:
                row = random_coordinate(size)
                col = random_coordinate(size)
            self.adding_ships(row, col, type)


def welcome_message(board_size, number_of_ships):
    """
    Displays the welcome message.
    Specifies the board size and the number of ships.
    Displays the coordinates for the top left corner.
    """

    # the welcome text is inspire from Ultimate battleships project ci
    message = f'''
--------------------------------------------
       Welcome to the BATTLESHIPS GAME!
   Board Size: {board_size}; Number of Battleships: {number_of_ships}
Top left corner coordinates - row: 0, col: 0
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


def validate_guess(object, opponent, guess, board_size):
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

        if (v_row, v_col) in opponent.guesses:
            print("You already hit that location, choose another one.")
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
    a = validate_guess(player, computer, coordinates, board_size)
    while not a:
        coordinates = guess_input()
        a = validate_guess(player, computer, coordinates, board_size)
    
    row, col = coordinates
    result = computer.guess(int(row), int(col))
    return result


def computer_guess(computer, player, board_size):
    """
    Sums up all the guessing process for computer
    """
    guess = (random_coordinate(board_size), random_coordinate(board_size))
    while guess in player.guesses:
        guess = (random_coordinate(board_size), random_coordinate(board_size))

    row, col = guess
    result = player.guess(int(row), int(col))
    return result


def score_text(guess_player, guess_computer, player_result, computer_result):
    """
    Prints informative text about the player's and computer's latest guess.
    """
    hit = "Hit"
    print(f"Player guessed: {guess_player}")
    print(f"Player {'hit a ship!' if player_result == hit else 'missed'}.")
    print(f"Computer guessed: {guess_computer}")
    print(f"Computer {'hit a ship!' if computer_result == hit else 'missed'}.")


def quit_game_input():
    """
    Presents the player the opportunity to quit the game
    """
    inp = input("Press any key to continue. To quit press 'n'.")
    if str(inp) == 'n':
        return 'quit'


def display_winner(player_score, computer_score):
    """
    Displays the final result of the game.
    """
    if player_score > computer_score:
        print("Player won")
    elif computer_score > player_score:
        print("Computer won")
    else:
        print("It's a draw")


def random_coordinate(board_size):
    """
    Generates a random number that can serve as a valid coordinate 
    """
    num = randint(0, board_size - 1)
    return num


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
    player.generate_ships(number_of_ships, board_size, 'player')
    computer.generate_ships(number_of_ships, board_size, 'computer')
    player.print_board(name)
    computer.print_board('computer')
    player_score = 0
    computer_score = 0
    while player_score < number_of_ships and computer_score < number_of_ships:
        plyr_guess = final_guess_player(player, computer, board_size)
        cpu_guess = computer_guess(computer, player, board_size)
        last_item_pl = player.guesses[-1]
        last_item_cpu = computer.guesses[-1]
        score_text(last_item_cpu, last_item_pl, plyr_guess, cpu_guess)
        if plyr_guess == "Hit":
            player_score += 1
        if cpu_guess == "Hit":
            computer_score += 1
        # print(player.guesses)
        # print(computer.guesses)
        print(f"{name}  {player_score} : {computer_score}  computer")
        player_won = (player_score == number_of_ships)
        computer_won = (computer_score == number_of_ships)
        if player_won or computer_won:
            display_winner(player_score, computer_score)
            break
        quit_question = quit_game_input()
        if quit_question == 'quit':
            break
        player.print_board(name)
        computer.print_board('computer')


main()
