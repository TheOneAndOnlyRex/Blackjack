import random
#the cards
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "Ace"]
money = 250
game = True
card_values = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "Jack" : 10,
    "Queen" : 10, 
    "King" : 10,
    "Ace" : 1
}

def calculate_hand(hand):
    total = 0

    for card in hand:
        value = card.split(" ")[0]
        total += card_values[value]
        
    return total


#creating the deck of cards + shuffling
deck = [card + " of " + suit for card in cards for suit in suits]
random.shuffle(deck)


player_busted = False
#Player turn
while money > 0 and game == True:
    #deck of cards
    deck = [card + " of " + suit for card in cards for suit in suits]
    random.shuffle(deck)
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    player_bet = int(input("\nYou have $" + str(money) + ". How much do you want to wager? "))
    

    while player_bet > money:
        print("\nNot enough money, try a smaller amount.")
        player_bet = int(input("\nYou have $" + str(money) + ". How much do you want to wager? "))
        
    print("\nYour balance now is: $" + str(money - player_bet))

    print("\nYour hand: " + str(player_hand))
    print("\nDealer's Visible Card: ")
    print(dealer_hand[0])
    player_value = calculate_hand(player_hand)
    print("\nYou are at " + str(player_value) + " points")
    
    while True:
        choice = input("Want to hit or stand? ")
        player_busted = False
    
        if choice == "hit": 
            new_card = deck.pop()
            player_hand.append(new_card)
            print("You drew: " + new_card)
            player_value = calculate_hand(player_hand)
            print("Your are now at: " + str(player_value))
    
        if player_value > 21:
            print("You Bust!")
            print("\nYou lose $" + str(player_bet))
            money -= player_bet
            player_busted = True
            break

        elif choice == "stand":
            print("\nYou stand at " + str(player_value))
            break
        
    #dealer's turn
    if not player_busted:
        print("Dealer's turn")
        dealer_total = calculate_hand(dealer_hand)
       
        while dealer_total <= 17:
            new_card = deck.pop()
            dealer_hand.append(new_card)
            dealer_total = calculate_hand(dealer_hand)
            print("The Dealer drew " + str(new_card) +  "\nThe Dealer is at: " + str(dealer_total) + " points.")

        if dealer_total >= 17 and dealer_total <= 21:
            print("The dealer stands at " +str(dealer_total))

        if dealer_total > 21: 
            print("The dealer busted!")
            print("\nYou got the money you wagered back.")
        else:
            if dealer_total > player_value:
                print("The Dealer Won.")
                print("\nYou lose $" + str(player_bet))
                money -= player_bet
            
            elif dealer_total < player_value:
                print("\nYou won!")
                print("You gained $" + str(player_bet))
                money += (player_bet)
            
            elif dealer_total == player_value:
                print("It's a tie!")
                print("\nYou got the money you wagered back: $" + str(player_bet))

    if money > 0:
        play_again = input("Want to play again? y or n: ")
        if play_again == "y":
            game = True
        if play_again == "n":
            print("Thank you for playing. You walk away with " + str(money) + "$")
            game = False
    else: 
        print("Game Over. You went bankrupt.")





    