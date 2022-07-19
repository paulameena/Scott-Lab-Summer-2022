#Tutorial on Evolutionary Game Theory, part 1
#as seen on https://www.freecodecamp.org/news/introduction-to-evolutionary-game-theory/


import random

class Bird:
    def __init__(self, strategy):
        """
        Each bird has a strategy type (hawk or dove)
        And a small starting fitness
        """
        self.strategy = strategy
        self.fitness = 10

    def contest(self, opponent, v, c):
       """
       Simulate the outcomes depending on the strategies
       """ 
       # both hawks --> 50:50 battle
       if self.strategy == opponent.strategy == "hawk":
          if random.randint(0, 1) == 1:
                self.fitness = self.fitness + v
                opponent.fitness = opponent.fitness - c
          else:
                self.fitness = self.fitness - c
                opponent.fitness = opponent.fitness + v

            # hawk meets dove

       elif self.strategy == "hawk" != opponent.strategy:
            self.fitness = self.fitness + v
            opponent.fitness = opponent.fitness
       elif self.strategy == "dove" != opponent.strategy:
            self.fitness = self.fitness
            opponent.fitness = opponent.fitness + v

        # both doves --> share the resource

       else:
            self.fitness = self.fitness + v/2
            opponent.fitness = opponent.fitness + v/2

       def spawn(self):
            """
            Allow a small chance of mutation to flip strategy
            Otherwise, return offspring of the same type
            """

            mutation = random.randint(0, 1000) > 999
            if mutation:
                if self.strategy == "dove":
                    return Bird("hawk")
                else:
                    return Bird("dove")
            else:
                return Bird(self.strategy)