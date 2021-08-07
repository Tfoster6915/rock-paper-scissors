import random
import math

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper,'s' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

#if both user and computer choice the same thing its a tie

    if user == computer:
        return (1, user, computer)
    return (-1, user, computer)
#determine if player wins or looses

    if is_win(user,computer):
        return "You have chosen {} and the computer has chosen {}. YOU won!".format(user, computer)
    return "You have chosen {} and the computer has chosen {}.".format(user,computer)
#last return determines automatically looses
#Next defining winner

def is_win(player, opponent):
    #return true if player beats opponent
    #winner conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # play against the computer untill someone wuns best of n games
    # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)

    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        #tie
        if result == 1:
            player_wins += 1
            print('It is a tie. You and the computer have both chosen {}. \n'.format(user))
            #you win  
        elif result == 1:
            print('You chose {} and the computer chose {}. You won!\n'.format(user, computer))
        else:
            computer_wins += 1
            print('You chose {}  and the computer chose {}. You lost :(\n'.format(user, computer))
        print('\n')

    if player_wins > computer_wins:
        print('You have won the best of {} You are awesome;D'.format(n))
    else:
        print('Sadly, the computer has won the best of {} games. Do better next time!'.format(n))
            
                

if __name__ == '__main__':
    play_best_of(3) #3
 
