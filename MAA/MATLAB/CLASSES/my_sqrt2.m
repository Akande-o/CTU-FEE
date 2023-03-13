function s = my_sqrt2(x)
% function s = my_sqrt2(x)
%
% function which calculates square root of argument x by using a while loop

s = 1; % initial condition 


while abs(s - sqrt(x)) > 1e0
    s = 0.5*(s + x/s);

end

