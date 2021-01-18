# View is a module that holds functions for printing and getting information from the user.
import Model as M
import time
import os
import sys
from pygame import mixer


def askYesNo(question: str, default="yes"):
    """
    Prompts user for yes or no input for a given question.
    :param question: string question
    :param default: default answer
    :return:
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def askForName():
    """
    Prompts user for name input.
    :return:
    """
    return input("Please type your name: ")


def getHitChoice(player: M.Player):
    """
    Gets players hit or stand decision.
    :param player:
    :return:
    """
    if isinstance(player, M.Dealer):
        time.sleep(1)
        return player.hitDecision()
    else:
        answer = input("Would you like to hit or stand? H/S: ")
        if answer.lower() == 'h' or answer.lower() == 'hit':
            return True
        elif answer.lower() == 's' or answer.lower() == 'stand':
            return False
        else:
            print("Invalid answer please input H or S!")
            getHitChoice(player)


def printBusted(player: M.Player):
    """
    Prints busted message.
    :param player:
    :return:
    """
    if isinstance(player, M.Dealer):
        print(player.name.upper() + " BUSTED!!")
    else:
        print("YOU BUSTED!")


def printVictory(player: M.Player):
    """
    Prints victory message.
    :param player:
    :return:
    """
    if isinstance(player, str):
        print(player + " WINS!!!")
    elif isinstance(player, M.Dealer):
        print(player.name.upper() + " WINS!!!")
    else:
        print("YOU WIN!!!")


def printHand(player: M.Player, showDealer: bool):
    """
    prints players hand
    :param player:
    :param showDealer:
    :return:
    """
    if not showDealer and isinstance(player, M.Dealer):
        print("Dealer Hand:\n " + str(player.hand.hand[0]))
    else:
        hand = ""
        for card in player.hand:
            hand = hand + " " + str(card)
        if isinstance(player, M.Dealer):
            print("Dealers Hand:\n" + hand + " Total: " + str(player.hand.total()))
        else:
            print("Your Hand:\n" + hand + " Total: " + str(player.hand.total()))


def clearTerminal():
    """
    clears the terminal
    :return:
    """
    time.sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')


def printTable(dealer: M.Player, player:M.Player, showDealer: bool):
    """
    prints current table.
    :param dealer:
    :param player:
    :param showDealer:
    :return:
    """
    printHand(dealer, showDealer)
    printHand(player, showDealer)


def playMusic():
    """
    Plays game music.
    :return:
    """
    mixer.init()
    mixer.music.load('Music/Duel.mp3')
    mixer.music.play()
    time.sleep(3.9)
    mixer.music.load('Music/CBBop.mp3')
    mixer.music.play(loops=-1, start=1)
