

N = 100000;
v1 = linspace(1,10,N);
v2 = zeros(1,N);

tic

for i = 1:length(v1)
    
    v2(i) = v1(i)^2;
    break;
    
end

toc

figure(1);
a = plot(v1,v2,'color',[0.5 0.1 0.2],'linestyle','--','linewidth',1.5);
xlabel('v1');
ylabel('v2');
legend('v1^2');

