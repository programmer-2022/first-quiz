################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/
#
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function
# should change (x, y) into (y, x).
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in
# `question2_test.py.`

from typing import List, Tuple


def change_position_tuple(tuple: Tuple) -> Tuple:
    """
        Swap the position of elements in a tuple.

        Arguments:
            tuple (Tuple): The input tuple you want to exchange.

        Returns:
            Tuple: a new tuple with the elements swapped.

        Example:
            >>> change_tuple_position(("a", "b"))
            ('b', 'a')
    """

    return (tuple[1], tuple[0])


def run_swapper(list_of_tuples: List[Tuple]) -> List[Tuple]:
    """
     Applies the change_position_tuple function to each tuple in a list of tuples.

     Args:
         list_of_tuples (List[Tuple]): The list of tuples on which the swap will be applied.

     Returns:
         List[Tuple]: A new list of tuples with the swapped elements.

     Example:
         >>> run_swapper([("a", "b"), ("c", "d")])
         [('b', 'a'), ('d', 'c')]
     """

    return list(map(change_position_tuple, list_of_tuples))
