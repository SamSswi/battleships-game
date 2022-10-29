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


def board(size):
    """
    Displays a basic board
    """

    row = []

    # underscore as a throwaway variable - CI Battleships game
    for _ in range(size):
        col = []
        for _ in range(size):
            col.append(".")
        row.append(col)

    guess = input("coordinates: ")
    print(guess)
    modify_board = guess.split(',')
    print(modify_board)  # python3 run.py
    row[int(modify_board[0])][int(modify_board[1])] = 'a'
    display_row = row
    for i in range(len(display_row)):
        display_row[i] = " ".join(display_row[i])
    display_row = "\n".join(display_row)
    print(display_row)


def main():
    """
    Main function
    """
    board_size = 5
    # number_of_ships = 4
    # welcome_message(board_size, number_of_ships)
    # name = name_input()
    # print(name)
    board(board_size)


main()