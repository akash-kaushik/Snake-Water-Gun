# Snake Water Gun

import random
import playsound

def winner_sound():
    winner_sound_list = ["Winner1.mp3", "Winner2.mp3"]
    sound_winner = random.choice(winner_sound_list)
    playsound.playsound(sound_winner)


def loser_sound():
    loser_sound_list = ["Loser1.mp3", "Loser2.mp3"]
    sound_loser = random.choice(loser_sound_list)
    playsound.playsound(sound_loser)



def tie_sound():
    sound = "Tie.mp3"
    playsound.playsound(sound)


def user_choice():
    a = False
    print("Press:\nS: Snake\nW: Water\nG: Gun:")
    while not a:
        uc = input()
        uc = uc.lower()
        if uc=="s" or uc=="w" or uc=="g":
            a = True
        else:
            print("Please give correct input!")
    return uc

def start_game():
    print("\t\t\tWelcome to Snake Water and Gun game\nThe rule of the Game:\n\t* Single Player Game\n\t* You have to"
          " press\n\t\t* s for Snake\n\t\t* w for Water\n\t\t* g for Gun")
    computer_score = 0
    human_score = 0
    game_played = 0
    start = False
    while not start:
        if not start:
            s = input("Do you want to continue the Game:\nY: Yes\nN: No:")
            s = s.lower()
            if s=="y":
                game_played = game_played + 1
                start = False
                game = False
            elif s=="n":
                start = True
                break
        while not game:
            game_list = ["snake", "water", "gun"]
            human_choice = user_choice()
            computer_choice = random.choice(game_list)[0]
            print(f"You choice {human_choice} and Computer choice {computer_choice}")
            if human_choice == computer_choice:
                print(f"No one win this round!\nComputer Score: {computer_score}\nYour Score: {human_score}")
                game = True
            elif human_choice == "s" and computer_choice == "w":
                human_score = human_score+1
                print(f"You win this round!\nComputer Score: {computer_score}\nYour Score: {human_score}")
                game = True
            elif human_choice == "w" and computer_choice == "g":
                human_score = human_score+1
                print(f"You win this round!\nComputer Score: {computer_score}\nYour Score: {human_score}")
                game = True
            elif human_choice == "g" and computer_choice == "s":
                human_score = human_score+1
                print(f"You win this round!\nComputer Score: {computer_score}\nYour Score: {human_score}")
                game = True
            else:
                computer_score = computer_score+1
                print(f"Computer win this round!\nComputer Score: {computer_score}\nYour Score: {human_score}")
                game = True
    while start:
        print(f"You played {game_played} time's!")
        if human_score == computer_score:
            print("Game Draw!")
            tie_sound()
            print(f"By {human_score} points\n\n\tThanks for Playing!")
            break
        elif human_score < computer_score:
            print("You Lose!")
            loser_sound()
            print(f"Computer Win's! point's {computer_score}\n\n\tThanks for Playing!")
            break
        elif human_score > computer_score:
            print("You Win!")
            winner_sound()
            print(f"Point's {human_score}\n\n\tThanks for Playing!")
            break


start_game()