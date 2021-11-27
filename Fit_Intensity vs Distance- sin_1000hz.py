import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import intensity_vs_distance

x = intensity_vs_distance.max_voltage_list()[0]
print(x)
y_array = intensity_vs_distance.max_voltage_list()[1]
y = [part[0] for part in y_array]
print(y)

def test(x, a, b, c):
    return a * ((b - x) ** c)


param, param_cov = curve_fit(lambda x, a, b, c: a * (x - b) ** c, x, y, sigma=[0.3] * len(x))

print("Sine function coefficients:")
print(param)
print("Covariance of coefficients:")
print(param_cov)

xs = np.linspace(min(x), max(x), 10 ** 3)
ys = param[0] * (xs - param[1]) ** param[2]
plt.plot(xs, ys, label="fit function")
# plt.errorbar(x, y, yerr=[0.015] * len(x), fmt='o', ecolor='r', label='delta')
x_error = 0.5
y_error = None
plt.errorbar(x, y, yerr=y_error, xerr=x_error, fmt='o', ecolor='black', elinewidth=1, capsize=3, capthick=1,
             label='measurements', markersize=2)
plt.legend(loc="upper right")
plt.xlabel('Distance - axis')
plt.ylabel('Voltage - axis')
plt.title('Intensity vs Distance- sin_1000hz')
#plt.show()
plt.savefig('Intensity vs Distance- sin_1000hz')
