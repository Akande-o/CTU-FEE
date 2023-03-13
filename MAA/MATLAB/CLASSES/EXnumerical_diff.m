% numerical differentiation

x = 0:0.01:2*pi;

y = @(x)sin(x);
dy = @(x)cos(x);
dny = diff(y(x)); % one possiblity how to approximate derivation
dny2 = gradient(y(x)); % another possiblity by function gradient

figure(1); clf;
hold on;
plot(x,y(x),'k-');
plot(x,dy(x),'b-');
plot(x(1:end-1),dny/0.01,'r--');
plot(x,dny2/0.01,'g--');
hold off;