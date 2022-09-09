import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer=random.choice(['r','s','p'])

    if user==computer:
        return ("its a tie")

    if iswin(user,computer):
        return("Congrats you won")

    return("Computer won")

def iswin(player,opponent):
    if(player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True

print(play())
