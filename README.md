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

