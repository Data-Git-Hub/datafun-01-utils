# Python Code Reusable Module
"""
Module: data-is-fun-part-(number).py

Purpose: Reusable Module for Analytics Projects for NWMSU CSIS
Description: This module provides a byline for my analytics projects. 
Author: Data-Git-Hub

TODO: Change the module name in this opening docstring
"""

#####################################
# Import Modules
#####################################

import statistics

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your boolean variable
free_shipping: bool = True
military_discount = True

# declare an integer variable 
# TODO: Add or replace this with your integer variable
years_in_operation: int = 90

# declare a floating point variable
# TODO: Add or replace this with your floating point variable
average_client_satisfaction_reviews_io: float = 1.3
average_deliver_time_in_days = 7.6
percent_military_discount = 0.1

# declare a list of strings
# TODO: Add or replace this with your list  
product_type_offered = ["Hand Rolled Cigars", "Machine Made Cigars", "Sampler Cigars"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your numeric list  
client_rating_score_reviews_io: list = [1.0, 1.0, 1.5, 2.0, 1.5, 3.0, 1.0, 1.0, 1.0, 1.0, 5.0, 1.0, 1.0, 1.5, 1.5, 2.0, 1.0, 1.0, 1.0]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your numeric list
min_score: float = min(client_rating_score_reviews_io)  
max_score: float = max(client_rating_score_reviews_io)  
mean_score: float = statistics.mean(client_rating_score_reviews_io)  
stdev_score: float = statistics.stdev(client_rating_score_reviews_io)

#####################################
# Define global functions (reusable instructions)
#####################################

#####################################
# Define main() function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything after the colon must be indented consistently (usually four spaces)

    This is used in best practices when coding.
    '''
    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script, then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
