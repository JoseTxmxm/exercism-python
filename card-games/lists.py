"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [number, number+1, number+2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    total_sum = sum(hand)
    num_cards = len(hand)

    average = total_sum / num_cards

    return average

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    if not hand:
        return False
        
    exact_average = sum(hand) / len(hand)

    first = (hand[0])
    last = (hand[-1])

    median_index = len(hand) // 2
    median = (hand[median_index])

    return (first == exact_average or
            last == exact_average or
            median == exact_average)

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_sum = 0
    even_count = 0
    odd_sum = 0
    odd_count = 0


    for i, value in enumerate(hand):
        if i % 2 == 0:
            even_sum += value
            even_count += 1
        else:
            odd_sum += value
            odd_count += 1

    if even_count == 0 or odd_count == 0:
        return False
        
    return (even_sum * odd_count) == (odd_sum * even_count)
    

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand and hand[-1] == 11:
        hand[-1] *= 2
    return hand