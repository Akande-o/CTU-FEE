v = 50 + 25*randn(1, 20);
for i = 1:length(v)
    if v(i) < 0
        v(i) = 0
    elseif v(i) > 100
        v(i) = 100
    end
end
for i = 1:length(v)
    v_grade(i) = grade_classification(v(i));
end
disp(v_grade)
figure(1)
graph = histogram(v)
xlabel("Integers between 0 and 100")
ylabel("Frequency")

