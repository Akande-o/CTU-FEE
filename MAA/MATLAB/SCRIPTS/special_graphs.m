% ### EXclassicCurves.m ###       11.25.14  (C.Bergevin)
% Motivated by DeVries (1994), this code plots a handful of 'classic' curves
% (simply turn on/off below)
% slightly modified o by V. Vencovsky

clear

figure(1);

% +++
% three-leaved rose
if 1==1
    a= 1;   N= 200; 
    theta= linspace(0,2*pi,N);  % polar coord.
    r= a*sin(3*theta);
    x= r.*cos(theta); y= r.*sin(theta);  % convert to Cartesian
end
subplot(2,2,1);
plot(x,y,'k','LineWidth',1); xlabel('x'); ylabel('y');
title('Three-leaved rose');
% +++
% spiral of Galileo
if 1==1
    a= 1;   N= 2000; 
    theta= linspace(0,10*pi,N);  % polar coord.
    r= a*theta.^2;
    x= r.*cos(theta); y= r.*sin(theta);  % convert to Cartesian
end
subplot(2,2,2);
plot(x,y,'k','LineWidth',1); xlabel('x'); ylabel('y');
title('Spiral of Galileo');

% +++
% Witch of Agnesi
if 1==1
    a= 1;   N= 2000; 
    x= linspace(-20,20,N);  % polar coord.
    y= (8*a^3)./(x.^2+4*a^2);
end
subplot(2,2,3);
plot(x,y,'k','LineWidth',1); xlabel('x'); ylabel('y');
title('Witch of Agnesi');
% +++
% Involute of a circle
if 1==1
    a= 1;   N= 200; 
    theta= linspace(0,4*pi,N);  % polar coord.
    x= a*cos(theta)+a*theta.*sin(theta); y= a*sin(theta)-a*theta.*cos(theta);
end
subplot(2,2,4);
plot(x,y,'k','LineWidth',1); xlabel('x'); ylabel('y');
title('Involute of a circle');
% +++
% Cissoid of Diocles
if 1==1
    a= 1;   N= 100; 
    theta= linspace(0,pi,N);  % polar coord.
    r= a*sin(theta).*tan(theta);
    x= r.*cos(theta); y= r.*sin(theta);  % convert to Cartesian
end

figure(2);
subplot(2,2,1);
plot(x,y,'k','LineWidth',1); xlabel('x'); ylabel('y');
title('Cissoid of Diocles');
% +++
% Cochleoid
if 1==1
    a= 1;   N= 2000; 
    theta= linspace(0,4*pi,N);  % polar coord.
    r= a*sin(theta)./theta;
    x= r.*cos(theta); y= r.*sin(theta);  % convert to Cartesian
end
subplot(2,2,2);
plot(x,y,'k','LineWidth',1); xlabel('x'); ylabel('y');
title('Cochleoid');
% +++
% Folium of Descartes
if 1==1
    a= 1;   N= 2000; 
    theta= linspace(0.8*pi,1.7*pi,N);  % polar coord.
    r= (3*a*sin(theta).*cos(theta))./((cos(theta)).^3 + (sin(theta)).^3);
    x= r.*cos(theta); y= r.*sin(theta);  % convert to Cartesian
end
subplot(2,2,3);
plot(x,y,'k','LineWidth',1); xlabel('x'); ylabel('y');
title('Folium of Descartes');
% +++
% Lemniscate of Bernoulli
if 1==1
    a= 1;   N= 1000; 
    theta= linspace(-pi/4,pi/4,N);  % polar coord.
    r= sqrt(a^2*cos(2*theta));
    x= r.*cos(theta); y= r.*sin(theta);  % convert to Cartesian
end
subplot(2,2,4);
plot(x,y,'k',-x,-y,'k','LineWidth',1); xlabel('x'); ylabel('y');
title('Lemniscate of Bernoulli');
% +++
% Logairthmic spiral
if 1==1
    a= 0.25;   N= 1000; 
    theta= linspace(0,6*pi,N);  % polar coord.
    r= exp(a*theta);
    x= r.*cos(theta); y= r.*sin(theta);  % convert to Cartesian
end
figure(3)
subplot(2,2,1);
plot(x,y,'k','LineWidth',1); xlabel('x'); ylabel('y');
title('Logarithmic spiral');
% +++
% Fey's butterfly
if 1==1
    N= 5000; 
    theta= linspace(0,14*pi,N);  % polar coord.
    r= exp(cos(theta))-2*cos(4*theta)+ (sin(theta/12)).^5;
    x= r.*cos(theta+pi/2); y= r.*sin(theta+pi/2);  % convert to Cartesian
end
subplot(2,2,2);
plot(x,y,'k','LineWidth',1); xlabel('x'); ylabel('y');
title('Fey''s butterfly');
% +++
% figure(1); clf; plot(x,y,'k.','LineWidth',1); xlabel('x'); ylabel('y');