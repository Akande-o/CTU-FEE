#!/bin/python3
# -*- encoding: utf-8 -*-
def solve(weigh):
    """The function takes solves a puzzle for which we have 12 balls and only 1 of them is different 
    and we find the different ball.
    Parameters:
    weigh - The method to the earlier defined class Balls that finds out which side (left or right) is heavier
    Returns:
    A tuple of the different ball number and whether it is heavier than all others or lighter 
    """
    # Initialise the list of balls in the puzzle
    balls = []
    #Appending the balls 1 ... 12 into the list balls
    for i in range(1, 13):
        balls.append(i)
    # We split the balls into two groups of 6 balls each (balls 1 to 6 and 7 to 12)
    heavier = weigh(balls[:6], balls[6:])

    # Considering the condition where the heavier ball is on the left(1 - 6)
    if heavier == "left":
        # Now on the left side of the balance, we split them into 2 groups ([1-3], [4-6])
        heavy_1 = weigh(balls[:3], balls[3:6])
        if heavy_1 == "left":      # If it is heavier on the left side([1-3])
            heavy_2 = weigh([balls[0]], [balls[1]]) # Weigh the balls 1 and 2 to see which is heavier among the three
            if heavy_2 == "left":  # If it is heavier on the left 
                return (balls[0], "+")
            elif heavy_2 == "right":   # If it is heavier on the right
                return (balls[1], "+")
            else:                      # If they are both of the same size
                return(balls[2], "+" )
        elif heavy_1 == "right":     # If it is heavier on the right side([4-6])
            heavy_2 = weigh([balls[3]], [balls[4]])  # Weigh the balls 4 and 5 to see which is heavier among the three
            if heavy_2 == "left":                 # if it is heavier on the left
                return (balls[3], "+")
            elif heavy_2 == "right":              # if it is heavier on the right
                return (balls[4], "+")
            else:                                 # if they are both the same size
                return(balls[5], "+" )
        
        # Now, we know that it is heavier on the left. Then, we are considering if the ball is lighter than the others
        # then so when we use ([1-3], [4-6]) are all the same size
        else:
            # We split the balls into two groups of 6 balls each (balls 7 to 9 and 10 to 12)
            heavy_2 = weigh(balls[6:9], balls[9:12])
            if heavy_2 == "left":      # if it is heavier on the left then we know the different ball is on the right
                heavy_3 = weigh([balls[9]], [balls[10]])  # Weight the balls 10 and 11 to see which is heavier among the three
                if heavy_3 == "left":    # if it is heavier on the left
                    return (balls[10], "-")
                elif heavy_3 == "right":   # if it is heavier on the right
                    return (balls[9], "-")
                else:                       # if they are both the same size
                    return (balls[11], "-")
            else:                         # if it is heavier on the right then we know the different ball is on the left
                heavy_3 = weigh([balls[6]], [balls[7]])  # Weigh the balls 7 and 8 to see which is heavier among the three
                if heavy_3 == "left":      # if it is heavier on the left
                    return (balls[7], "-")
                elif heavy_3 == "right":   # if it is heavier on the right
                    return (balls[6], "-")
                else:                      # if they are both the same size
                    return (balls[8], "-")
    # Considering the condition where the heavier ball is on the right(7 - 12)
    else:
        # Now on the left side of the balance, we split them into 2 groups ([7-9], [10-12])
        heavy_1 = weigh(balls[6:9], balls[9:12])
        if heavy_1 == "left":       # If it is heavier on the left side([7-9])
            heavy_2 = weigh([balls[6]], [balls[7]])  # Weigh the balls 7 and 8 to see which is heavier among the three
            if heavy_2 == "left":   # if it is heavier on the left
                return (balls[6], "+")
            elif heavy_2 == "right":  # if it is heavier on the right
                return (balls[7], "+")
            else:                     # if they are both the same size
                return(balls[8], "+" )
        elif heavy_1 == "right":       # if it is heavier on the right side[10-12]
            heavy_2 = weigh([balls[9]], [balls[10]])  #Weigh the balls 10 and 11 to see which is heavier among the three
            if heavy_2 == "left":     # if it is heavier on the left
                return (balls[9], "+")
            elif heavy_2 == "right":   # if it is heavier on the right
                return (balls[10], "+")
            else:                       # if they are both the same size
                return(balls[11], "+" )
        # Now, we know that it is heavier on the right. Then, we are considering if the ball is lighter than the others
        # then so when we use ([7-9], [10-12]) are all the same size
        else:
            heavy_2 = weigh(balls[:3], balls[3:6])
            if heavy_2 == "left":   # if it is heavier on the left then we know the different ball is on the right
                heavy_3 = weigh([balls[3]], [balls[4]])  #Weigh the balls 4 and 5 to see which is heavier among the three
                if heavy_3 == "left":     # if it is heavier on the left
                    return (balls[4], "-")
                elif heavy_3 == "right":  # if it is heavier on the right
                    return (balls[3], "-")
                else:                     # if they are of the same size
                    return (balls[5], "-")
            else:                  # if it is heavier on the right then we know the different ball is on the left
                heavy_3 = weigh([balls[0]], [balls[1]])  # Weigh the balls 1 and 2 to see which is heavier
                if heavy_3 == "left":  # if it is heavier on the left
                    return (balls[1], "-")
                elif heavy_3 == "right":   # if it is heavier on the right
                    return (balls[0], "-")
                else:                      # if they are of the same size
                    return (balls[2], "-")




        
