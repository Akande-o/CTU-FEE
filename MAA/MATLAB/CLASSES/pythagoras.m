function [c, a, b] = pythagoras(a, b)
    
    if nargin == 2
       c = sqrt(a^2 + b^2)
       
    elseif nargin == 1
        disp("You only inputed one element")
        c = NaN
        b = NaN
        a = NaN
    else nargin == 0
        disp("You didn't pass any argument")
        c = NaN
        b = NaN
        a = NaN
    end