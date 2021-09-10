import random
from os import system, name

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, comp_score):
    if user_score == comp_score:
        return "DRAW"
    elif comp_score == 0:
        return "Opponent has the Black Jack"
    elif user_score == 0:
        return "Win with a black jack"
    elif user_score > 21:
        return "You lose. Sum over 21"
    elif comp_score > 21:
        return "Opponent went over you win!!!!"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You Lose!!!"


def setup_cards(computer_cards, user_cards):
    clear()
    user_cards.clear()
    computer_cards.clear()

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


def play_game():
    user_cards = []
    computer_cards = []
    game_over = False

    setup_cards(computer_cards, user_cards)

    while not game_over:
        user_score = cal_score(user_cards)
        comp_score = cal_score(computer_cards)

        print(f"   Your cards : {user_cards}, Current Score : {user_score}")
        print(f"   Computer's first card : {computer_cards[0]}, Computer's Score : {comp_score} ")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            should_deal = input("Type y to get another card and n to stop")
            if should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = cal_score(computer_cards)

    print(f"   Your Final cards : {user_cards}, final score : {user_score}")
    print(f"   Computer's Final cards : {computer_cards}, final score : {comp_score}")
    print(compare(user_score, comp_score))


while input("Do you want to play again ? Type y to continue : ") == "y":
    clear()
    play_game()
