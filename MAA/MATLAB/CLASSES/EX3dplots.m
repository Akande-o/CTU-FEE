% 3D plots


z = 0:0.01:4*pi;

x = cos(z);
y = sin(z);

figure(1); clf;
plot3(x,y,z);
xlabel('x'); ylabel('y'); zlabel('z');


%% surf plot
N = 25;
[X,Y,Z] = peaks(N);

figure(2); 
surf(X,Y,Z);
shading flat; % remove the black lines in the surf plot
h = colorbar;

figure(3); clf;
numcont = 20;
contour(X,Y,Z,numcont);

figure(4); clf;
waterfall(X,Y,Z);
