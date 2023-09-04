""" Purpose: 
Create a class that inherits everything from NumericSeries and adds
attributes and methods to soccer performance data.
"""

from numeric_series import NumericSeries  # Import the base class
from util_logger import setup_logger  # Import the logger setup function

logger, logname = setup_logger(__file__)

class SoccerPerformanceSeries(NumericSeries):
    """
    A class representing a series of soccer performance for soccer data.

    (Additional) Attributes:
       team_name (str): the name of the soccer team
    """

    def __init__(self, name, units, data, team_name):
        """
        Initialize the object when first created using the arguments passed in.
        Every class needs an __init__ method to construct a new object.

        @args:
            self (object): the object being created that will hold the real data
            name (str): a short name for this list of numeric data
            units (str): the units in which the data is measured
            data (list): the list of numeric data to be held by the object
            team_name (str): the name of the soccer team
        """

        # First, initialize the parent (super) class with parent's attributes
        super().__init__(name, units, data)

        # Then, initialize our additional specialized attributes
        self.team_name = team_name

    def __str__(self):
        """
        Return a string representation of the instantiated object.

        Returns:
            str: a string representation of the instantiated object
        """
        str = f"SoccerPerformanceSeries for Team: {self.team_name}, name={self.name}, units={self.units}, {len(self.data)} data points: {self.data}"
        return str


if __name__ == "__main__":
    # Create a series of soccer performance data for a team
    team_name = "Team A"

    goals_scored_data = [2, 3, 1, 4, 2, 3]
    games_played_data = [5, 4, 4, 6, 5, 6]

    goals_scored_series = SoccerPerformanceSeries("Goals Scored", "Goals", goals_scored_data, team_name)
    games_played_series = SoccerPerformanceSeries("Games Played", "Games", games_played_data, team_name)

    # Log the soccer performance series and perform some calculations
    logger.info(f"Created Soccer Goals Scored Series: {goals_scored_series}")
    logger.info(f"Created Soccer Games Played Series: {games_played_series}")
    logger.info(f"Team: {team_name}")
    logger.info(f"Total Goals Scored: {goals_scored_series.sum()}")
    logger.info(f"Total Games Played: {games_played_series.sum()}")
    logger.info(f"Average Goals Scored per Game: {goals_scored_series.mean()}")
    logger.info(f"Average Games Played per Season: {games_played_series.mean()}")
