import numpy as np

# curve-fit() function imported from scipy
from scipy.optimize import curve_fit

from matplotlib import pyplot as plt

# numpy.linspace with the given arguments
# produce an array of 40 numbers between 0
# and 10, both inclusive
import intensity_vs_distance

x = intensity_vs_distance.max_voltage_list()[0]
print(x)
y_array = intensity_vs_distance.max_voltage_list()[1]
y = [part[0] for part in y_array]
print(y)

# Test function with coefficients as parameters
def test(x, a, b, c):
    return a*((b-x)**c)


# curve_fit() function takes the test-function
# x-data and y-data as argument and returns
# the coefficients a and b in param and
# the estimated covariance of param in param_cov
param, param_cov = curve_fit(lambda x,a,b,c:a*(x-b)**c, x, y,sigma=[0.3]*len(x))

print("Sine function coefficients:")
print(param)
print("Covariance of coefficients:")
print(param_cov)

xs = np.linspace(min(x),max(x),10**3)
ys = param[0]*(xs-param[1])**param[2]
plt.plot(xs,ys)
plt.errorbar(x, y,yerr=[0.003]*len(x),fmt='o',ecolor='r',label='delta')
plt.show()
