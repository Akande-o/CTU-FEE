balls = []
for i in range(1, 13):
    balls.append(i)
ball = (balls[:6])
ball1 = balls[6:]
print(ball1)
print(ball)
def solve(weigh):
    for i in range(1, 12, 2):
        if i == 1:
            heavier = weigh([i], [i+1])
            if heavier != "none":
                heavy_1 = weigh([i+2], [i])
                
                if heavy_1 == "none":
                    heavy_2 = weigh([i+1], [i+2])
                    if heavier == "left" and heavy_2 == "right":
                        return (i+1, "-")
                    else:
                        return (i+1, "+")
                else:
                    if heavier == "left" and heavy_1 == "right":
                        return (i, "+")
                    else:
                        return (i, "-")
            
        elif i > 2 and i < 10:
            heavier = weigh([i], [i+1])
            if heavier != "none":
                heavy_1 = weigh([i-1], [i])
                
                if heavy_1 == "none":
                    heavy_2 = weigh([i+1], [i+2])
                    if heavier == "left" and heavy_2 == "right":
                        return (i+1, "-")
                    else:
                        return (i+1, "+")
                else:
                    if heavier == "left" and heavy_1 == "right":
                        return (i, "+")
                    else:
                        return (i, "-")
                
        else:
            heavier = weigh([i], [i+1])
            if heavier != "none":
                heavy_1 = weigh([i-1], [i])
                
                if heavy_1 == "none":
                    heavy_2 = weigh([i+1], [i-1])
                    if heavier == "left" and heavy_2 == "right":
                        return (i+1, "-")
                    else:
                        return (i+1, "+")
                else:
                    if heavier == "left" and heavy_1 == "right":
                        return (i, "+")
                    else:
                        return (i, "-")