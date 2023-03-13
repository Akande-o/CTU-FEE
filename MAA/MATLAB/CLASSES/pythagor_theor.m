function [c, a, b] = pythagor_theor(a,b)

% calculate length of c side in right angle triangle

if nargin == 2 % two arguments
    
    c = sqrt(a^2 + b^2);
    
elseif nargin == 1  % passing a single argument
    
    disp('You passed only one argument')
    
    c =NaN;
    a = NaN;
    b = NaN;
    
elseif nargin ==0 % calling a function without argument
    disp('You didnot pass any argument')
    
    c =NaN;
    a = NaN;
    b = NaN;
    
end




