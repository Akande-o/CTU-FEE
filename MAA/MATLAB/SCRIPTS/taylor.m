x = -2*pi:0.01:2*pi;
% initialising the number of terms for each angle in x
y = [];
% iterating through each angle to get the error of e-3
for k = x
    n = 0;
    T = -2*pi;
    % getting the number of terms required for each angle to get an error
    % of maximum e-3
    while abs(T - sin(k)) > exp(-3)
        i = 0:n;
        t = ((-1).^i).* k.^(2.*i+1)./factorial(2.*i+1);
        T = sum(t);
        n = n+1;
    end
    % adding each number of terms to the vector
    y(end+1) = n;
end
%The number of terms required to get an error of maximum e-3
num = max(y)
    




        