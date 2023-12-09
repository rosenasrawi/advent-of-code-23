from _getinput import *
from collections import Counter
from functools import cmp_to_key

# --- Day 7: Camel Cards ---

def card2nums(card, joker = False):

    card_nums = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    if joker: card_nums['J'] = 0

    card = [card_nums[c] if c in card_nums else int(c) for c in card]

    return card

def check_hand(card):

    nj = card.count(0)

    if nj == 5: return 7

    card = [c for c in card if c != 0]
    counts = list(Counter(card).values())
    counts[counts.index(max(counts))]+= nj

    counts.sort()
    
    if 5 in counts: return 7
    elif 4 in counts: return 6
    elif counts == [2,3]: return 5
    elif counts == [1,1,3]: return 4
    elif counts == [1,2,2]: return 3
    elif len(counts) == 4: return 2
    elif len(counts) == 5: return 1

def sort_cards(hand1, hand2):

    for h1, h2 in zip(hand1[0], hand2[0]):
        if h1 == h2:
            continue
        elif h1 > h2:
            return 1
        elif h1 < h2:
            return -1
    return 0

def get_hands(joker = False):

    input = getinput(day='07', example=False)
    input = [line.split() for line in input]

    cards = [card2nums(list(card),joker) for card, _ in input]
    bids = [int(bid) for _, bid in input]

    hands = [[check_hand(card)] + card for card in cards]
    hands = list(zip(hands,bids))

    return hands

def get_sorted(joker = False):

    hands = get_hands(joker)
    hands = sorted(hands, key = cmp_to_key(sort_cards))

    ranks = list(range(1, len(hands)+1))
    bids = [b for _, b in hands]

    return sum([r * b for r, b in zip(ranks,bids)])

print('Part 1:', get_sorted())
print('Part 2:', get_sorted(joker=True))