function grade = grade_classification(x)
if nargin < 1
    disp("There is no input parameter. Please input an integer between 0 and 100")
else
    if x <= 50
        grade = 'F'
    elseif x<=60
        grade = 'E'
    elseif x<=70
        grade = 'D'
    elseif x <= 80
        grade = 'C'
    elseif x<=90
        grade = 'B'
    else
        grade = 'A'
    end
end
