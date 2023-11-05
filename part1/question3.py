################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

from typing import List


class Oven:
    """
    This is a class representing a magical oven capable of transforming ingredients into magical results.

    Attributes:
    - ingredients: List of ingredients stored in the oven.
    - result: The result of the transformation, represented as a string.

    Methods:
    - add(element): Add an element to the list of ingredients in the oven.
    - freeze(): Set the oven's result to "snow."
    - boil(): Set the oven's result to "gold."
    - wait(): Set the oven's result to "pizza."
    - get_output(): Return the current result of the oven.

    """

    def __init__(self) -> None:
        """
        Initializes an oven with an empty list of ingredients and an empty result.
        """
        self.ingredients: List = []
        self.result: str = ""

    def add(self, element) -> None:
        """
        Add an element to the list of ingredients in the oven.

        Parameters:
        - element: The element to be added to the list of ingredients.
        """
        self.ingredients.append(element)

    def freeze(self) -> None:
        """
        Set the oven's result to "snow."
        """
        self.result = "snow"

    def boil(self) -> None:
        """
        Set the oven's result to "gold."
        """
        self.result = "gold"

    def wait(self) -> None:
        """
        Set the oven's result to "pizza."
        """
        self.result = "pizza"

    def get_output(self) -> str:
        """
        Return the current result of the oven.

        Returns:
        - The current result of the oven, which is a string.
        """
        return self.result


def make_oven():
    """
    Create an instance of the Oven class and return it.

    Returns:
    - A newly created instance of the Oven class.
    """
    return Oven()


def alchemy_combine(oven, ingredients, temperature):
    """
    Combine ingredients in the oven and set the result based on the temperature.

    Parameters:
    - oven: The oven where the combination will take place.
    - ingredients: A list of ingredients to be combined.
    - temperature: The temperature at which the ingredients will be subjected.

    Returns:
    - The result of the combination, which is a string.
    """
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature > 150:
        oven.boil()
    else:
        oven.wait()

    return oven.get_output()
