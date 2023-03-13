function s = my_sqrt(x)
% function s = my_sqrt(x)
%
% function which calculates square root of argument x

s = 1;

kmax = 10;
figure(1)
hold on; % new call of the plot function will 
plot(1:kmax,sqrt(x)*ones(1,kmax),'--');
%not erase the previous content but adds to the previous content of the graph

for k=1:kmax
    s = 0.5*(s + x/s);
    plot(k,s,'+')
end

