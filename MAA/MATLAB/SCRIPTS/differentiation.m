%% Comparison of the two functions of differentiation in Matlab
% Comparing both diff() and gradient() functions
Y = -1:0.05:1;
h = 0.05
Z=(1./(1+exp(-Y./0.1)));
Zrand = Z + 0.01*randn(size(Y))
Ydiff = Y(2:end)
Zdiff = diff(Z)./h
Zgrad = gradient(Z)./h
Zdiffr = diff(Zrand)./h
Zgradr = gradient(Zrand)./h
figure(1)
hold on
plot(Y(2:end), Zdiff)
plot(Y(2:end), Zdiffr, "+")
xlabel("Y")
ylabel("Sigmoid")
title("Using the diff()function")
legend("Sigmoid without noise", "Sigmoid with noise")
hold off
figure(2)
hold on
plot(Y, Zgrad)
plot(Y, Zgradr, "o")
xlabel("Y")
ylabel("Sigmoid")
title("Using the gradient()function")
legend("Sigmoid without noise", "Sigmoid with noise")
hold off
% We can clearly see from the graphs that the gradient function seems to
% give a better and more precise result

%%Comparing the errors when the step size is smaller
Ysm = -1:0.01:1;
h = 0.01
Zsm=(1./(1+exp(-Ysm./0.1)));
Zsmrand = Zsm + 0.01*randn(size(Ysm))
Ysma = Ysm(2:end)
Zsmdiff = diff(Zsm)./h
Zsmgrad = gradient(Zsm)./h
Zsmdiffr = diff(Zsmrand)./h
Zsmgradr = gradient(Zsmrand)./h
figure(3)
subplot(2,1,1);
hold on
plot(Y(2:end), Zdiff)
plot(Y(2:end), Zdiffr, "+")
xlabel("Y")
ylabel("Sigmoid")
title("Using the diff()function")
legend("Sigmoid without noise", "Sigmoid with noise")
hold off
subplot(2,1,2);
hold on
plot(Ysm(2:end), Zsmdiff)
plot(Ysm(2:end), Zsmdiffr, "+")
xlabel("Ysm")
ylabel("Sigmoid")
title("Using the diff()function with smaller step size")
legend("Sigmoid without noise", "Sigmoid with noise")
hold off
figure(4)
subplot(2,1,1);
hold on
plot(Y, Zgrad)
plot(Y, Zgradr, "o")
xlabel("Y")
ylabel("Sigmoid")
title("Using the gradient()function")
legend("Sigmoid without noise", "Sigmoid with noise")
hold off
subplot(2,1,2);
hold on
plot(Ysm, Zsmgrad)
plot(Ysm, Zsmgradr, "o")
xlabel("Ysm")
ylabel("Sigmoid")
title("Using the gradient()function with smaller step size")
legend("Sigmoid without noise", "Sigmoid with noise")
hold off
% From the graphs represented above we can see that with smaller step size
% the error in the deviation becomes larger and more points tend to deviate
% from the original path to the curve