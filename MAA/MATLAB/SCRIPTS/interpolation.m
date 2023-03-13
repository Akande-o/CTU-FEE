X = [0 1 2 3 4 5 6]
Y = [0 0.8415 0.9093 0.1411 -0.7568 -0.9589 -0.2794]
Xi = 0:0.01:6
Y1 = interp1(X,Y, Xi, "linear")
Y2 = interp1(X,Y, Xi, "nearest")
Y3 = interp1(X,Y, Xi, "pchip")
Y4 = interp1(X,Y, Xi, "spline")
figure(3)
hold on
plot(Xi, Y1, "k+")
plot(Xi, Y2, "b+")
plot(Xi, Y3, "r+")
plot(Xi, Y4, "g+")
legend("linear", "nearest", "cubic", "spline")
hold off

