from random import randint


# the idea of creating the Board class and its structure is taken from
# Code Institute Ultimate Battleships project.
# Link to the deployed game: https://p3-battleships.herokuapp.com/
# Source where the code was displayed:
# https://www.youtube.com/watch?v=4sqtzZQpDJE
class Board:
    """
    Main board class. Sets board size, the number of ships,
    the player's name and the board type (player or computer board)
    Has methods for adding ships and guesses and printing the board.
    """

    # The init function is taken from Code Institute
    # Ultimate Battleships project.
    def __init__(self, size, num_ships, participant_name, board_type):
        self.size = size
        self.board = [['.' for i in range(size)] for j in range(size)]
        self.num_ships = num_ships
        self.participant_name = participant_name
        self.board_type = board_type
        self.guesses = []
        self.ships = []

    def print_board(self, participant_name):
        """
        Displays the board, with the name on top.
        """
        print(f"{participant_name}'s board:")
        # idea to loop a print statement is taken from Code Institute
        # Ultimate Battleships project.
        for i in range(len(self.board)):
            print(" ".join(self.board[i]))

    # The adding_ships function is taken from Code Institute
    # Ultimate Battleships project.
    def adding_ships(self, a, b):
        """
        Adds ships to the board for the player.
        Adds ship coordinates to the self.ships list for the computer.
        """
        if self.board_type == 'computer':
            self.ships.append((a, b))
        elif self.board_type == 'player':
            self.board[a][b] = '@'
            self.ships.append((a, b))

    # The guess function is taken from Code Institute
    # Ultimate Battleships project.
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

    def generate_ships(self, num_ships, size):
        """
        Generates ships for either player or computer board.
        """

        for _ in range(num_ships):
            row = random_coordinate(size)
            col = random_coordinate(size)
            while (row, col) in self.ships:
                row = random_coordinate(size)
                col = random_coordinate(size)
            self.adding_ships(row, col)


def welcome_message(board_size, number_of_ships):
    """
    Displays the welcome message.
    Specifies the board size and the number of ships.
    Displays the coordinates for the top left corner.
    """

    # the welcome message is inspired from Code Institute
    # Ultimate battleships project.
    message = f'''
       Welcome to the BATTLESHIPS GAME!
   Board Size: {board_size}; Number of Battleships: {number_of_ships}
Top left corner coordinates - row: 0, col: 0
    '''
    print_46_dashes()
    print(message)
    print_46_dashes()
    return message


def name_input():
    """
    Gets player name with user input.
    Validates player name.
    Returns the name.
    """

    # the idea to use a while True loop to get the right user input
    # is inspired from Code Institute Love Sandwiches project
    # (https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode)
    while True:
        input_text = "Type in your battle name (max 30 characters):"
        player_name = input(input_text + "\n")
        print_46_dashes()
        if validate_name(player_name):
            return player_name


def validate_name(player_name):
    """
    Returns False if the name is too long or an empty string
    """

    name_length = len(player_name)
    if name_length > 30:
        print(f"Your name has {name_length} characters and it exceeds"
              " the limit of 30 characters: \nTry entering a shorter "
              "battle name!")
        return False
    elif player_name == '':
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
    row = input("Select a row where to strike: \n")
    col = input("Let's add precision to that. Select a column: \n")

    player_guess = (row, col)

    return player_guess


def validate_guess(opponent, guess, board_size):
    """
    Check whether a player guess is valid.
    """

    # the idea to use if condition inside the try section
    # is inspired from Code Institute Love Sandwiches project
    # (https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode)
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


def valid_guess_player(computer, board_size):
    """
    Sums up all the guessing process for the player
    """
    coordinates = guess_input()
    validation = validate_guess(computer, coordinates, board_size)
    while not validation:
        coordinates = guess_input()
        validation = validate_guess(computer, coordinates, board_size)

    row, col = coordinates
    result = computer.guess(int(row), int(col))
    return result


def computer_guess(player, board_size):
    """
    Sums up all the guessing process for computer
    """
    guess = (random_coordinate(board_size), random_coordinate(board_size))
    while guess in player.guesses:
        guess = (random_coordinate(board_size), random_coordinate(board_size))

    row, col = guess
    result = player.guess(int(row), int(col))
    return result


def round_result(guess_player, guess_computer, player_result, computer_result):
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
    inp = input("Press any key to continue. To quit press 'n'.\n")
    if str(inp) == 'n':
        return 'quit'


def final_result(player_name, player_score, computer_score):
    """
    Displays the final result of the game.
    """
    print("THE GAME IS OVER!")
    if player_score > computer_score:
        print_46_dashes()
        print(f"Well done, Admiral {player_name}! The victory is yours!!!")
        print_46_dashes()
    elif computer_score > player_score:
        print_46_dashes()
        print("The enemy won! The battle is lost! Time to regroup.")
        print_46_dashes()
    else:
        print_46_dashes()
        print("That's a draw! Time to negotiate a ceasefire agreement.")
        print_46_dashes()


def random_coordinate(board_size):
    """
    Generates a random number that can serve as a valid coordinate
    """
    num = randint(0, board_size - 1)
    return num


def print_46_dashes():
    """
    Prints 46 dashes
    """
    dashes = "-" * 46
    print_dashes = print(dashes)
    return print_dashes


def main():
    """
    Main function. Starts a new game. Sets the board size.
    Resets the scores. Initializes the boards. Runs the process
    of playing the game between the player and the computer.
    Updates the scores and displays the final result.
    """
    board_size = 5
    number_of_ships = 4
    welcome_message(board_size, number_of_ships)
    p_name = name_input()
    player = Board(board_size, number_of_ships, p_name, 'player')
    computer = Board(board_size, number_of_ships, "Computer", "computer")
    player.generate_ships(number_of_ships, board_size)
    computer.generate_ships(number_of_ships, board_size)
    player.print_board(p_name)
    computer.print_board('computer')
    player_score = 0
    computer_score = 0
    while player_score < number_of_ships and computer_score < number_of_ships:
        plyr_guess = valid_guess_player(computer, board_size)
        cpu_guess = computer_guess(player, board_size)
        last_item_pl = player.guesses[-1]
        last_item_cpu = computer.guesses[-1]
        round_result(last_item_cpu, last_item_pl, plyr_guess, cpu_guess)
        if plyr_guess == "Hit":
            player_score += 1
        if cpu_guess == "Hit":
            computer_score += 1
        print_46_dashes()
        print(f"{p_name}  {player_score} : {computer_score}  computer")
        print_46_dashes()
        player_won = (player_score == number_of_ships)
        computer_won = (computer_score == number_of_ships)
        if player_won or computer_won:
            final_result(p_name, player_score, computer_score)
            break
        quit_question = quit_game_input()
        if quit_question == 'quit':
            # The idea to restart the game after player decides to quit is
            # taken from the Code Institute Ultimate Battleships project
            main()
            break
        player.print_board(p_name)
        computer.print_board('computer')
    # The idea to give the player the option to start a new game is
    # taken from the Code Institute Ultimate Battleships project
    input("Press any key to start a new game:\n")
    main()


main()
