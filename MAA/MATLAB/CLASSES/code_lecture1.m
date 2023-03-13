


%% created a vektor of angles from 0 to 2pi and calculate a sinusoid of the angle vector

v4 = 0:2*pi/100:2*pi; % created a vector from 0 to 2*pi


y = sin(v4);

figure(99);
plot(v4,y);
xlabel('angle');
ylabel('sin(angle)');



%% operators on vectors and matrices

v1 = [1 2 3];
v2 = [4 5 6];

v3 = v1 .* v2  % element wise multiplication

v3 = v1 * v2.'  % matrix multiplication 1*4 + 2*5 + 3*6 = 32

% [1 2 3] * [4 
%            5
%            6]   

v4 = v1.^2

v5 = v1 ./ v2  % element wise division of (vectors) matrices

%% a system of linear equations

% 2x1 + 3x2 = 20
% 3x1 + 5x2 = 5

A = [2 3; 3 5];
b = [20; 5];

inv(A)*b 

A\b

%% matrix of zeros, matrix of ones

z = zeros(3,3)

o = ones(4,4)


random_numbersI = randn(2,2)  % random numbers with normal distribution
random_numbersII = rand(2,2)  % random numbers with uniform distr between 0 and 1



