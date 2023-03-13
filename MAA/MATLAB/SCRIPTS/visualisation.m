%% circle
theta = 0:pi/50:2*pi;
r = 1
x = r*sin(theta)
y = r*cos(theta)
figure(1)
plot(x,y)

%%  ellipse
a = 2
b = 1
t = 0:pi/100:2*pi
x = a.*cos(t)
y = b.*sin(t)
figure(2)
plot(x,y)
xlim([-2,2])
ylim([-2,2])

%% three leavened rose
a = 2
t = 0:pi/100:2*pi
r = a*t
x = r.*cos(t)
y = r.*sin(t)
figure(3)
plot(x,y,'k','LineWidth',1); xlabel('x'); ylabel('y');
title("Spiral of Archimedes")