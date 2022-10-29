def welcome_message(board_size, number_of_ships):
    """
    Displays the welcome message.
    Specifies the board size and the number of ships.
    Displays the coordinates for the top left corner.
    """
    message = f'''
    ---------------------------------------------
           Welcome to the BATTLESHIPS GAME!
       Board Size: {board_size}; Number of Battleships: {number_of_ships}
    Top left corner coordinates - row: 1, col: 1
    ---------------------------------------------
    
    '''
    print(message)
    return message





def main():
    """
    Main function
    """
    board_size = 5
    number_of_ships = 4
    welcome_message(board_size, number_of_ships)


main()