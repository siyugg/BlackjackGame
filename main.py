from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
total_score = []
dealer_score = []


def deal_card():
    rt1_card = random.choice(cards)
    return rt1_card

def pcheck_11(pscore):
    if 11 in total_score:
        if pscore>21:
            index = total_score.index('11')
            total_score[index] = 1
    else:
        pass

def dcheck_11(dscore):
    if 11 in dealer_score:
        if dscore>21:
            index=dealer_score.index('11')
            dealer_score[index] = 1
    else:
        pass

def computer_max():
    while sum(dealer_score) < 21:
        if sum(dealer_score) <= 15:
            dnew = deal_card()
            dealer_score.append(dnew)
        elif sum(dealer_score) > 15:
            tf = random.randrange(0, 1)
            if tf == '1':
                dnew = deal_card()
                dealer_score.append(dnew)


def win_lose(pscore, dscore):
    if pscore<=21 and dscore<=21:
        if pscore > dscore:
            print("You Win!")
        elif pscore < dscore:
            print("You lose!")
        elif pscore == dscore:
            print("It's a tie!")
    elif pscore <= 21 and dscore > 21:
        print("You Win!")
    elif pscore > 21:
        if dscore > 21:
            print("It's a tie!")
        elif dscore <= 21:
            print("You lose!")


start = input("Do you want to play a game of blackjack? y or n: ")
while start == 'y':
    print(logo)
    card1 = deal_card()
    card2 = deal_card()
    total_score.append(card1)
    total_score.append(card2)
    print(f"Your cards : {total_score}, current score: {sum(total_score)}")

    dealer_card1 = deal_card()
    dealer_card2 = deal_card()
    dealer_score.append(dealer_card1)
    dealer_score.append(dealer_card2)
    computer_max()
    print(f"Computer's first card: {dealer_card1}")

    next_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if next_card == 'n':
        pscore = sum(total_score)
        dscore = sum(dealer_score)
        win_lose(int(pscore), int(dscore))
    while next_card == 'y':
        new_card = deal_card()
        total_score.append(new_card)
        pscore = sum(total_score)
        dscore = sum(dealer_score)
        pcheck_11(pscore)
        dcheck_11(dscore)
        print(f"Your cards: {total_score}, current score: {pscore}")
        next_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if next_card == 'n':
            win_lose(pscore, dscore)

    print(f"Your final hand: {total_score}, final score: {sum(total_score)}")
    print(f"Computer's final hand: {dealer_score}, final score: {sum(dealer_score)}")
    start = 'n'