%% This is the solution that we were able to discuss earlier today.
%Unfortunately, as you might have guessed it is not completely precise. It
%gives the same estimate to an extra base and two extra bases of 10 (i.e
%when n= 1000 and 10000 so it is not completely accuarate.
min_values = []
xvalues = linspace(-pi,pi,100)
for i = 1:length(xvalues)- 1
    disp(i)
    xmin = fminbnd(@(x)cos(4*x)*sin(10*x)*exp(-abs(x)),xvalues(i), xvalues(i+1))
    min_values(end+1) = xmin
end
y_values = cos(4.*min_values).*sin(10.*min_values).*exp(-abs(min_values))
min_y = min(y_values)
index = find(y_values == min_y)
min_x = min_values(index)
x = -pi:0.1:pi
y = cos(4.*x).*sin(10.*x).*exp(-abs(x))
figure(2)
hold on
plot(x, y)
hold off

%Also I would like to note that the minimum y value calculated and
%thatshown on the graph are quite different. I think that is something
%worth thinking about.

%% The estimate is the same as when one uses fminsearch method as shown below
% So I'm assuming this is the best I can produce using these methods that
% I'm aware of or the graph is not completely accurate with its points.
% Either way, I hope you find this helpful
x0 = 0
xmin = fminsearch(@(x)cos(4*x)*sin(10*x)*exp(-abs(x)),x0)