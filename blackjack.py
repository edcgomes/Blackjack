import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(list):
  hand=[]
  a= random.choice(list)
  b= random.choice(list)
  hand.append(a)
  hand.append(b)
  return hand

def score(cards_in_hand):
  score_total= sum(cards_in_hand)
  if score_total>21:
    if 11 in cards_in_hand:
      score_total-=10
  return score_total
  
def game():
    user_hand= deal_card(cards)
    computer_hand= deal_card(cards)
    computer_fistcard=(computer_hand[0])
    user_score= score(user_hand)
    computer_score= score(computer_hand)
    print(f"Your cards: {user_hand}, current score: {user_score}")
    print(f"Computer first card: {computer_fistcard}")
    more_cards=True
    while more_cards:
      another_card= input("Type 'y' for another card or 'n' to pass: ")
      if another_card=="y":
        extra_card= random.choice(cards)
        user_hand.append(extra_card)
        user_score= score(user_hand)
        if user_score > 21:
          print(f"Your cards are {user_hand} and your score is {user_score}")
          print(f"Bust! You went above 21. You lose.")
          more_cards=False
          another_game= input("Wanna play again? Type 'y' or 'n': ")
          if another_game== "y":
              break
              game()
        else:
          print(f"Your cards are {user_hand} and current score is {user_score}")
      else:
        print(f"Your final hand is {user_hand}, final score: {user_score}")
        print(f"Computer's final hand is {computer_hand}, final score: {computer_score}")
        if user_score==21 and computer_score !=21:
          print("Blackjack! You won!")
        elif user_score==computer_score:
          print("It's a draw")
        elif user_score>computer_score:
          print("You won!")
        else:
          print("You lose.")
        more_cards=False
        another_game= input("Wanna play again? Type 'y' or 'n': ")
        if another_game== "y":
            game()
           
start= input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start=="y":
    game()

  




