x = -4:0.1:4
y = x.^2
yrand = y + 2*randn(size(x))
pfit = polyfit(x, yrand, 2)
yfit = polyval(pfit, x)
figure(1)
hold on
plot(x, yrand, "r.")
plot(x, yfit, "k")
hold off
