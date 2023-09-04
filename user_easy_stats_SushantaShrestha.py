"""
Purpose: Calculate basic statistics of a soccer match.

"""
import math
import statistics


# Configure logging
from util_logger import setup_logger
logger, logname = setup_logger(__file__)

# Sample Data: Number of Games Played (x) and count of wins (y)
matches_played = [10, 15, 20, 25, 30, 35, 40]
goals_scored = [2, 4, 5, 8, 10, 12, 15]

# Calculate statistics for X (Number of Matches Played) and Y (Goals Scored)
mean_matches_played = statistics.mean(matches_played)
median_matches_played = statistics.median(matches_played)
mode_matches_played = statistics.mode(matches_played)
variance_matches_played = round(statistics.variance(matches_played), 2)
std_dev_matches_played = round(statistics.stdev(matches_played), 2)
min_matches_played = min(matches_played)
max_matches_played = max(matches_played)

mean_goals_scored = statistics.mean(goals_scored)
median_goals_scored = statistics.median(goals_scored)

try:
    mode_goals_scored = statistics.mode(goals_scored)
except statistics.StatisticsError:
    mode_goals_scored = "No unique mode found"
variance_goals_scored = round(statistics.variance(goals_scored), 2)
std_dev_goals_scored = round(statistics.stdev(goals_scored), 2)
min_goals_scored = min(goals_scored)
max_goals_scored = max(goals_scored)

# Display statistics for X (Number of Matches Played)
logger.info(f"Mean: {mean_matches_played}")
logger.info(f"Median: {median_matches_played}")
logger.info(f"Mode: {mode_matches_played}")
logger.info(f"Variance: {variance_matches_played}")
logger.info(f"Standard Deviation: {std_dev_matches_played}")
logger.info(f"Smallest: {min_matches_played}")
logger.info(f"Largest: {max_matches_played}")

# Display statistics for Y (Goals Scored)
logger.info(f"Mean: {mean_goals_scored}")
logger.info(f"Median: {median_goals_scored}")
logger.info(f"Mode: {mode_goals_scored}")
logger.info(f"Variance: {variance_goals_scored}")
logger.info(f"Standard Deviation: {std_dev_goals_scored}")
logger.info(f"Smallest: {min_goals_scored}")
logger.info(f"Largest: {max_goals_scored}")