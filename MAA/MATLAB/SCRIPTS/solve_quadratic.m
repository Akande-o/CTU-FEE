function[r1, r2] = solve_quadratic(a,b,c)
D = b^2 - 4*a*c;
if D > 0
    disp("There are two distinct solutions to this equation")
    r1 = (-b + sqrt(D))/ 2*a;
    r2 = (-b - sqrt(D))/ 2*a;
elseif D == 0
    disp("There is only one solution to this equation")
    r1 = -b/2*a;
    r2 = r1;
elseif D < 0
    disp("There is no solution for the equation")
    r1 = NaN;
    r2 = NaN;
end
