def welcome_message(board_size, number_of_ships):
    """
    Displays the welcome message.
    Specifies the board size and the number of ships.
    Displays the coordinates for the top left corner.
    """

    #the welcome text is inspire from Ultimate battleships project ci
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

    input_text = "Type in your battle name (max 30 characters):"
    name = input(input_text + "\n")
    print('-' * len(input_text))
    return name


def main():
    """
    Main function
    """
    board_size = 5
    number_of_ships = 4
    welcome_message(board_size, number_of_ships)
    name = name_input()
    print(name)


main()