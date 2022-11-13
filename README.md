![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome SamSswi,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!


# Battleships Game

The Battleships Game is a Python terminal game running in the Code Institute mock terminal on Heroku.

The users play against the computer in a game where they need to sink the computer's battleships before the computer sinks theirs. A battleship occupies one square on the board.

[This is the live version of the project]()

![Am I responsive image]()

## How to play

The Battleships Game is based on the classical war-themed [Battleship](https://www.thesprucecrafts.com/the-basic-rules-of-battleship-411069) board game, where the two players play against each other trying to guess the location of the opponent's ships. 

The gameplay is straightforward. In this game, the player enters a battle name and two boards are printed with ships randomly generated on them. The player can see their ships on their board, however the computer's ships are concealed. 

The ships are indicated by an "@" symbol. Guesses made on the board are marked with "*" in case of a Hit and with "X" in case of a Miss.

The Battleships Game is turn based. The winner is the participant who manages to sink all the ships of the opponent in the least amount of turns. 

## Features

### Existing Features
- Generating random ships on board
    - The ships of both participants are placed randomly on board
    - The ships of the computer are concealed from the player

![Start game boards]()

- Play against the computer
- The application accepts user input
- The application maintains the score

![Guesses and score update]()

- Input validation and error checking
    - The coordinates entered must be within the grid size
    - The coordinates must be numbers
    - The same guess can't be made twice

![Input validation]()

- The data is maintained in class objects

### Future Features
- The player can select the board size and the number of ships

## Data Model

I used the Board class as my data model. The game creates two objects of the Board class to hold the boards of the player and the computer.

The Board class stores such data as: the board size, the number of ships, the position of the ships on board, the guesses made agaist the board, the board type and the player's name.

The Board class contains methods that help playing the game, such as: a method to print the board (print_board), a method to add ships on the board (add_ships), a method to add a guess and return a result (guess) and a method to randomly generate coordinates for adding the ships on the board (generate_ships).


## Testing 

I've tested the project by doing the following:
    - Passed the code through the PEP8 linter and confirmed there are no problems
    - Given invalid inputs: empty strings and a strings that are too long for the name input; strings, out of bounds numbers, same guess twice, for the coordinate inputs.
    - Tested in my local terminal and in the Code Institute Heroku terminal

 
## Bugs 

None

## Validator Testing

- PEP8
    - **No errors were returned**
    - As a workaround for the [pep8online.com](pep8online.com) validator, I added a PEP8 validator in the Gitpod Workspace.
    - The "pycodestyle" extension was already installed.
    - I pressed "Ctrl + P" in the workspace and typed ">linter" in the search bar.
    - Selected "Python: Select Linter" then selected "pycodestyle".
    - As installing pycodestyle overwrote some original settings, after making sure there were no errors returned, I reverted the settings.
      

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku
- Deployment steps
    - Fork or clone this repository
    - Create a Heroku app
    - Set the buildbacks to Python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click on Deploy

## Credits

- Code Institute for the deployment terminal
- Creating the **Board class** and its structure is taken from Code Institute [Ultimate Battleships](https://p3-battleships.herokuapp.com/) project. [The source where the code was displayed](https://www.youtube.com/watch?v=4sqtzZQpDJE)
- The **init** function is taken from Code Institute [Ultimate Battleships](https://p3-battleships.herokuapp.com/) project.
- The **adding_ships** function is taken from Code Institute [Ultimate Battleships](https://p3-battleships.herokuapp.com/) project.
- The guess function is taken from Code Institute [Ultimate Battleships](https://p3-battleships.herokuapp.com/) project. 
- Ideas to validate the user input: Code Institute [Love Sandwiches]((https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode)) project.
