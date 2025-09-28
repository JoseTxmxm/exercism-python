"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """


    if card in ['J', 'K', 'Q']:
        return 10

    elif card == 'A':
        return 1

    else:
        try:
            return int(card)
        except ValueError:
            raise ValueError(f"Invalid card: {card}")

    
def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_value = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
    }
    card_one_value = card_value.get(card_one)
    card_two_value = card_value.get(card_two)

    if card_one_value > card_two_value:
        return card_one
    elif card_two_value > card_one_value:
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    card_value = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11, 
        '10': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
    }

    card_one_value = card_value.get(card_one)
    card_two_value = card_value.get(card_two)
    hand_value = card_one_value + card_two_value

    if hand_value <= 10:
        return 11
    else:
        return 1
    

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    card_value = {
        'J': 10,
        'Q': 10, 
        'K': 10,
        'A': 11, 
        '10': 10,
    }
    card_one_value = card_value.get(card_one)
    card_two_value = card_value.get(card_two)
        
    return (card_one_value == 11 and card_two_value == 10) or (card_one_value == 10 and card_two_value == 11)


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    card_value = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11, 
        '10': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
    }

    card_one_value = card_value[card_one] if card_one in card_value else int(card_one)
    card_two_value = card_value[card_two] if card_two in card_value else int(card_two)
    
    return card_one_value == card_two_value
    

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    card_value = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11,
        '10': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
    }

    try:
        value_one = card_value[str(card_one)]
        value_two = card_value[str(card_two)]
    
        total = value_one + value_two
    
        total -= 10 if total > 21 and (value_one == 11 or value_two == 11) else 0

        has_ace = card_one == 'A' or card_two == 'A'

    except KeyError:
        return False
    is_not_pair_of_aces = not (card_one == 'A' and card_two == 'A')
    return (9 <= total <= 11 or has_ace) and is_not_pair_of_aces
    