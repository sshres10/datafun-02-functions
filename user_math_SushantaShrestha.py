"""
Purpose: Calculate basic statistics of a soccer match.

"""
import math
import logging

# Configure logging
from util_logger import setup_logger
logger, logname = setup_logger(__file__)

def calculate_average_goals(total_goals, total_games):
    """
    Calculate the average goals per game for a soccer team.

    total_goals: Total number of goals scored by the team.
    total_games: Total number of games played by the team.

    return: The average goals per game (rounded to the nearest integer).
    """
    if total_games == 0:
        return 0  # Avoid division by zero if no games have been played.
    
    average = total_goals / total_games
    return round(average)

# Get user input for total goals and total games played
total_goals_scored = int(input("Enter the total number of goals scored: "))
total_games_played = int(input("Enter the total number of games played: "))

# Calculate the average goals per game
average_goals = calculate_average_goals(total_goals_scored, total_games_played)

# Display the result
print(f"The average goals per game is: {average_goals}")

# Explore some functions in the math module
logger.info("Explore some functions in the math module")
logger.info(f"math.comb(5,1) = {math.comb(5,1)}")  # Calling math.comb function
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")

# Log the user input and calculated result
logger.info(f"Total goals scored: {total_goals_scored}")
logger.info(f"Total games played: {total_games_played}")
logger.info(f"Average goals per game: {average_goals}")
