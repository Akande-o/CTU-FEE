

x = -3:0.01:3;  % x-axis for exponential functions

N = 3;
y = zeros(size(x)); % creates vector of zeros

for n = 0:N
    y = y + x.^n/factorial(n);
end


% this creates two plots in one figure (plots are in one column)
figure(1);
subplot(1,2,1);
% plot(x,y,'k-');
loglog(x,y,'k-'); % both axis are log scaled
subplot(1,2,2);
plot(x,exp(x),'r--');
