function freq_i = cochlear(freq, displ)
dist = abs(displ)
[M,I] = max(dist)
freq_i = freq(I)
phase = unwrap(angle(displ))
phase_gradient = diff(phase)
freq_gradient = diff(freq)
gradient = phase_gradient./freq_gradient
grad = gradient(I)
group_delay = (-1/2*pi)*grad
figure(1)
plot(freq, dist)
figure(2)
plot(freq,phase)
figure(3)
plot(freq(1:end-1), phase_gradient)



