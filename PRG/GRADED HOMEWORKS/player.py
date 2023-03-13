class MyPlayer:
    """ A simple player for prisoner's dilemma"""
    def __init__(self, payoff, num = 0):
        """
        Attributes:
        payoff - the 2 by 2 matrix in the form of a tuple which generates the points 
        for each choice made with reference to the opponents choice
        num - the number of iterations(rounds) of the entire game
        my_last - my player's last choice
        opp_last - my opponent's last choice
        """
        self.payoff = payoff
        self.num = num
        self.my_last = None
        self.opp_last = None
 
    def move(self):
        """Returns my current choice based on my last choice and my opponent's last choice"""
        if self.num != 0:
            if self.opp_last is None:
                return False
            elif self.my_last == True and self.opp_last == False:
                return True
            elif self.my_last == True and self.opp_last == True:
                return True
            elif self.my_last == False and self.opp_last == True:
                return True
            else:
                return False
        else:
            if self.opp_last is None:
                return False
            elif self.my_last == True and self.opp_last == False:
                return True
            elif self.my_last == True and self.opp_last == True:
                return True
            elif self.my_last == False and self.opp_last == True:
                return True
            else:
                return False

            
    def record_last_moves(self, my_last, opp_last):
        """
        Parameters:
        my_last - my player's last choice
        opp_last - my opponent's last choice
        """
        self.my_last = my_last
        self.opp_last = opp_last