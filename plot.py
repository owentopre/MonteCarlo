import numpy as np
from matplotlib import pyplot as plt

def quadratic(x, c0, c1, c2):
    """
    A function defining a quadratic equation.

    Parameters
    ----------
    x: (list, array)
        A set of values at which the function is evaluated.
    c0: float
        The coefficient of the x^0 term
    c1: float
        The coefficient of the x^1 term
    c2: float
        The coefficient of the x^2 term

    Returns
    -------
    y: array
        The function evaluated at x.
    """

    xs = np.array(x)  # make sure x is an array
    return c0 + c1 * xs + c2 * xs ** 2
    

np.random.seed(42)  # set seed for reproducible random data

# values to set up quadratic
n = 20  # number of data points
x = np.linspace(-10, 10, n)  # points at which to evaluate the function
coeffs = [-7.6, 3.4, 1.7]  # quadratic coefficients

# create data: quadratic + Gaussian noise with zero mean and standard deviation of 20
data = quadratic(x, coeffs[0], coeffs[1], coeffs[2]) + np.random.normal(0.0, 20.0, n)

# perform line fitting with polyfit
order = 2  # polynomial of order 2, i.e., a quadratic
c = np.polyfit(x, data, order)

# plot the data and the best fit line
fig, ax = plt.subplots()
ax.scatter(x, data, label="data")  # plot the data
ax.plot(x, quadratic(x, c[1], c[0]), 'k', lw=2, label="Best fit")  # plot the "best fit" line
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.text(0, -8, 'Best fit gradient: {0:.2f}'.format(c[0]), fontsize=14)
ax.text(0, -9.5, 'Best fit y-intercept is {0:.2f}'.format(c[1]), fontsize=14)
ax.legend()

fig.tight_layout()
plt.show()