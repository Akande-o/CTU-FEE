% Example of animation


p0 = [0.1 0.2 0.1 0.005 0.1];

N = 100; 
x = linspace(-1.4,0.4,N);

E = @(x) p0(1)*x.^4 + p0(2)*x.^3 + p0(3)*x.^2 + p0(4)*x + p0(5);
xP = E(x);

figure;
hold on;
plot(x,xP,'r');
p = plot(x(1),xP(1),'bo','linewidth',1.5);
for n=1:length(xP)
   p.XData = x(n); p.YData = xP(n); 
   pause(0.1);
   drawnow
   
end