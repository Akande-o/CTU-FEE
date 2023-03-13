function [c, a, b] = pythagor_theor_default(a,b)

% calculate length of c side in right angle triangle

if nargin < 2 b = 2; end
if nargin < 1 a = 1; end

c = sqrt(a^2 + b^2);
    
