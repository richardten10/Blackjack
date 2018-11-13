import random
from time import sleep

def main():
    setUp()
    counter = setUp.howManyRounds
    while counter>0:
        run()
        counter -=1

def run():
    manageComputerHand.setInitial()
    manageComputerHand.decideIfHitOrStick()
    manageComputerHand.nextMoves()

    managePlayerHand.initialDeal()
    managePlayerHand.choices()

    valueHands.declareWinner()

class setUp():
    print("Let's play blackjack!")
    howManyRounds = input("How many rounds do you want to play?")

class valueHands():
    def valueEach(self):
        pass

    def compare(self):
        pass

    def declareWinner(self):
        pass


class deal():

    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]

    def setNextCard(self):
        rand = random.choice(cards)
        return rand

    def getNextCard(self):
        rand = random.choice(cards)
        return rand

    def dealStarting(self):
        hand =  [getNextCard, getNextCard]

    def dealHit(self):

        pass

class managePlayerHand():
    def initialDeal(self):
        pass

    def hit(self):
        pass

    def stick(self):
        pass

    def manage(self):
        pass

    def choices(self):
        pass

class manageComputerHand():
    def setInitial(self):
        pass

    def getInitial(self):
        pass

    def decideIfHitOrStick(self):
        pass

    def nextMoves(self):
        pass

if __name__ == "__main__":
    main()
