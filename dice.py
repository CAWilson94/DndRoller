import abc 
from random import randint

class DiceRoller: 

    def __init__(self, dice, num_rolls):
        self._state = dice # state is represented by number of sides i.e. which dice we are using 
        self.num_rolls = num_rolls

    def request(self):        
        total_dice_num = 0 
        for i in range(1, self.num_rolls): 
            total_dice_num += self._state.roll()
        print(f"Final dice number: {total_dice_num}")


class State(metaclass=abc.ABCMeta): 
    """
        Encapsulating behaviour associated with a particular set of context 
    """

    @abc.abstractmethod
    def roll(self): 
        print("They see me rolling, they hating...")
        randint(0, 100)


class D6Dice(State): 

    def roll(self): 
        random_rolled_number = randint(1, 6)   
        print(f"Rolling 6 sided dice: {random_rolled_number}")   
        return random_rolled_number 

class D4Dice(State): 

    def roll(self): 
        random_rolled_number = randint(1, 4)   
        print(f"Rolling 4 sided dice: {random_rolled_number}")   
        return random_rolled_number

class D8Dice(State): 

    def roll(self): 
        random_rolled_number = randint(1, 8)   
        print(f"Rolling 8 sided dice: {random_rolled_number}")   
        return random_rolled_number

class D12Dice(State): 

    def roll(self): 
        random_rolled_number = randint(1, 12)   
        print(f"Rolling 12 sided dice: {random_rolled_number}")   
        return random_rolled_number

class D10Dice(State): 

    def roll(self): 
        random_rolled_number = randint(1, 10)   
        print(f"Rolling 10 sided dice: {random_rolled_number}") 
        return random_rolled_number

class D100Dice(State): 

    def roll(self): 
        random_rolled_number = randint(1, 10) * 10 
        print(f"Rolling D100 dice: {random_rolled_number} as percentage") 
        return random_rolled_number

class D20Dice(State): 

    def roll(self): 
        random_rolled_number = randint(1, 20)   
        print(f"Rolling 20 sided dice: {random_rolled_number}") 
        return random_rolled_number


def main(): 
    
    d20 = D20Dice()
    dice_roller = DiceRoller(d20, 5)
    random_rolled_num = dice_roller.request()

if __name__ == "__main__":
    main()