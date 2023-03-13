% ### EXestimatePI.m ###      04.22.11 {C. Bergevin}
% Use a random # generator to estimate pi by considering the ratio of areas
% of a circle to a square

clear
% -----------
N=1000;      % # of points to use
% -----------
figure(1); clf; hold on; grid on; 
% +++
% generate array of (uniformly distributed) x and y values
A= 2*rand(N,1)-1;   % x coord.
B= 2*rand(N,1)-1;   % y coord.
% +++
% loop thru to test if each coordinate pair is inside or out
Ac= 0;  % indexer
for nn=1:N
    x= A(nn); y= B(nn);
    % test to see if the point falls within the unit circle (i.e., within
    % it area); if so, update indexer
    if (sqrt(x^2+y^2) <= 1),    Ac= Ac+1;   end
    plot(x,y,'kx','LineWidth',1);     % also plot for visual purposes
end
% +++
% estimate pi as the ratio of the areas
piEST= 4*(Ac/N); fprintf('\n estimate for pi = %g (using %g points) \n\n',piEST, N);
% +++
axis([-1 1 -1 1]);  xlabel('x'); ylabel('y')
% also draw a unit circle
theta= linspace(0,2*pi,100); xC= cos(theta); yC= sin(theta); plot(xC,yC,'r-','LineWidth',2);