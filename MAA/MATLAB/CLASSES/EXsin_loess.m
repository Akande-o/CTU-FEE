% loess example

x = 0:0.01:2*pi;

y = sin(x);  % sine of x

yn = y + randn(size(x));

ys = smooth(x,yn,0.5,'loess');
ysr = smooth(x,yn,0.5,'rloess');

figure(1); clf;
hold on;
plot(x,yn,'.','markersize',7);
plot(x,y,'k-','linewidth',1.5);
plot(x,ys,'r-','linewidth',1.5);
plot(x,ysr,'g-','linewidth',1.5);
hold off;
legend('data','sine(x)','loess','rloess','fontsize',14)
xlabel('x','fontsize',15);
ylabel('y','fontsize',15);

