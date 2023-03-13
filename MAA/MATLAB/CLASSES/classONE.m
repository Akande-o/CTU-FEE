%% Task 1
% creating the vector v1 by listing it out
v1 = [0 2 4 6 8 10 12]
% creating vectors using the (FROM:STEP:TO) method
v2 = 0:10
v3 = 0:2:10
v4 = -pi/2:pi/4:pi/2
%creating vectors using the FROM,TO,NUMBER method involving linspace or
%logspace function
v5 = linspace(0,10,6)
v6 = logspace(1,2,5)

%% Task 2
v7 = [0 4 10 12 15 16 8] %enumeration
v8 = 0:3:15  %from:step:to
v9 = -4:2:8  %from:step:to
v10 = logspace(1, 5, 5)   %from, to, number
v11 = zeros(1, 4)   % using the zeros function
v12 = ones(1, 3)   %using the ones function

%% Task 3
v13 = [1 2 3]
v14 = [2 3 4]
v15 = v14*2
v16 = v13*v14.'
v17 = v13.*v14
v18 = v13*v14'

%% Task 4
m1 = [1 2 3]
m2 = [1 2 3; 4 5 6; 7 8 9]
a = m2(3, 1)
b = m2(2,:)
c = m2(:,3)

%% Task 5
A = v13'*v14
C = [v1';v2';v1']'
D = [v13 v14]

%% Task 6
lhs = [3 -3 4; 1 6 5; 1 -2 3]
rhs = [30; 7; 17]
U = transpose(lhs\rhs)
U1 = U(1)
U2 = U(2)
U3 = U(3)

%% Task 7
% grouping all the resistance of all resistors into a list
R = [10 20 40 80 100]
%grouping all the voltage of all the resistors into a list
V = [20 22 24 26 30]
%calculating the current and power of each resistor using element wise
%multiplication and grouping them into a list
I = V./R
P = I.*V
TP = P(1) + P(2) + P(3) + P(4) + P(5)

%% Task 8
X = 1:10
Y = 10*X./(X+5)
Z = 100*X./((X+5).*(X+5))
figure(1);
plot(X,Z)
xlabel('x')
ylabel('100x/((x+5)(x+5))')

%% Task 9
t = 0:0.5:2
xt = exp(-t)
yt = t
zt = xt.*yt
t2 = 0:0.1:2;
figure(2);
plot(t2, exp(-t2))
xlabel('t')
xlim([0,2])
set(gca,'XTick',[0 : 0.1 : 2]);
ylabel('x(t) = exp(-t)')
figure(3);
plot(t2, t2)
xlabel('t')
xlim([0,2])
set(gca,'XTick',[0 : 0.1 : 2]);
ylabel('y(t) = t')
figure(4);
plot(t2, t2.*exp(-t2))
xlabel('t')
xlim([0,2])
set(gca,'XTick',[0 : 0.1 : 2]);
ylabel('z(t) = t * exp(-t)')



