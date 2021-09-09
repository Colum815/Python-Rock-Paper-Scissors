# # PLAYER ONE SET UP
import random

p1_score = 0
p2_score = 0
goes = 0
player_one_flag = True
player_two_flag = True
while goes < 3:

    goes += 1
# -------------------------------------------------- PLAYER ONE INFO----------------------------------------------------
    player_one = ""
    while player_one_flag:
        print("")
        #print("-----------------------------------------------------------------")
        print("Player one: ")
        player_one = input("Rock,Paper,Scissors: ").lower()
        if player_one == "rock":
            print("Player one chose rock")
            break
        elif player_one == "paper":
            print("Player one chose paper")
            break
        elif player_one == "scissors":
            print("Player one chose scissors")
            break
    print("-----------------------------------------------------------------")
# -------------------------------------------------- PLAYER TWO INFO----------------------------------------------------
    while player_two_flag:

        print("Computers turn: ")
        print("Rock,Paper,Scissors: ")
        my_list = ["rock", "paper", "scissors"]
        player_two = random.choice(my_list)
        print("Computer picked", player_two)
        break
    print("-----------------------------------------------------------------")
# -------------------------------------------WINNING CONDITION SECTION--------------------------------------------------

    if player_one == "rock" and player_two == "scissors":
        p1_score += 1
        print("Player one wins")
        print("-----------------------------------------------------------------")
    elif player_one == "scissors" and player_two == "paper":
        p1_score += 1
        print("Player one wins")
        print("-----------------------------------------------------------------")
    elif player_one == "paper" and player_two == "rock":
        p1_score += 1
        print("Player one wins")
        print("-----------------------------------------------------------------")
    elif player_two == "rock" and player_one == "scissors":
        p2_score += 1
        print("Computer wins")
    elif player_two == "scissors" and player_one == "paper":
        p2_score += 1
        print("Computer wins")
    elif player_two == "paper" and player_one == "rock":
        p2_score += 1
        print("Computer wins")
    elif player_two == player_one:
        print("Draw")
# --------------------------------------------------OUTPUT WINNER-------------------------------------------------------
print("Three rounds are up")
if p1_score > p2_score:
    print("Player one: ", p1_score,"\n Computer:", p2_score)
    print("Player one wins")
elif p2_score > p1_score:
    print("Computer: ", p2_score,"\n Player one:", p1_score)
    print("Computer wins")
else:
    print("-----------------------------------------------------------------")
    print("The final score is a Draw")
    print("-----------------------------------------------------------------")

