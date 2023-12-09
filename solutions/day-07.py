from _getinput import *
from collections import Counter

# --- Day 7: Camel Cards ---

def card2nums(card, joker = False):

    card_nums = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    if joker: card_nums['J'] = 0

    card = [card_nums[c] if c in card_nums else int(c) for c in card]

    return card

def get_cards(joker = False):

    input = getinput(day='07', example=False)
    input = [line.split() for line in input]

    cards = [card2nums(list(card),joker) for card, _ in input]
    bids = [int(bid) for _, bid in input]

    return cards, bids

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

def get_hands(joker = False):

    cards, bids = get_cards(joker)
    hands = [check_hand(card) for card in cards]

    cards = list(zip(hands, bids, cards))
    cards = list(sorted(cards, key=lambda x:x[0], reverse=True))    

    return cards

def sort_cards(joker = False):

    cards = get_hands(joker)
    cards_sorted = []

    for i, card in enumerate(cards):
        
        cards_sorted.append(card)

        if len(cards_sorted) != 1:

            move = i

            while True:

                hp, bp, cp = cards_sorted[move-1]
                hn, bn, cn = cards_sorted[move]

                if hp > hn:
                    break

                if hp == hn:

                    for j in range(len(cp)):
                        if cp[j] < cn[j]:
                            cards_sorted[move-1] = [hn, bn, cn]
                            cards_sorted[move] = [hp, bp, cp]
                            break
                        elif cp[j] > cn[j]:
                            break
                    
                move -= 1
                if move == 0: break

    ranks = list(range(len(cards_sorted), 0, -1))
    bids = [b for _, b, _ in cards_sorted]
    total = sum([r*b for r,b in zip(ranks,bids)])

    return total

print('Part 1:', sort_cards())
print('Part 2:', sort_cards(joker=True))